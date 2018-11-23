import React, {Component} from 'react';
import '../styles/styles.css'
import axios from 'axios'

class user_description extends Component {

    constructor() {
        super();
        this.state = {
            firstName : '',
            lastName : '',
            profilePicture : '',
            userDescription : ''
        }

    }

    componentDidMount() {
        axios.get('user/something').then(
            response => this.setState({
                firstName : response.data.first_name,
                lastName : response.data.last_name,
                profilePicture : response.data.profile_picture,
                userDescription : response.data.description
            })
        )
    }

    render() {
        return (
            <div className="user-description">
                <div className={'user-name'}>
                    <h1>{this.state.firstName} {this.state.lastName}</h1>
                </div>
                <div className={'description'}>
                    {this.state.userDescription}
                </div>
            </div>
        );
    }
}

export default user_description;