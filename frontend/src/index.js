import React from 'react';
import ReactDOM from 'react-dom';
import {
  BrowserRouter,
  Routes,
  Route
} from "react-router-dom";

import './index.css';

import App from './App';
import Login from './components/Login';
import Register from './components/Register';
import Dashboard from './components/Dashboard'
import Header from './components/Header';

const routing = (
  <BrowserRouter>
  <Header />
      <Routes>
        <Route exact path="/" element={<App />}/>
        <Route exact path="/login" element={<Login />}/>
        <Route exact path="/register" element={<Register />}/>
        <Route exact path="/dashboard" element={<Dashboard />}/>
      </Routes>
  </BrowserRouter>
);

ReactDOM.render(routing, document.getElementById('root'));

// import reportWebVitals from './reportWebVitals';



// // If you want to start measuring performance in your app, pass a function
// // to log results (for example: reportWebVitals(console.log))
// // or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
// reportWebVitals();
