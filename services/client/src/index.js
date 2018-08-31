import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import axios from 'axios';

import UsersList from './components/UsersList';

class App extends Component {
  constructor() {
    super();
    this.state = {
      users: [],
    }
  }
  componentDidMount() {
    this.getUsers();
  }
  getUsers() {
    axios.get(`${process.env.REACT_APP_USERS_SERVICE_URL}/users`)
    .then((res) => {
      const { users } = res.data.data;
      this.setState({ users });
    })
    .catch((err) => {
      return console.log(err);
    });
  }
  render() {
    return (
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
    );
  }
};

ReactDOM.render(
  <App />,
  document.getElementById('root')
);