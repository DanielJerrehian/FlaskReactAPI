import React from "react"
import {NavLink} from "react-router-dom";


function Navbar() {
    return (
        <div className="navbar">
            <NavLink to="/" className="navbar-link">Home</NavLink>
            <NavLink to="/about" className="navbar-link">About</NavLink>
            <NavLink to="/users" className="navbar-link">Users</NavLink>
            <NavLink to="/color" className="navbar-link">Top Color</NavLink>
        </div>
    )
}

export default Navbar