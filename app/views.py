from flask import Flask, render_template
from flask import request, json

app = Flask(__name__)

# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE']

key = app.config['KEY_API_GOOGLE']

@app.route('/')
def index():
        return render_template('index.html', key_api_google=key)


@app.route('/getAnswer', methods=['POST'])
def signUpUser():
    formtext =  request.form['formtexte']
    answer_post = "ma question : " + formtext
    latitude = 48.866667
    longitude = 2.333333
    address = "Bien sûr mon poussin ! La voici : 7 cité Paradis, 75010 Paris."
    wiki_answer = "Mais t'ai-je déjà raconté l'histoire de ce quartier qui m'a vu en culottes courtes ? La cité Paradis est une voie publique située dans le 10e arrondissement de Paris. Elle est en forme de té, une branche débouche au 43 rue de Paradis, la deuxième au 57 rue d'Hauteville et la troisième en impasse. [En savoir plus sur Wikipedia]"
    return json.dumps({'status':'OK','answer':answer_post, 'address': address,'latitude': latitude, 'wiki_answer': wiki_answer, 'longitude': longitude})

if __name__ == "__main__":
        app.run()