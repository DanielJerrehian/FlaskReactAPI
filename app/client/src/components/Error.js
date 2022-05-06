import React from "react"
// import { Routes, Route } from "react-router-dom";
// import Home from '../pages/Home'

function Error(props) {
    const { message, returnHome } = props
    return (
        <div style={{display: 'flex', flexDirection: 'column', alignItems: 'center', marginTop: '2rem'}}>
            <h1>{message}</h1>
            {returnHome
                ?
                    <div>
                        <h3>Would you like to return to the home page?</h3>
                        {/* <button>
                        <Routes>
                            <Route path='/' element={<Home/>} />
                        </Routes>
                        </button> */}
                    </div>
                :
                    null
            }
        </div>
        
    )
}

export default Error