import React, {Component} from 'react';
import '../styles/login.css';


class login_page extends Component {
  constructor() {
    super();
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleSubmit(event) {
    event.preventDefault();
    const data = new FormData(event.target);

    fetch('/user/login/', {
      method: 'POST',
      body: data,
    });
  }

  render() {
      return (
          //<h1> Welcome to BadgeBook!</h1>
          <form onSubmit={this.handleSubmit}>
            <label htmlFor="email">Enter your email</label>
            <input id="email" name="email" type="email" />

            <label htmlFor="password">Enter password</label>
            <input id="password" name="password" type="text" required/>

            <button>LogIn!</button>
          </form>
      );
  }
}

export default login_page;
