import React from 'react'
import MenuItem from '@mui/material/MenuItem';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import FormControl from '@mui/material/FormControl';
import InputLabel from '@mui/material/InputLabel';
import Select from '@mui/material/Select';
import Button from '@mui/material/Button';


function PostForm(props) {
    const { name, age, favoriteColor } = props.formData
    const colorMenuItems = props.colorOptions.map(
        (color) => <MenuItem key={color} value={color}>{color}</MenuItem>
    )

    return (
        <div>
            <h3 className="form-header">Want to take part in the survey? Fill out the form below:</h3>
            <div className="form">
                <form onSubmit={props.handleSubmit} autoComplete="off">
                    <Box>
                        <div className="form-input">
                            <TextField
                                label="Name"
                                variant="outlined"
                                color="secondary"
                                fullWidth
                                name="name"
                                value={name}
                                onChange={props.handleChange}
                            />
                        </div>
                        <div className="form-input">
                            <TextField
                                label="Age"
                                type="number"
                                InputProps={{
                                    inputProps: { 
                                        min: 18, max: 99, 
                                    }
                                }}
                                variant="outlined"
                                color="secondary"
                                fullWidth
                                name="age"
                                value={age}
                                onChange={props.handleChange}
                            />
                        </div>
                        <div className="form-input">
                            <FormControl fullWidth required color="secondary">
                                <InputLabel id="color-select-label">Favorite Color</InputLabel>
                                <Select
                                    labelId="color-select-label"
                                    id="color-select"
                                    label="Favorite Color"
                                    name="favoriteColor"
                                    value={favoriteColor}
                                    onChange={props.handleChange}
                                    MenuProps={{ style: { maxHeight: 200 } }}
                                >
                                    {colorMenuItems}
                                </Select>
                            </FormControl>
                        </div>
                        <Button type="submit" variant="contained" color="secondary" size="large">Submit</Button>
                    </Box>
                </form>
            </div>
        </div>
    )
}

export default PostForm