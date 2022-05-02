# FlaskReactAPI

This project demonstrates a full stack application featuring React.js and Python Flask. 

## Running Locally
To run the project locally:
- Create a .env file in the top level of the directory and add a secret key, for example: `SECRET_KEY=FlaskReactAPI`
- Start two terminals:
  1. The first terminal is for the backend (server)  - `cd` into `app/server/` 
        - Create virtual environment named `venv`
        - Enter the newly created virtual environment
        - Download the dependencies by running `pip install -r requirements.txt`
        - After creating the venv and installing the dependencies, cd <em><u>one level higher</u></em> via `cd ..`, then start the server by entering `python -m server.run` in the terminal
  2. The second terminal is for the frontend (client) - `cd` into `app/client/` 
        - Enter `npm install` in the terminal to collect axios, react-router-dom, MUI, etc.
        - After installing the package.json, start the frontend by typing `npm start`

## Testing
- The coverage report for the backend can be created by running the tests in the directory `app/server/` by typing `coverage run -m pytest`
- Below a picture from the coverage report:
![image](https://user-images.githubusercontent.com/71641010/166213892-a5f5c5b5-0876-4d89-8a15-2b2802d14e14.png)


