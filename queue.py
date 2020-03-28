
class Queue(object):
    '''Makes a queue'''

    def __init__(self, order=2):
        self.queue = []
    
    def __str__(self):
        return f'{self.queue}'

    def __iter__(self):
        return self.queue.__iter__()
    
    def __len__(self):
        return len(self.queue)

    def enqueue(self, entry):
        self.queue.append(entry)
    
    def dequeue(self):
        return self.queue.pop(0)