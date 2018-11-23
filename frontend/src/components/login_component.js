import React, {Component} from 'react';
import '../styles/login.css'


class login_page extends Component {
  constructor() {
    super();
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleSubmit(event) {
    event.preventDefault();
    const data = new FormData(event.target);

    fetch('/api/where am i sending this to', {
      method: 'POST',
      body: data,
    });
  }

  render() {
      return (
        <form onSubmit={this.handleSubmit}>

          <label htmlFor="email">Enter your email</label>
          <input id="email" name="email" type="email" />

          <label htmlFor="password">Enter password</label>
          <input id="password" name="password" type="text" required/>

          <button>Send data!</button>
        </form>
      );
  }
}

export default login_page;
