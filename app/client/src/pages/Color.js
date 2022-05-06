import React, { useState, useEffect } from 'react'
import axios from "axios"

import LoadingData from '../components/LoadingData'
import Error from '../components/Error';

function Color() {
    const [data, setData] = useState([{}])
    const [isLoading, setIsLoading] = useState(false)

    useEffect(() => {
        setIsLoading(true);
        axios
            .get("/color-data")
            .then(response => {
                setIsLoading(false);
                setData(response.data)
            })
    }, [])

    return (
        <div>
            {
                isLoading 
                    ? 
                        <LoadingData loading={isLoading} /> 
                    :
                        (typeof data?.userCount != "undefined")
                            ? 
                                (
                                    <div>
                                        <h1>Top Colors</h1>
                                        <h3>According to our survey... our users:</h3>
                                        <ul>
                                            <li className="data">Favorite color is {data.topFavoriteColor}</li>
                                            <li className="data">Second favorite color is {data.secondFavoriteColor}</li>
                                        </ul>
                                    </div>
                                )
                            : 
                                <Error message="That didn't work, please try again" returnHome={false} />
            }
        </div>
    )
}

export default Color