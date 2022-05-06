import React, { useState, useEffect } from 'react'
import axios from "axios"

import Welcome from '../components/Welcome'
import SiteData from '../components/SiteData'
import LoadingData from '../components/LoadingData'
import PostForm from '../components/PostForm'
import Error from '../components/Error';


function Home() {
    const [data, setData] = useState([{}])
    const [formData, setFormData] = useState({name: "", age: "", favoriteColor: ""})
    const [isLoading, setIsLoading] = useState(false)
    const colorOptions = ["Black", "White", "Red", "Green", "Yellow", "Blue", "Pink", "Gray", "Brown", "Orange", "Purple"]


    useEffect(() => {
        setIsLoading(true);
        axios
            .get("/site-data")
            .then(response => {
                setData(response.data)
                setIsLoading(false);
            })
    }, [])

    function handleSubmit(event) {
        event.preventDefault()
        axios
            .post("/user-data", formData)
            .then(response => {
                setData(response.data)
                setFormData({ name: "", age: "", favoriteColor: "" })
            })
    }

    function handleChange(event) {
        const {name, value} = event.target
        setFormData(prevFormData => {
            return {
                ...prevFormData,
                [name]: value
            }
        })
    }

    return (
        <div>
            <Welcome />
            {
                isLoading 
                    ? 
                        <LoadingData loading={isLoading} /> 
                    :
                        (typeof data?.userCount != "undefined")
                            ? 
                                <SiteData data={data} /> 
                            : 
                                <Error message="That didn't work, please try again" returnHome={false} />
            }
            <PostForm handleSubmit={handleSubmit} handleChange={handleChange} formData={formData} colorOptions={colorOptions} />
        </div>
    )   
}

export default Home