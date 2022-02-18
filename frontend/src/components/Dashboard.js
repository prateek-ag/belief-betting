import React, {useState, useEffect} from 'react';
import axiosInstance from "../axios";
import { useNavigate } from 'react-router-dom';

function Dashboard() {
    const nav = useNavigate()
    const [name, setName] = useState('');

    useEffect(() => {
        axiosInstance
			.get(`user/dashboard/`, {})
			.then((res) => {
                console.log(res)
				setName(res.data.first_name + res.data.last_name)
			})
            .catch(error => {
                nav('/login')
            });
    })
    return (
        <React.Fragment>
            <h1>Hello {name}, you have been logged in</h1>
        </React.Fragment>
    );
}

export default Dashboard;