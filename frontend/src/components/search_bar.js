import React, {Component} from 'react';
import '../styles/styles.css'
import axios from 'axios'
import {Combobox} from 'evergreen-ui'
class search_bar extends Component {
    constructor() {
      super();
      // this.handleSubmit = this.handleSubmit.bind(this);
      this.state = {
          searchQuery : 'tony',
          searchItems : []
      }
    }

    handleSubmit(event) {
        alert(this.state.searchQuery);
        console.log(this.state.searchQuery);
        let data = this.state.searchQuery;
        axios.post('/user/', {'search' : data}).then(res => this.setState({data: res.users}))
    }


    componentDidMount() {
        axios.post('/user/search_user/',  {
            search: this.state.searchQuery
        }).then(
            response => {
                this.setState({searchItems: response.users})
            }
        );
        console.log(this.state.searchItems);
    }

    render() {
        let searchDropdownItems = this.state.searchItems;
        return (
            <div className="search-bar">
              <form className="example">
                {/*<input id='search' value={this.state.searchQuery} type="text" placeholder="Search.." name="search" onChange={this.setQuery}/>*/}
                <Combobox
                  items={searchDropdownItems}
                  onChange={e=> this.setState({searchItems: e.target.value})}
                  placeholder="Users"
                  autocompleteProps={{
                    // Used for the title in the autocomplete.
                    title: 'Users'
                  }}
                />
                <button type={'submit'}><i className="fa fa-search"></i></button>
              </form>
            </div>
        );
    }
}

export default search_bar;
