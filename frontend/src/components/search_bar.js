import React, {Component} from 'react';
import '../styles/styles.css'
import axios from 'axios'
import {SearchInput} from 'evergreen-ui'
class search_bar extends Component {
    constructor() {
      super();
      // this.handleSubmit = this.handleSubmit.bind(this);
      this.state = {
          searchQuery : ''
      }
    }

    handleSubmit(event) {
        alert(this.state.searchQuery);
        console.log(this.state.searchQuery);

        let data = this.state.searchQuery;
        axios.post('/user/', {'search' : data}).then(response => this.setState({data: response.response}))
    }

    render() {
        return (
            <div className="search-bar">
              <form className="example">
                {/*<input id='search' value={this.state.searchQuery} type="text" placeholder="Search.." name="search" onChange={this.setQuery}/>*/}
                <SearchInput
                    name={'text-input-name'}
                    placeholder={'Search for Users'}
                    onChange={e => this.setState({searchQuery: e.target.value})}
                    value={this.state.value}
                />
                <button type={'submit'}><i className="fa fa-search"></i></button>
              </form>
            </div>
        );
    }
}

export default search_bar;
