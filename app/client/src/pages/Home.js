import React, { useState, useEffect } from 'react'
import axios from "axios"

import Welcome from '../components/Welcome'
import SiteData from '../components/SiteData'
import LoadingData from '../components/LoadingData'
import PostForm from '../components/PostForm'


function Home() {
    const [data, setData] = useState([{}])
    const [formData, setFormData] = useState({name: "", age: "", favoriteColor: ""})
    const colorOptions = ["Black", "White", "Red", "Green", "Yellow", "Blue", "Pink", "Gray", "Brown", "Orange", "Purple"]

    useEffect(() => {
        axios
            .get("/site-data")
            .then(response => {
                setData(response.data)
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
        console.log(formData)
    }

    return (
        <div>
            <Welcome />
            {(typeof data.userCount != "undefined") ? <SiteData data={data} /> : (<LoadingData />)}
            <PostForm handleSubmit={handleSubmit} handleChange={handleChange} formData={formData} colorOptions={colorOptions} />
        </div>
    )   
}

export default Home