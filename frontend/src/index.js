import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import SearchBar from './components/search_bar'
import UserBadges from './components/badge_section'
import ProfilePicture from './components/profile_picture'
import UserDescription from './components/user_descripion'
import Footer from './components/footer'
import * as serviceWorker from './serviceWorker';
import './styles/styles.css'

ReactDOM.render(
    <div className={'app-body container'}>
        <SearchBar/>
        <ProfilePicture/>
        <UserBadges />
        <UserDescription/>
        <Footer/>
    </div>
    , document.getElementById('root'));

// window.onload(
    // fetch('https://management-system-api.herokuapp.com/', {
    // method: 'POST',
    // body: {
    //    'user_id': 'something',
    //    'token': "G5NIJdnKD7CyuPsy1zi4euipxnNhc0WJwGd8qJHS4XA",
    // },
    // }).then((response) => {
    //  return response.json()
    // }).then((json) => {
    //   for (let i = 0; i > json.badge.length; ++i) {
    //
    //   }
    // })
// );

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: http://bit.ly/CRA-PWA
serviceWorker.unregister();
