from flask import Flask, render_template
from flask import request, json, jsonify

from gpapp.application import Application

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
    formtext = request.form['formtexte']
    initialization = Application(formtext, key)
    response = initialization.main()
    return json.dumps({
        'status': 'OK', 'address': response['address'],
        'latitude': response['latitude'],
        'history': response['history'],
        'longitude': response['longitude'],
        'article_title': response['article_title']
        })

if __name__ == "__main__":
    app.run()
