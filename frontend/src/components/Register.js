import React, { useState } from "react";
import axiosInstance from "../axios";
import { useNavigate } from 'react-router-dom';
//MaterialUI
import Avatar from '@material-ui/core/Avatar';
import Button from '@material-ui/core/Button';
import CssBaseline from '@material-ui/core/CssBaseline';
import TextField from '@material-ui/core/TextField';
import Link from '@material-ui/core/Link';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';


const useStyles = makeStyles((theme) => ({
	paper: {
		marginTop: theme.spacing(8),
		display: 'flex',
		flexDirection: 'column',
		alignItems: 'center',
	},
	avatar: {
		margin: theme.spacing(1),
		backgroundColor: theme.palette.secondary.main,
	},
	form: {
		width: '100%', // Fix IE 11 issue.
		marginTop: theme.spacing(1),
	},
	submit: {
		margin: theme.spacing(3, 0, 2),
	},
}));

export default function Register(props) {

	const {
		isLoggedIn: [isLoggedIn, setLogin]
	  } = {
		...(props.state)
	  };

	const nav = useNavigate();
	const initialFormData = Object.freeze({
		email: '',
        firstName: '',
        lastName: '',
		password: '',
	});

	const [formData, updateFormData] = useState(initialFormData);

	const handleChange = (e) => {
		updateFormData({
			...formData,
			[e.target.name]: e.target.value.trim(),
		});
	};

	const handleSubmit = (e) => {
		e.preventDefault();

		axiosInstance
			.post(`user/register/`, {
				email: formData.email,
                first_name: formData.firstName,
                last_name: formData.lastName,
				password: formData.password,
			})
			.then((res) => {
				localStorage.setItem('access_token', res.data.access);
				localStorage.setItem('refresh_token', res.data.refresh);
				localStorage.setItem('is_logged_in', 1)
				setLogin(1)
				axiosInstance.defaults.headers['Authorization'] =
					'JWT ' + localStorage.getItem('access_token');
				nav('/');
			});
	};

	const classes = useStyles();

	return (
		<Container component="main" maxWidth="xs">
			<CssBaseline />
			<div className={classes.paper}>
				<Avatar className={classes.avatar}></Avatar>
				<Typography component="h1" variant="h5">
					Sign Up
				</Typography>
				<form className={classes.form} noValidate>
					<TextField
						variant="outlined"
						margin="normal"
						required
						fullWidth
						id="email"
						label="Email Address"
						name="email"
						autoComplete="email"
                        required
						autoFocus
						onChange={handleChange}
					/>
                    <TextField
						variant="outlined"
						margin="normal"
						required
						fullWidth
						name="firstName"
						label="First Name"
						id="firstName"
						autoComplete="given-name"
                        required
						onChange={handleChange}
					/>
                    <TextField
						variant="outlined"
						margin="normal"
						required
						fullWidth
						name="lastName"
						label="Last Name"
						id="lastName"
						autoComplete="family-name"
                        required
						onChange={handleChange}
					/>
                    <TextField
						variant="outlined"
						margin="normal"
						required
						fullWidth
						name="password"
						label="Password"
						type="password"
						id="password"
						autoComplete="current-password"
                        required
						onChange={handleChange}
					/>
					<Button
						type="submit"
						fullWidth
						variant="contained"
						color="primary"
						className={classes.submit}
						onClick={handleSubmit}
					>
						Sign Up
					</Button>
					<Grid container>
						<Grid item>
							<Link href="/login" variant="body2">
								{"Already Have an account? Sign In"}
							</Link>
						</Grid>
					</Grid>
				</form>
			</div>
		</Container>
	);
}