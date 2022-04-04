import React, { useState } from "react"
import { NavLink } from "react-router-dom";
import Container from '@mui/material/Container';
import AppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import Box from "@mui/material/Box";
import MenuItem from "@mui/material/MenuItem";
import MenuIcon from '@mui/icons-material/Menu';

import DrawerComponent from "./DrawerComponent"

function Navbar() {
    const [openDrawer, setOpenDrawer] = useState(false)

    return (
        <AppBar color="secondary" position="static">
            <Container maxWidth="none">
                <Toolbar>
                    <Box sx={{ flexGrow: 1, display: { xs: "none", md: "flex" } }}>
                        <MenuItem
                            autoFocus
                            style={{ color: "white" }}
                        >
                            <NavLink to="/" className="navbar-link">Home</NavLink>
                        </MenuItem>
                        <MenuItem
                            autoFocus
                        >
                            <NavLink to="/about" className="navbar-link">About</NavLink>
                        </MenuItem>
                        <MenuItem
                            autoFocus
                        >
                            <NavLink to="/users" className="navbar-link">Users</NavLink>
                        </MenuItem>
                        <MenuItem
                            autoFocus
                        >
                            <NavLink to="/color" className="navbar-link">Top Color</NavLink>
                        </MenuItem>
                    </Box>
                    <Box sx={{ flexGrow: 1, display: { xs: "flex", md: "none" } }}>
                        <MenuIcon 
                            onClick={setOpenDrawer}
                            style={{ cursor: "pointer" }}
                        />
                        <DrawerComponent
                            openDrawer={openDrawer}
                            setOpenDrawer={setOpenDrawer}
                        />
                    </Box>
                </Toolbar>
            </Container>
        </AppBar>
    )
}

export default Navbar