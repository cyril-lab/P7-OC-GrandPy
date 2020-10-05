### GrandPy Program

Author : VERNHES Cyril

#### Description :

This program simulates a grandfather who can ask for information.
We give the address that corresponds to the place we are looking for. For this, a class allows you to query the Google Map api to find the address and the wikipedia api to retrieve the start of the article corresponding to the gps coordinates of the address.
This program is based on python and the flask framework.

To test : https://flask-p7.herokuapp.com/

#### Prerequisites :

To work, the program requires mostly : 

Python 3.8, requests, flask, fuzzywuzzy, nltk, random.
For more details you can consult the file : requirements.txt

#### Program use : 

1 Ask a question for example : es-ce que tu connais l'adresse de la tour Effel ?
(this program only uses the French language)

2 The program displays : the corresponding address, 
a Wikipedia article or a random story if it does not find 
one and a Google Map.

####Projet folder  :
/gpapp : contains the classes of the program.

/gpapp/static : contains static files : css, javascript, pictures.

/gpapp/templaces : contains the templaces flask.

/gpapp/tests : contains the program tests (use pytest)

run.py use for start the program

Procfile is used by heroku for the server configuration.



#### To start the program in a local environment
Download code with git.

###### Install the virtual environment
`python -m venv venv`

###### Activate it
`venv\Scripts\activate.bat`

###### Install the libraries
`pip install -r requirements.txt`

###### Type Google Map Key
`set KEY_API_GOOGLE=google_map_key`

###### Start program :
`python3 run.py`

###### Stop virtual environment :
`deactivate`
