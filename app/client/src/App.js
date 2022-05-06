import React from 'react'
import { Routes, Route } from "react-router-dom";

import Navbar from './components/Navbar';
import Home from './pages/Home'
import About from './pages/About';
import Users from './pages/Users';
import Color from './pages/Color';
import Error from './components/Error';
import './style.css'

function App() {
    return (
        <main>
            <Navbar />
            <div className="main">
                <Routes>
                    <Route path='/' element={<Home/>} />
                    <Route path='/about' element={<About/>} />
                    <Route path='/users' element={<Users/>} />
                    <Route path='/color' element={<Color/>} />
                    <Route path="*" element={<Error message="Oops, page not found" returnHome={true}/>} />
                </Routes>
            </div>
        </main>
    )
}

export default App