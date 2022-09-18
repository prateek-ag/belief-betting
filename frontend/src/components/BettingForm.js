import React, {useState, useEffect} from 'react';
import axiosInstance from "../axios";
import { useNavigate } from 'react-router-dom';

import PropTypes from 'prop-types';
import Tabs from '@material-ui/core/Tabs';
import Tab from '@material-ui/core/Tab';
import Typography from '@material-ui/core/Typography';
import Box from '@material-ui/core/Box';
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';
import Grid from '@material-ui/core/Grid'

export default function BettingForm() {
    const [outcome, setOutcome] = useState()

    const handleClick = (e) => {
        console.log(e.currentTarget.value)
        if (e.target.name == "yes") {
            setOutcome(1)
        }
        else if (e.target.name == "no") {
            setOutcome(0)
        }

        console.log(outcome)

    }


    return (
        <React.Fragment>
            <Box sx={{'width': '100%'}}>
                <Box sx={{ borderBottom: 1, borderColor: 'divider' }}>
                    <Tabs>
                        <Tab label="Buy"/>
                        <Tab label="Sell"/>
                    </Tabs>
                    <Typography variant="h7">Pick an Outcome</Typography>
                    <form>
                        <Grid container spacing={2}>
                            <Grid container item xs={6} direction="column">
                                <Button 
                                    variant="contained"
                                    onClick = {handleClick}
                                    value="yes">Yes</Button>
                            </Grid>
                            <Grid container item xs={6} direction="column">
                            <Button 
                                    variant="contained"
                                    onClick = {handleClick}
                                    value="no">No</Button>
                            </Grid>
                        </Grid>
                        <TextField
						variant="outlined"
						margin="normal"
						required
						fullWidth
						id="email"
						label="Email Address"
						name="email"
						autoComplete="email"
						autoFocus
						
					/></form>
					
                </Box>
            </Box>
        </React.Fragment>
    )
}