import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import { Provider } from 'react-redux';

import Quotes from './components/Quotes';
import PostQuotes from './components/Postquotes';
import store from './store';

class App extends Component {
  render() {
    return (
      <Provider store={store}>
        <div className="App">
          <header className="App-header">
            <img src={logo} className="App-logo" alt="logo" />
              <h2>My Quotes App</h2>
          </header>
          <PostQuotes />
          <hr />
          <Quotes />
        </div>
      </Provider>
    );
  }
}

export default App;
