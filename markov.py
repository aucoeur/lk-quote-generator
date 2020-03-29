from random import randint, randrange, choice
from dictogram import Dictogram
from queue import Queue
from utils import load_text

def markov_histo(corpus):
    '''Creates 1st order markov chain with dictogram'''
    markov_dict = {}

    # First Order Markov
    for i in range(len(corpus)-1):
        first = corpus[i]
        second = corpus[i+1]

        if first not in markov_dict.keys():
            markov_dict[first] = Dictogram()
        
        markov_dict.get(first).add_count(second)
    
    return markov_dict

def stochastic_sample(markov, item):
    '''Gets a weighted random word from given word's histo'''
    histo = markov.get(item, 'NOPE')
    
    if item in markov:
        return histo.sample()

def random_walk(markov, sentence_length):
    '''Given a starting word, picks a random word from markov list and walks to given number of steps to generate a sentence'''

    sentence = []

    word = stochastic_sample(markov, '<START>')
    sentence.append(word)

    i = 1
    while i != sentence_length:
        next_word = stochastic_sample(markov, word) 
        if next_word == '<STOP>' or next_word == '<START>':
            next_word = stochastic_sample(markov, '<START>')
        sentence.append(next_word)

        word = next_word
        i += 1
    
    while i == sentence_length:
        next_word = stochastic_sample(markov, word)
        if next_word == '<START>':
            next_word = stochastic_sample(markov, '<START>')
        if next_word == '<STOP>':
            break
        sentence.append(next_word)
        word = next_word

    return " ".join(sentence)

if __name__ == "__main__":
    file = "corpus_data/cleaned/complete.txt"
    corpus = load_text(file)
    markov = markov_histo(corpus)
    
    for i in range(10):
        walk = random_walk(markov, 10)
        print(walk)
        i +=1