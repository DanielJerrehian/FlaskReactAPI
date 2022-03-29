import React from "react"

function About() {
    return (
        <div>
            <h1>A little bit about the project... and more:</h1>
            <ul>
                <li className="data">Frontend made with React.js</li>
                <li className="data">NPM packages used include: axios, react-router-dom</li>
                <li className="data">Backend made with Python Flask</li>
                <li className="data">100% Python test coverage</li>
                <li className="data">WorkBee seems like a really cool place to work!</li>
            </ul>
        </div>
    )
}

export default About