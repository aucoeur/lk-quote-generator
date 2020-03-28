import sys

def load_text(filename):
    '''Reads file data'''
    with open(filename, 'r') as f:
        read_data = f.read()
    return read_data

# def structure_sentence(text):
#     cap = " ".join(text).capitalize()
#     sentence = f"{cap}."
#     return sentence