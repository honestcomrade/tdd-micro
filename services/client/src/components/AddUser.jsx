import React from 'react';

const AddUser = (props) => {
  return (
    <form 
      onSubmit={(event) => props.addUser(event)}
    >
      <div className="field">
        <input 
          name="username"
          className="input is-large"
          type="text"
          placeholder="Username"
          required
          value={props.username}
          onChange={props.handleChange}
        />
      </div>
      <div className="field">
        <input 
          name="email"
          className="input is-large"
          type="email"
          placeholder="Email"
          required
          value={props.email}
          onChange={props.handleChange}
        />
      </div>
      <input 
        className="button is-primary is-large is-fullwidth"
        type="submit"
        value="submit"
      />
    </form>
  )
};

export default AddUser;