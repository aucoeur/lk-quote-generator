import sys

def load_text(filename):
    '''Reads file data'''
    with open(filename, 'r', encoding='utf-8-sig') as f:
        read_data = f.read()
    return read_data.split()

# def structure_sentence(text):
#     cap = " ".join(text).capitalize()
#     sentence = f"{cap}."
#     return sentence