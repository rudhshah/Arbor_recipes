import React from 'react';
import ReactDOM from 'react-dom';
import Search from './search';
import App from './app';
import Addbar from './addbar';

// This method is only called once
ReactDOM.render(
  // Insert the likes component into the DOM
  <App />,
  document.getElementById('reactEntry'),
);
