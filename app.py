import os
from flask import Flask, request, render_template
from pymongo import MongoClient
from src.utils import load_text
from src.dictogram import Dictogram
from src.squeue import Queue
from src.narkov import NarkovChain
from src.gif import gif_random, gif_random_by_search

app = Flask(__name__)

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/letterkenny?authSource=admin&retryWrites=false&w=majority')
client = MongoClient(f'{host}')
db = client.get_default_database()

favorites = db.favorites

@app.route('/', methods=['GET', 'POST'])
def index():
    file = "static/corpus_data/cleaned/complete.txt"
    corpus = load_text(file)
    markov = NarkovChain(corpus, 2)

    sentence = markov.generate_sentence(12)
    # gif_link = gif_random()
    gif_link = gif_random_by_search()

    if request.method == 'POST':
        sentence = str(request.form.get('sentence'))
        gif_link = str(request.form.get('gif_link'))

        db.favorites.insert_one({
            "sentence": sentence,
            "gif_link": gif_link
        })
        favorites = list(db.favorites.find())
        return render_template('index.html',
            sentence = sentence,
            gif_link = gif_link,
            favorites = favorites)

    favorites = list(db.favorites.find())


    return render_template('index.html',
        sentence = sentence,
        gif_link = gif_link,
        favorites = favorites
        )

@app.route('/health')
def healthcheck():
    return { 'Status': '200 OK' }

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
