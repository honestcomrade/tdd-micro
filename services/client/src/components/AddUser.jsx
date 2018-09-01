import React from 'react';

const AddUser = (props) => {
  return (
    <form onSubmit={(event) => event.preventDefault()}>
      <div className="field">
        <input 
          name="username"
          className="input is-large"
          type="text"
          placeholder="Username"
          required
        />
      </div>
      <div className="field">
        <input 
          name="email"
          className="input is-large"
          type="email"
          placeholder="Email"
          required
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