import React from 'react';

function UserDetails(props) {
    const user = props.user
    return (
        <li key={user.id} className="data">
            <span className="italics"> Name:</span> {user?.name === null ? "N/A" : user.name},
            <span className="italics"> Age:</span> {user?.age === null ? "N/A" : user.age},
            <span className="italics"> Favorite Color:</span> {user?.favorite_color === null ? "N/A" : user.favorite_color}
        </li>
    )
};

export default UserDetails