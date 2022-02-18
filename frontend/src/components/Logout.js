import React, {useState, useEffect} from 'react';
import axiosInstance from "../axios";
import { useNavigate } from 'react-router-dom';

function Logout(props) {
    const {
		isLoggedIn: [isLoggedIn, setLogin]
	  } = {
		...(props.state)
	  };

    useEffect(() => {
        localStorage.removeItem('access_token')
        localStorage.removeItem('refresh_token')
        localStorage.setItem('is_logged_in', 0)
        setLogin(0)
    })
    return (
        <React.Fragment>
            <h1>You have been successfully logged out</h1>
        </React.Fragment>
    );
}

export default Logout;