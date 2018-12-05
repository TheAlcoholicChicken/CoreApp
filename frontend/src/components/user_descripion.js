import React, {Component} from 'react';
import '../styles/styles.css'
import axios from 'axios'
import {Avatar, Button,Textarea, TextInput} from 'evergreen-ui'

class user_description extends Component {

    constructor() {
        super();
        this.state = {
            firstName : 'John',
            lastName : 'Doe',
            profilePicture : 'https://i.kym-cdn.com/entries/icons/original/000/017/403/218_copy.jpg',
            userDescription : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
            userId : '',
            userlogin : true,
            edit: false
        }

    }

    componentDidMount() {
        let url = 'user/' + window.location.href.split("/").pop();
        console.log(url);
        axios.get(url).then(
            response => this.setState({
                userId : response.user_id,
                firstName : response.data.first_name,
                lastName : response.data.last_name,
                profilePicture : response.data.profile_picture,
                userDescription : response.data.description
            })
        ).catch(error => {
            console.log(error);
        });
    }

    renderEditButton() {
        if (this.state.userlogin) {
            return (
              <Button
                  marginRight={12}
                  iconBefore="edit"
                  onClick={this.setState({edit: !this.state.edit})}>
                  Edit
              </Button>
            );
        }
    }
    render() {
        {console.log(this.state.userlogin)}
        if (!this.state.edit) {
            return (
                <div className="user-description">
                    {this.renderEditButton()}
                    <Avatar
                        name={this.state.firstName + this.state.lastName}
                        size={250}
                        src={this.state.profilePicture}
                    />
                    <div className={'user-name'}>
                        <h1>{this.state.firstName} {this.state.lastName}</h1>
                    </div>
                    <div className={'description'}>
                        {this.state.userDescription}
                    </div>
                </div>
            );
        } else {
            return(
                <div className={"user-description"}>
                    <Avatar
                        name={this.state.firstName + this.state.lastName}
                        size={250}
                        src={this.state.profilePicture}
                    />
                    <div>
                    <TextInput
                        value={this.state.firstName}
                    />
                    <TextInput
                        value={this.state.lastName}
                    />
                    </div>
                    <Textarea
                        value={this.state.userDescription}
                        onChange={e=>this.setState({userDescription: e.target.value})}
                    />
                </div>
            )}
    }
}

export default user_description;