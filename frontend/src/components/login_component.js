import React, {Component} from 'react';
import '../styles/styles.css'


class user_profile extends Component {
    render() {
        return (
            <div className="login-fields">
                <input type={'email'} placeholder={"Enter your email."}></input>
                <input type={'password'}></input>
                <button type={'submit'}>Submit</button>
            </div>
        );
    }
}

export default user_profile;