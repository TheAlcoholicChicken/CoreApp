import React from 'react';
import ReactDOM from 'react-dom';
import LoginPage from './components/login_component.js';
import CreateAcc from "./components/create_account.js";
import './index.css';

import * as serviceWorker from './serviceWorker';
import './styles/styles.css'
import LandingComponennt from './components/landing.js'


ReactDOM.render(
    <div className={'app-body container'}>
      <LoginPage />
      <br/>
      <CreateAcc />
        <LandingComponennt/>
    </div>
    , document.getElementById('root'));


// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: http://bit.ly/CRA-PWA
serviceWorker.unregister();
