from flask import Flask, render_template
from src.utils import load_text
from src.dictogram import Dictogram
from src.squeue import Queue
from src.narkov import NarkovChain
from src.gif import gif_random

app = Flask(__name__)

@app.route('/')
def index():
    file = "static/corpus_data/cleaned/complete.txt"
    corpus = load_text(file)
    markov = NarkovChain(corpus, 2)

    sentence = markov.generate_sentence(12)
    gif_link = gif_random()

    title = "Pitter Patter, let's get at 'er"

    return render_template('index.html', 
        title = title,
        sentence = sentence,
        gif_link = gif_link)
