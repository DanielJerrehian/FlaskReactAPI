import React from 'react';

function UserDetails(props) {
    const user = props.user
    return (
        <li key={user.id} className="data">
            <span className="italics"> Name:</span> {user?.name === "None" ? "N/A" : user.name},
            <span className="italics"> Age:</span> {user?.age === "None" ? "N/A" : user.age},
            <span className="italics"> Favorite Color:</span> {user?.favorite_color === "None" ? "N/A" : user.favorite_color}
        </li>
    )
};

export default UserDetails