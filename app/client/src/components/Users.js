import React, { useState, useEffect } from "react"
import axios from "axios"

import LoadingData from './LoadingData'

function Users() {
    const [data, setData] = useState([{}])

    useEffect(() => {
        axios
            .get("/user-count")
            .then(response => {
                setData(response.data)
            })
    }, [])

    return (
        <div>
            {(typeof data.userCount != "undefined") 
                ? 
                    (
                        <div>
                            <h1>Users</h1>
                            <ul>
                                <li className="data">User Count: {data.userCount}</li>
                            </ul>
                        </div>                 
                    )
                : 
                    (<LoadingData />)}
        </div>
    )
}

export default Users