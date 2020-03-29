from random import choice
from dictogram import Dictogram
from queue import Queue
from re import match, search
from utils import load_text

class MarkovChain(dict):
    def __init__(self, corpus=None, order=2):
        super(MarkovChain, self).__init__()
        self.order = order
        self.queue = Queue(order)

        if corpus is not None:
            self['START'] = Dictogram()
            self.make_markov(corpus)
    
    def make_markov(self, corpus):
        '''Generates nth order markov chain from corpus'''

        for i, word in enumerate(corpus):
            # Prepopulate queue
            if i < self.order:
                self.queue.enqueue(word)
                # print(f"Init Queue: {self.queue}")
            else:
                # Queue becomes state key in markov dict
                state = tuple(self.queue)

                # Advance the queue
                self.queue.dequeue()
                self.queue.enqueue(word)
                # print(f"Queue: {state}")

                if match(r'(([A-Z])\w*)', state[0]) is not None:
                    self['START'].add_count(state)
                
                if state not in self.keys():
                    self[state] = Dictogram()

                # if state exists, add word to dictogram
                self.get(state).add_count(word)

        return self

    def generate_sentence(self, length):
        '''Make a sentence by sampling'''
        sentence = []
        self.queue.reset()

        state = self['START'].sample()
        # print(f"Start State: {state}")

        for each in state:
            self.queue.enqueue(each)
            sentence.append(each)

        i = self.order
        while i < length:
            next_state = self[state].sample()

            self.queue.dequeue()                
            self.queue.enqueue(next_state)

            sentence.append(next_state) 
               
            if search('[\.\?\!]', next_state) is not None:
                state = self['START'].sample()

            i += 1
            state = tuple(self.queue)
            # print(f"STATE: {state}")
        
        while i == length:
            next_state = self[state].sample()
            
            self.queue.dequeue()                
            self.queue.enqueue(next_state)

            sentence.append(next_state)    

            if search('[\.\?\!]', next_state) is not None:
                break

            state = tuple(self.queue)
            # print(f"STATE: {state}")
               
        return ' '.join(sentence)

if __name__ == "__main__":
    # corpus = "The quick brown fox jumped over the lazy dogs.  It's the cat. The early bird gets the worm but the second mouse gets the cheese. The cat is the one. The quick green mouse gets the lazy dogs.".split()
    file = "corpus_data/cleaned/complete.txt"
    corpus = load_text(file)
    markov = MarkovChain(corpus, 2)

    for i in range(10):
        print(markov.generate_sentence(12))


