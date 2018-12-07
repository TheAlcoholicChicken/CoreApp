import React, {Component} from 'react';
import '../styles/styles.css'
import axios from 'axios'
import {Combobox} from 'evergreen-ui'
class search_bar extends Component {
    constructor() {
      super();
      // this.handleSubmit = this.handleSubmit.bind(this);
      this.state = {
          searchQuery : ' ',
          searchItems : []
      }
    }

    componentDidMount() {
        axios.post('/user/search_user/',  {
            search: this.state.searchQuery,
            id_only: false
        }).then(
            response => {
                // console.log("Search response: " + response.data);
                this.setState({searchItems: response.data.users})
            }
        );
    }

    changePages(url) {
        axios.post('/user/search_user/', {
            search: url,
            id_only: false
        }).then (
            res => {
                window.location.replace(res.data.users[0].user_profile_link);
            }
        )
    }
    render() {
        let searchDropdownItems = this.state.searchItems;
        let searchNames = [];
        console.log(searchDropdownItems);
        searchDropdownItems.forEach((value, key)=>{
            searchNames.push(searchDropdownItems[key].data.first_name);
        });

        return (
            <div className="search-bar">
              <form className="example">
                {/*<input id='search' value={this.state.searchQuery} type="text" placeholder="Search.." name="search" onChange={this.setQuery}/>*/}
                <Combobox
                  items={searchNames}
                  onChange={e=> this.changePages(e)}
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
