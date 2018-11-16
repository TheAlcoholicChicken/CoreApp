import React, {Component} from 'react';
import '../styles/styles.css'

class search_bar extends Component {
    render() {
        return (
            <div className="search-bar">

              <form class="example" action="">
                <input type="text" placeholder="Search.." name="search" />
                <button type="submit"><i class="fa fa-search"></i></button>
              </form>
            </div>
        );
    }
}

export default search_bar;
