import React, {Component} from 'react';
import '../styles/styles.css'
import axios from 'axios'
import {SearchInput} from 'evergreen-ui'
class search_bar extends Component {
    constructor() {
      super();
      this.handleSubmit = this.handleSubmit.bind(this);
      this.setQuery = this.setQuery.bind(this);
      this.state = {
          searchQuery : ''
      }
    }

    handleSubmit(event) {
        console.log(this.state.searchQuery);
        let data = this.state.searchQuery;
        axios.post('/user/', {'search' : data}).then(response => this.setState({data: response.response}))
    }

    setQuery(event) {
        this.setState({searchQuery : event.target.value})
    }

    render() {
        return (
            <div className="search-bar">
              <form className="example" onSubmit={this.handleSubmit}>
                {/*<input id='search' value={this.state.searchQuery} type="text" placeholder="Search.." name="search" onChange={this.setQuery}/>*/}
                <SearchInput
                    name={'text-input-name'}
                    placeholder={'Search for Users'}
                />
                <button type={'submit'}><i className="fa fa-search"></i></button>
              </form>
            </div>
        );
    }
}

export default search_bar;
