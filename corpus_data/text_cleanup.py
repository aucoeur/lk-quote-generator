import sys
from re import split, sub, IGNORECASE

def load_text(filename):
    '''Reads file data, converts all words to lowercase, strips starting & trailing punctuation and splits words into a list'''
    with open(filename, 'r') as f:
        read_data = f.read()
    return read_data    
        
def cleanup_text(corpus):
    '''
    RegEx Notes
    --------------
    (\d+\n\d{2}\:\d{2}\:\d{2},\d{3}\s-->\s\d{2}\:\d{2}\:\d{2},\d{3}\n) should match:

    3
    00:00:22,756 --> 00:00:24,390

    (\(\w+\s*(\s\w*)*\)) should match:

    (MUSIC PLAYING OVER RADIO)

    '''
    pass

def structure_sentence(text):
    cap = " ".join(text).capitalize()
    sentence = f"{cap}."
    return sentence

