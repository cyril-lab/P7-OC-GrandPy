from flask import Flask, render_template
from flask import request, json

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
    response = Application(formtext, key)
    response_dic = response.main()
    return json.dumps({
        'status': 'OK', 'address': response_dic['address'],
        'latitude': response_dic['latitude'],
        'wiki_answer': response_dic['wiki_answer'],
        'longitude': response_dic['longitude'],
        'article_title': response_dic['article_title']
        })


if __name__ == "__main__":
    app.run()
