import json
import unittest

from project import db
from project.tests.base import BaseTestCase
from project.api.models import User

def add_user(username, email):
    user = User(username=username, email=email)
    db.session.add(user)
    db.session.commit()
    return user

class TestUserService(BaseTestCase):
  """Tests for the UserService."""

  def test_main_no_users(self):
    """Ensure the main route behaves correctly when no users exist in DB"""
    response = self.client.get('/')
    self.assertEqual(response.status_code, 200)
    self.assertIn(b'All Users', response.data)
    self.assertIn(b'<p>No users found...</p>', response.data)

  def test_base_route(self):
    """Ensure the /ping route behaves correctly."""
    response = self.client.get('/users/ping')
    data = json.loads(response.data.decode())
    self.assertEqual(response.status_code, 200)
    self.assertIn('pong!', data['message'])
    self.assertIn('success', data['status'])
    

  def test_single_user_get(self):
      """Ensure get single user behaves correctly."""
      user = add_user('michael', 'michael@mherman.org')
      with self.client:
          response = self.client.get(f'/users/{user.id}')
          data = json.loads(response.data.decode())
          self.assertEqual(response.status_code, 200)
          self.assertIn('michael', data['data']['username'])
          self.assertIn('michael@mherman.org', data['data']['email'])
          self.assertIn('success', data['status'])
  
  
  def test_single_user_no_id(self):
      """Ensure error is thrown if no id is provided."""
      with self.client:
          response = self.client.get('/users/notAnId')
          data = json.loads(response.data.decode())
          self.assertEqual(response.status_code, 404)
          self.assertIn('User does not exist', data['message'])
          self.assertIn('fail', data['status'])

  
  def test_single_user_incorrect_id(self):
      """Ensure error is thrown if the id does not exist."""
      with self.client:
          response = self.client.get('/users/127629')
          data = json.loads(response.data.decode())
          self.assertEqual(response.status_code, 404)
          self.assertIn('User does not exist', data['message'])
          self.assertIn('fail', data['status'])

  def test_all_users(self):
    """Ensure get all users behaves correctly."""
    add_user('michael', 'michael@mherman.org')
    add_user('john', 'john@smith.org')
    with self.client:
        response = self.client.get('/users')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data['data']['users']), 2)
        self.assertIn('success', data['status'])
        self.assertIn('michael', data['data']['users'][0]['username'])
        self.assertIn(
          'michael@mherman.org',data['data']['users'][0]['email'])
        self.assertIn('john', data['data']['users'][1]['username'])
        self.assertIn(
          'john@smith.org',data['data']['users'][1]['email'])
  

  def test_add_user(self):
    """Ensure a new user can be added to the database"""
    with self.client:
      response = self.client.post(
        '/users',
        data=json.dumps({
          'username': 'michael',
          'email': 'michael@mherman.org'
        }),
        content_type='application/json'
      )
      data = json.loads(response.data.decode())
      self.assertEqual(response.status_code, 201)
      self.assertIn('michael@mherman.org was added!', data['message'])
      self.assertIn('success', data['status'])
      

  def test_add_user_invalid_json(self):
    """Ensure error is thrown if the JSON object is empty"""
    with self.client:
      response = self.client.post(
        '/users',
        data=json.dumps({}),
        content_type='application/json'
      )
      data = json.loads(response.data.decode())
      self.assertEqual(response.status_code, 400)
      self.assertIn('Invalid payload.', data['message'])
      self.assertIn('fail', data['status'])

  
  def test_add_user_invalid_json_keys(self):
    """Ensure error is thrown if the JSON object does not have a username key"""
    with self.client:
      response = self.client.post(
        '/users',
        data=json.dumps({'email': 'michael@mherman.org'}),
        content_type='application/json'
      )
      data = json.loads(response.data.decode())
      self.assertEqual(response.status_code, 400)
      self.assertIn('Invalid payload.', data['message'])
      self.assertIn('fail', data['status'])
  

  def test_add_user_duplicate_email(self):
    """Ensure error is thrown if the email already exists"""
    with self.client:
      self.client.post(
        '/users',
        data=json.dumps({
          'username': 'michael',
          'email': 'michael@mherman.org'
        }),
        content_type='application/json',
      )
      response = self.client.post(
        '/users',
        data=json.dumps({
          'username': 'michael',
          'email': 'michael@mherman.org'
        }),
        content_type='application/json',
      )
      data = json.loads(response.data.decode())
      self.assertEqual(response.status_code, 400)
      self.assertIn(
        'Sorry. That email already exists.', data['message'])
      self.assertIn('fail', data['status'])



if __name__ == '__main__':
  unittest.main()