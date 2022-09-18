import React, {useState, useEffect} from 'react';
import axiosInstance from "../axios";
import { useNavigate, useParams } from 'react-router-dom';
import Paper from '@material-ui/core/Paper';
import Box from '@material-ui/core/Box';
import Card from '@material-ui/core/Card';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';
import Grid from '@material-ui/core/Grid'

import BettingForm from './BettingForm'

const useStyles = makeStyles((theme) => ({
	paper: {
		marginTop: theme.spacing(8),
		display: 'flex',
		flexDirection: 'column',
		alignItems: 'left',
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

const bull = (
    <Box
      component="span"
      sx={{ display: 'inline-block', mx: '2px', transform: 'scale(0.8)' }}
    >
      •
    </Box>
  );

export default function Events() {
    let { eventID } = useParams()
    const [event, setEvent] = useState([]);

    useEffect(() => {
        let mounted = true;
        axiosInstance
			.get(`events/${eventID}`, {})
			.then((res) => {
                if (mounted) {
                    console.log(res.data)
                    setEvent(res.data)
                }
			})
            .catch(error => {
				console.log('events/${eventID}')
                console.log(error)
            });
        return () => mounted = false;    
    }, [])

    const classes = useStyles();

    return (
        <Grid container spacing={2} className={classes.paper}>

        {/* Header */}
            
        <Grid container item xs={12} direction="column">
            <Card>
                <CardContent>
                    <Grid container>
                    <Grid container item xs={6} direction="column" >
                    <Typography sx={{ fontSize: 12 }} color="text.secondary">{event.category}</Typography>
                    <Typography variant="h4" component="div">{event.name}</Typography>
                    </Grid>
                    <Grid container item xs={6} direction="column" >
                    <Typography variant="h6">
                    Trade Volume: {event.volume}
                    </Typography>
                    <Typography variant="h6">
                        Market Ends On: {event.end_date}
                    </Typography>
                    </Grid>
                    </Grid>
                </CardContent>
            </Card>
        </Grid>
            

        {/* // Body */}
        <Grid container item>
        <Grid container spacing={2}>
            <Grid container item xs={8} direction="column">
            <Card>
                <CardContent>
                    <h1>Hello</h1>
                </CardContent>
            </Card>
            </Grid>
            <Grid container item xs={4} direction="column">
                <Card>
                    <CardContent>
                        <BettingForm></BettingForm>
                    </CardContent>
                </Card>
            </Grid>
        </Grid>
        </Grid>
        </Grid>
    );


}