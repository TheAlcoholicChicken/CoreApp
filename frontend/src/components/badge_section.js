import React, {Component} from 'react';
import '../styles/styles.css'
import axios from 'axios'
import {Avatar, Text} from 'evergreen-ui'

class Badge extends React.Component {
    render() {
        return (
            <div className={'badge-list'}>
                {/*<img src={"Hello World"}/>*/}
                <button className={'app-badge'}>
                </button>
            </div>
        );
    }
}

class user_badge extends Component {

    constructor(props) {
        super(props);
        this.state = {
            badge: [{
                app_name: "Hangman",
                app_url: "",
                app_icon: "https://i.pinimg.com/originals/af/41/cb/af41cbe06748a6f631139915a810e2f6.png", // url to image
                badge_text: "5%th in Hangman"
            }, {
                app_name: "Quiz",
                app_url: "",
                app_icon: "https://i.pinimg.com/originals/af/41/cb/af41cbe06748a6f631139915a810e2f6.png", // url to image
                badge_text: "8%th in Quizapp"
            }
            ]
        }
    }

    componentDidMount() {

        axios.post('get_badges/', {
            user_id : window.location.href.split("/").pop()
        }).then(
            response => this.setState({badge: response.data.badges})
        ).catch(error => {
            console.log(error)
        });
    }

    renderBadge() {
        let badgeElement = [];
        console.log(this.state.badge);
        if (this.state.badge !== undefined) {
            this.state.badge.map((badge) => {
                badgeElement.push(
                    <li className={'badge-element'}>
                        <Avatar
                            size={50}
                            src={badge.app_icon}
                        />
                        <Text>{badge.badge_text}</Text>
                    </li>)
            });
        }
        return badgeElement;
    }

    render() {
        return (
            <div className="badge-section">
                <ul className={"badges"}>

                    {this.renderBadge()}
                </ul>
            </div>
        );
    }
}

export default user_badge;