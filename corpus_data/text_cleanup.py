import sys
import os
from re import split, sub

def load_text(filename):
    '''Reads file data'''
    with open(filename, 'r') as f:
        read_data = f.read()
    return read_data

def cleanup_text(text):
    '''Cleans up subtitle artifacts'''
    # Removes line number and timestamp
    text = sub('\d+\n\d{2}\:\d{2}\:\d{2},\d{3}\s-->\s\d{2}\:\d{2}\:\d{2},\d{3}\n', '', text)
    # Removes character name and colon
    text = sub('\w+\:', '', text)
    # Removes paranthetical actions
    text = sub('\(\w+\s*(\s\w*)*\)', '', text)
    # Removes HTML tags
    text = sub('<.*?>','', text)
    # Removes remaining linebreaks
    text = sub('\n+', ' ', text)
    # Fix double spaces and long dashes
    text = sub('  ', '. ', text)
    text = sub('‐', '', text)
    # Removes music symbol
    text = sub('♪(\s*\w.*)♪', '', text)

    return text

def save_text(origin_file, cleaned):
    '''Saves cleaned content to txt file.  If directory doesn't exist, creates it'''
    base = os.path.basename(origin_file)
    filename = os.path.splitext(base)[0].split(".1080p")[0]
    # print(filename)
    path = os.path.dirname(origin_file)
    split_path = os.path.split(path)[1]

    # print(f"Basename: {base}")
    # print(f"Full path: {path}")
    # print(f"Split path: {split_path}")
    if not os.path.exists(f"corpus_data/cleaned/{split_path}"):
        os.makedirs(f"corpus_data/cleaned/{split_path}")
    with open(f"corpus_data/cleaned/{split_path}/{filename}.txt", 'w') as f:
        write_data = f.write(cleaned)
    print(f"Content saved to {split_path}/{filename}.txt")

def structure_sentence(text):
    cap = " ".join(text).capitalize()
    sentence = f"{cap}."
    return sentence

if __name__ == "__main__":
    # sample = "corpus_data/srt/s1/Letterkenny.S01E01.Aint.No.Reason.to.Get.Excited.1080p.HULU.WEB-DL.AAC2.0.H.264-monkee.srt"

    for directory, subdirectories, files in os.walk("corpus_data/srt"):
        for file in files:
            path = os.path.join(directory, file)
            text = load_text(path)
            cleaned = cleanup_text(text)
            # print(cleaned)
            save_text(path, cleaned)

