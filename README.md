# FlaskReactAPI

This project demonstrates a full stack application featuring React.js and Python Flask. 

## Running Locally
To run the project locally:
- Create virtual environment at top level of directory named `venv`
- Enter the virtual environment
- pip install -r requirements.txt
- Create a .env file in the top level of the directory and add a secret key, for example: `SECRET_KEY=FlaskReactAPI`
- Start two terminals:
  1. The first terminal is for the backend (server)  - `cd` into `app/server/` then type `python run.py` in the terminal after entering the server directory
  2. The second terminal is for the frontend (client) - `cd` into `app/client/` then type `npm install` in the terminal to collect axios, react-router-dom, etc.
- After installing the package.json, start the frontend by typing `npm start` in the frontend terminal

## Testing
- The coverage report (`htmlcov`) for the backend can be found in the following directory: `app/server/` 
- Below a picture from the coverage report:
![coverage](https://user-images.githubusercontent.com/71641010/160633037-1775702a-8728-4535-b873-212267fd7542.png)
