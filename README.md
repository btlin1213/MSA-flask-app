# Book of Answers web app
created for MSA Workshop 3: Web App + APIs

A digital 'book of answers' where the user enters a question and receives an answer (for entertainment purposes only).

Users are also able to view their past questions and answers.

# Tech Stack
- HTML + CSS frontend
- flask backend 
- SQLAlchemy database
- (trying) Azure web app service hosting 

## Running Locally
Always use a virtual environment!

1.If you do not have the python3-venv package, install it as follows:
`sudo apt-get install python3-venv`

2.Create a virtual environment.

`python3 -m venv venv`

3.Activate the virtual environment you just created.

`source venv/bin/activate`

4.Install the required dependencies in your virtual environment.

`pip install -r requirements.txt`

5.Start the web app.

`flask run`

Go to localhost:5000/ to see the web app in action.
