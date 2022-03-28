import React, { useState, useEffect } from 'react'
import axios from "axios"

import LoadingData from './LoadingData'

function Color() {
    const [data, setData] = useState([{}])

    useEffect(() => {
        axios
            .get("/top-color")
            .then(response => {
                setData(response.data)
            })
    }, [])

    return (
        <div>
            {(typeof data.topFavoriteColor != "undefined") 
                ? 
                    (
                        <div>
                            <h1>User Favorite Color</h1>
                            <ul>
                                <li className="data">According to our survey, our users favorite color is {data.topFavoriteColor}</li>
                            </ul>
                        </div>                 
                    )
                : 
                    (<LoadingData />)}
        </div>
    )
}

export default Color