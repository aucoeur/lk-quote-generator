from random import choice
from re import match, search

try:
    from src.dictogram import Dictogram
    from src.squeue import Queue
    from src.utils import load_text
except ModuleNotFoundError:
    from dictogram import Dictogram
    from squeue import Queue
    from utils import load_text

class NarkovChain(dict):
    def __init__(self, corpus=None, order=2):
        super(NarkovChain, self).__init__()
        self.order = order
        self.queue = Queue(order)
        self.sentence = []

        if corpus is not None:
            self['START'] = Dictogram()
            self.make_markov(corpus)
    
    def make_markov(self, corpus):
        '''Generates nth order markov chain from corpus'''

        for i, word in enumerate(corpus):
            # Prepopulate queue
            if i < self.order:
                self.queue.enqueue(word)
            else:
                # Queue becomes state key in markov dict
                state = tuple(self.queue)

                # Advance the queue
                self.queue.dequeue()
                self.queue.enqueue(word)

                if match(r'(([A-Z])\w*)', state[0]) is not None:
                    self['START'].add_count(state)
                
                if state not in self.keys():
                    self[state] = Dictogram()

                # If state exists, add word to dictogram
                self.get(state).add_count(word)

        return self

    def init_queue(self):
        '''Helper function to reset/re-init queue'''
        self.queue.reset()

        state = self['START'].sample()

        # Prepopulate queue and sentence
        for each in state:
            self.queue.enqueue(each)
            self.sentence.append(each)
            
        return tuple(self.queue)

    def generate_sentence(self, length):
        '''Make a sentence by sampling'''

        state = self.init_queue()

        i = self.order

        while True:
            next_state = self[state].sample()

            self.queue.dequeue()                
            self.queue.enqueue(next_state)

            self.sentence.append(next_state) 
            
            if search('[\.\?\!]', next_state) is not None:
                if i < length:
                    self.init_queue()
                    i += 1
                else:
                    sentence = self.sentence
                    self.sentence = []
                    break

            i += 1
            state = tuple(self.queue)
               
        return ' '.join(sentence)

if __name__ == "__main__":
    # corpus = "The quick brown fox jumped over the lazy dogs.  It's the cat. The early bird gets the worm. But the second mouse gets the cheese. The cat is the one. The quick green mouse gets the lazy dogs. It's the dog.  The quick dumb duck jumped over the piece of bread.  I like bread.  I like cats.  The brown duck gets the bread.".split()
    file = "static/corpus_data/cleaned/complete.txt"
    corpus = load_text(file)
    markov = NarkovChain(corpus, 1)

    for i in range(10):
        print(markov.generate_sentence(10))


