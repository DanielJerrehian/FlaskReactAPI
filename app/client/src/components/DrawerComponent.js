import React from 'react';
import { useNavigate } from "react-router-dom";

import Drawer from '@mui/material/Drawer';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemText from '@mui/material/ListItemText';


function DrawerComponent(props) {
    const navigate = useNavigate();

    function navigatePage(link) {
        function handleClick() {
            navigate(`/${link}`);
            props.setOpenDrawer(false);
        }
        return () => handleClick()
    };

    return (
        <Drawer
            open={props.openDrawer}
            onClose={() => props.setOpenDrawer(false)}
            anchor="left"
        >
            <List>
                <ListItem
                    style={{ cursor: "pointer" }}
                >
                    <ListItemText
                        onClick={navigatePage("")}
                        primary="Home"
                        
                    />
                </ListItem>
                <ListItem
                    style={{ cursor: "pointer" }}
                >
                    <ListItemText
                        onClick={navigatePage("about")}
                        primary="About"
                    />
                </ListItem>
                <ListItem
                    style={{ cursor: "pointer" }}
                >
                    <ListItemText
                        onClick={navigatePage("users")}
                        primary="Users"
                    />
                </ListItem>
                <ListItem
                    style={{ cursor: "pointer" }}
                >
                    <ListItemText
                        onClick={navigatePage("color")}
                        primary="Top Color"
                    />
                </ListItem>
            </List>
        </Drawer>
    )
}

export default DrawerComponent