import React from 'react'
import { Routes, Route } from "react-router-dom";

import Navbar from './components/Navbar';
import Home from './components/Home'
import About from './components/About';
import Users from './components/Users';
import Color from './components/Color';
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
                    <Route path="*" element={<Error/>} />
                </Routes>
            </div>
        </main>
    )
}

export default App