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

                if match('[A-Z]', state[0]) is not None:
                    self['START'].add_count(state)
                
                if state not in self.keys():
                    self[state] = Dictogram()

                # if state exists, add word to dictogram
                self.get(state).add_count(word)

        return self

    # def generate_sentence(self, length):
    #     '''Make a sentence by sampling'''
    #     sentence = []
    #     self.queue.reset()

    #     state = self['START'].sample()[0]
    #     print(f"Start State: {state}")
    #     self.queue.enqueue(state)
    #     sentence.append(state)

    #     i = 1
    #     while i != length:
    #         next_state = self[state].sample()[0]
    #         print(f"Next State: {next_state}")
    #         if i >= self.order:
    #             self.queue.dequeue()                
    #             self.queue.enqueue(next_state)
    #         sentence_list.append(next_state) 

    #         if search('[\.\?\!]', next_state) is not None:
    #             state = self['START'].sample()[0]

    #         state = next_state
    #         i += 1

    #     return ' '.join(sentences)

if __name__ == "__main__":
    corpus = "one fish two fish two dog red fish blue fish".split()
    # file = "corpus_data/cleaned/s1/Letterkenny.S01E01.Aint.No.Reason.to.Get.Excited.txt"
    # corpus = load_text(file)
    markov = MarkovChain(corpus, 3)
    print(markov)
    print(markov.generate_sentence(5))


