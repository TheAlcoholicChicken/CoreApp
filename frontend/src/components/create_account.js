import React, {Component} from 'react';
import '../styles/login.css'
import Popup from 'reactjs-popup'


class create_account extends Component {
  constructor() {
    super();
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleSubmit(event) {
    event.preventDefault();
    const data = new FormData(event.target);
    var post_request = {};
    data.forEach((value, key)=>{
      post_request[key] = value;
    });
    fetch('/user/create_account/', {
      method: 'POST',
      body: JSON.stringify(post_request),
    });
  }

  render() {
      // return (
      //   <form onSubmit={this.handleSubmit}>
      //     <label htmlFor="email">Enter your email</label>
      //     <input id="email" name="email" type="email" />
      //
      //     <label htmlFor="password">Enter password</label>
      //     <input id="password" name="password" type="text" required/>
      //
      //     <label htmlFor="password">Please confirm password</label>
      //     <input id="password" name="confirmPassword" type="text" required/>
      //
      //     <button>Create Account!</button>
      //   </form>
      // );
      return (
        <Popup
          trigger={<button className="button"> Create Account! </button>}
          modal
          closeOnDocumentClick
        >

          <form onSubmit={this.handleSubmit}>
            <label htmlFor="email">Enter your email</label>
            <input id="email" name="email" type="email" />

            <label htmlFor="password">Enter password</label>
            <input id="password" name="password" type="text" required/>

            <label htmlFor="password">Please confirm password</label>
            <input id="password" name="confirmPassword" type="text" required/>

            <label htmlFor="firstname">Enter your firstname</label>
            <input id="firstname" name="firstname" type="text" />

            <label htmlFor="lastname">Enter your lastname</label>
            <input id="lastname" name="lastname" type="text" />

            <button>Create Account!</button>
          </form>

        </Popup>
      );
  }
}

export default create_account;
