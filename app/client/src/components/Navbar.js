import React from "react"
import Container from '@mui/material/Container';
import AppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import Box from "@mui/material/Box";
import MenuItem from "@mui/material/MenuItem";
import {NavLink} from "react-router-dom";



function Navbar() {
    return (
        <AppBar color="secondary" position="static">
            <Container maxWidth="xl">
                <Toolbar>
                    <Box sx={{ flexGrow: 1, display: { xs: "none", md: "flex" } }}>
                        <MenuItem>
                            <NavLink to="/" className="navbar-link">Home</NavLink>
                        </MenuItem>
                        <MenuItem>
                            <NavLink to="/about" className="navbar-link">About</NavLink>
                        </MenuItem>
                        <MenuItem>
                            <NavLink to="/users" className="navbar-link">Users</NavLink>
                        </MenuItem>
                        <MenuItem>
                            <NavLink to="/color" className="navbar-link">Top Color</NavLink>
                        </MenuItem>
                    </Box>
                </Toolbar>
            </Container>
        </AppBar>
    )
}

export default Navbar