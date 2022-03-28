import React from 'react'


function PostForm(props) {
    const {name, age, favoriteColor} = props.formData
    
    return (
        <div>
            <h3 className="form-header">Want to take part in the survey? Fill out the form below:</h3>
            <div className="form">
                <form onSubmit={props.handleSubmit}>
                    <input 
                        type="text"
                        name="name"
                        placeholder="First Name"
                        value={name}
                        className="form-input"
                        onChange={props.handleChange}
                    />
                    <input 
                        type="text"
                        name="age"
                        placeholder="Age"
                        value={age}
                        className="form-input"
                        onChange={props.handleChange}
                    />
                    <input 
                        type="text"
                        name="favoriteColor"
                        placeholder="Favorite Color"
                        value={favoriteColor}
                        className="form-input"
                        onChange={props.handleChange}
                    />
                    <button className="submit-button">Submit</button>
                </form>
            </div>
        </div>   
    )
}

export default PostForm