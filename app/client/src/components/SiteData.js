import React from "react"

function SiteData(props) {
    return ( 
        <div className="site-data">
            <p>This project demonstrates a frontend made in React and backend done with Python Flask.</p>
            <p>Here's some information about the project:</p>
            <ul>
                <li className="data">Project Name: {props.data.projectName}</li>
                <li className="data">Total Users: {props.data.userCount}</li>
                <li className="data">Top Favorite Color: {props.data.topFavoriteColor}</li>
            </ul>
            <hr className="line"></hr>
        </div>
    )
}

export default SiteData