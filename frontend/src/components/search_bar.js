import React, {Component} from 'react';
import '../styles/styles.css'

class search_bar extends Component {
    constructor() {
      super();
      this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleSubmit(event) {
      event.preventDefault();
      const data = new FormData(event.target);

      fetch('/user/', {
        method: 'POST',
        body: data,
      }).then((response) => {
         return response.json()
      }).then((json) => {
          this.setState({data: json})
          alert(json['response'])
      })
    }

    render() {
        return (
            <div className="search-bar">
              <form class="example" onSubmit={this.handleSubmit}>
                <input type="text" placeholder="Search.." name="search" />
                <button type="submit" value="Search"><i class="fa fa-search"></i></button>
              </form>
            </div>
        );
    }
}

export default search_bar;
