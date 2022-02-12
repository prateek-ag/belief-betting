import React from "react";
import {AppBar, Toolbar, Typography, CssBaseline} from '@material-ui/core'

function Header() {
	return (
		<React.Fragment>
			<CssBaseline />
			<AppBar
				position="static"
				color="white"
				elevation={0}
			>
				<Toolbar>
					<Typography variant="h6" color="inherit" noWrap>
						Prateek's Project
					</Typography>
                    
				</Toolbar>
			</AppBar>
		</React.Fragment>
	);
}


export default Header;