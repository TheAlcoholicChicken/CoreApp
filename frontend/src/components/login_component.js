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
    var request_body = {};
    console.log("Requesting login")
    data.forEach((value, key)=>{
      request_body[key] = value;
    });
    fetch('/user/login/', {
      method: 'POST',
      body: JSON.stringify(request_body),
    }).then(response => {
        console.log(response)
        return response.json()
    }).then(response => {
        console.log(response)
        if ("Login successful." == response["response"] && response["user_id"] != "") {
            window.location.href = window.location.href + response["url"]
        } else {
            alert(response["response"])
        }
    });
  }

  render() {
      return (
        <form onSubmit={this.handleSubmit}>
          <label htmlFor="email">Enter your email</label>
          <input id="email" name="email" type="email" />

          <label htmlFor="password">Enter password</label>
          <input id="password" name="password" type="text" required/>

          <button>Login</button>
        </form>
      );
  }
}

export default login_page;
