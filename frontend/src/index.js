import React, { useState } from 'react';
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
import Events from './components/Events'
import Logout from './components/Logout'

function Index() {
  const [isLoggedIn, setLogin] = useState(localStorage.getItem("is_logged_in"))

  return (
    <BrowserRouter>
    <Header state={{ isLoggedIn: [isLoggedIn, setLogin] }}/>
        <Routes>
          <Route exact path="/" element={<App />}/>

          <Route exact path="/login" element={<Login state={{ isLoggedIn: [isLoggedIn, setLogin] }}/>}>
            <Route path='/login/failed_login' element={<p>Username or password incorrect</p>} />
          </Route>

          <Route exact path="/logout" element={<Logout state={{ isLoggedIn: [isLoggedIn, setLogin] }}/>}/>
          <Route exact path="/register" element={<Register state={{ isLoggedIn: [isLoggedIn, setLogin] }}/>}/>
          <Route exact path="/dashboard" element={<Dashboard />}/>
          <Route exact path="/events" element={<Events />}/>
        </Routes>
    </BrowserRouter>
  );
}

ReactDOM.render(<Index />, document.getElementById('root'));

// import reportWebVitals from './reportWebVitals';



// // If you want to start measuring performance in your app, pass a function
// // to log results (for example: reportWebVitals(console.log))
// // or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
// reportWebVitals();
