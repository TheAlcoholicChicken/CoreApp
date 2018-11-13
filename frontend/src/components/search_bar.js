import React, {Component} from 'react';
import '../styles/styles.css'

class search_bar extends Component {
    render() {
        return (
            <div className="search-bar">
                <h1>
                    <input type="text" className="form-control" id={'search-bar'}/>
                </h1>
            </div>
        );
    }
}

export default search_bar;