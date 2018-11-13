import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import SearchBar from './components/search_bar'
import UserBadges from './components/badge_section'
import ProfilePicture from './components/profile_picture'
import UserDescription from './components/user_descripion'
import * as serviceWorker from './serviceWorker';
import './styles/styles.css'

ReactDOM.render(
    <div>
    <SearchBar/>
    <UserBadges/>
    <UserDescription/>
    <ProfilePicture/>
    </div>
    , document.getElementById('root'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: http://bit.ly/CRA-PWA
serviceWorker.unregister();
