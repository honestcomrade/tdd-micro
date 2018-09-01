import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import axios from 'axios';

import UsersList from './components/UsersList';
import AddUser from './components/AddUser';

class App extends Component {
  constructor() {
    super();
    this.state = {
      users: [],
      username: '',
      email: '',
    };
    this.addUser = this.addUser.bind(this);
    this.handleChange = this.handleChange.bind(this);
  };
  componentDidMount() {
    this.getUsers();
  };
  getUsers() {
    axios.get(`${process.env.REACT_APP_USERS_SERVICE_URL}/users`)
    .then((res) => {
      const { users } = res.data.data;
      this.setState({ users });
    })
    .catch((err) => {
      return console.log(err);
    });
  };
  addUser(event) {
    event.preventDefault();
    console.log(this.state);
    const data = { 
      username: this.state.username,
      email: this.state.email,
    };
    axios.post(`${process.env.REACT_APP_USERS_SERVICE_URL}/users`, data)
    .then((res) => {
      this.getUsers();
      this.setState({ username: '', email: ''})
    })
    .catch((err) => {
      return console.log(err);
    });
  };
  handleChange(event) {
    const obj = [];
    obj[event.target.name] = event.target.value;
    this.setState(obj);
  };
  render() {
    return (
      <div>
        <section className="section">
        <br />
        <h1 className="title is-1 is-1">Add a User</h1>
        <hr /><br />
          <AddUser
            username={this.state.username}
            email={this.state.email}
            addUser={this.addUser} 
            handleChange={this.handleChange}
          />
        </section>
        <section className="section">
          <div className="container">
            <div className="columns">
              <div className="column is-one-third">
                <br />
                <h1 className="title is-1 is-1">All Users</h1>
                <hr /><br />
                <UsersList
                  users={this.state.users}
                />
              </div>
            </div>
          </div>
        </section>
      </div>
    );
  };
};

ReactDOM.render(
  <App />,
  document.getElementById('root')
);