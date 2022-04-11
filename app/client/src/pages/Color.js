import React, { useState, useEffect } from 'react'
import axios from "axios"

import LoadingData from '../components/LoadingData'

function Color() {
    const [data, setData] = useState([{}])

    useEffect(() => {
        axios
            .get("/color-data")
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
                            <h1>Top Colors</h1>
                            <h3>According to our survey...</h3>
                            <ul>
                                <li className="data">Our users favorite color is {data.topFavoriteColor}</li>
                                <li className="data">Their second favorite color is {data.secondFavoriteColor}</li>
                            </ul>
                        </div>                 
                    )
                : 
                    (<LoadingData />)}
        </div>
    )
}

export default Color