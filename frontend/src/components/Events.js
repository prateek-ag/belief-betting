import React, {useState, useEffect} from 'react';
import axiosInstance from "../axios";
import { useNavigate } from 'react-router-dom';

import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Container from '@material-ui/core/Container';
import { makeStyles } from '@material-ui/core/styles';
import CssBaseline from '@material-ui/core/CssBaseline';
import Paper from '@material-ui/core/Paper';

const useStyles = makeStyles((theme) => ({
	paper: {
		marginTop: theme.spacing(8),
		display: 'flex',
		flexDirection: 'column',
		alignItems: 'center',
        width: '80%',
        marginLeft: 'auto',
        marginRight: 'auto',
	},
	avatar: {
		margin: theme.spacing(1),
		backgroundColor: theme.palette.secondary.main,
	},
	form: {
		width: '80%', // Fix IE 11 issue.
		marginTop: theme.spacing(1),
	},
	submit: {
		margin: theme.spacing(3, 0, 2),
	},
}));

function Events() {
    const nav = useNavigate()
    const [events, setEvents] = useState([]);

    useEffect(() => {
        let mounted = true;
        axiosInstance
			.get(`events/`, {})
			.then((res) => {
                if (mounted) {
                    setEvents(res.data)
                }
			})
            .catch(error => {
                console.log(error)
            });
        return () => mounted = false;    
    }, [])

    const classes = useStyles();

    return (

        <div className={classes.paper}>
         <h1>Event List</h1>
         
         <TableContainer component={Paper}>
            <Table sx={{ minWidth: '50%' }} aria-label="simple table">
            <TableHead><TableRow style={{fontWeight:"bold"}}>
            <TableCell>Name</TableCell>
            <TableCell align="right">Start Date</TableCell>
            <TableCell align="right">End Date</TableCell>
            <TableCell align="right">Category</TableCell>
          </TableRow></TableHead>
            <TableBody>
           {events.map(event => 
           <TableRow key={event.id}>
               <TableCell>{event.name}</TableCell>
               <TableCell align="right">{event.start_date}</TableCell>
               <TableCell align="right">{event.end_date}</TableCell>
               <TableCell align="right">{event.category}</TableCell>
               </TableRow>
           )}
           </TableBody>
           </Table>
         </TableContainer>


       </div>
      );
    }

export default Events;