import React, {Component} from 'react';
import '../styles/styles.css'
import axios from 'axios'

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

    constructor() {
        super();
        this.state = {
            badge: []
        }
    }

    componentDidMount() {
        axios.post('user/get_badges', {
            user_id : 'something'
        }).then(
            response => this.setState({badge: response.badges})
        ).catch(error => {
            console.log(error)
        });
    }

    renderBadge() {
        this.state.badge.map((item, index) => {
            return <li key={index}>{item}</li>
        });
    }

    render() {
        return (
            <div className="badge-section">
                <h1>
                    {this.renderBadge()}
                </h1>
            </div>
        );
    }
}

export default user_badge;