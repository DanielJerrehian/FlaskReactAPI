import React, { useState, useEffect } from "react"
import axios from "axios"

import LoadingData from '../components/LoadingData'
import UserDetails from '../components/UserDetails'

function Users() {
    const [data, setData] = useState([{}])

    useEffect(() => {
        axios
            .get("/user-data")
            .then(response => {
                setData(response?.data)
            })
    }, [])

    return (
        <div>
            {(typeof data?.userCount != "undefined")
                ?
                (
                    <div>
                        <h1>Users</h1>
                        <div>
                            <h3>General user statistics:</h3>
                            <ul>
                                <li className="data">User Count: {data?.userCount}</li>
                                <li className="data">Average User Age: {data?.averageAge}</li>
                            </ul>
                        </div>
                        <div>
                            <h3>The last three users who filled out the survey were:</h3>
                            <ol>
                                {data?.lastThreeUsers.map(user => (
                                    <UserDetails user={user} key={user.id} />
                                ))}
                            </ol>
                        </div>
                    </div>
                )
                :
                (<LoadingData />)}
        </div>
    )
}

export default Users