import React, {Component} from 'react';
import '../styles/styles.css'
import axios from 'axios'

class Badge extends React.Component {
    render() {
        return (
            <div className={'badge-list'}>
                <img src={props.foobar}/>
                <button className={'app-badge'}>
                    {this.props.valus}
                </button>
            </div>
        );
    }
}

class user_badge extends Component {

    constructor() {
        super();
        this.state = {
            badges: []
        }
    }

    componentDidMount() {
        axios.post('user/get_badges', {
            user_id : 'something'
        }).then(
            response=> this.setState({badges: response.badges})
        )
    }

    static renderBadge() {
        return <Badge value={props.badges[0].image}/>
    }

    render() {
        return (
            <div className="badge-section">
                <h1>
                    This is for the user's badges.
                </h1>
            </div>
        );
    }
}

export default user_badge;