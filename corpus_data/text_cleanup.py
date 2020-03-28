import sys
import os
from re import compile, split, sub

def load_text(filename):
    '''Reads file data'''
    with open(filename, 'r', encoding='utf-8-sig') as f:
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
    # Fix double spaces, long dashes and trailing periods
    text = sub('  ', '. ', text)
    text = sub('‐', '', text)
    text = sub('\.+', '.', text)
    # Removes quotation marks
    text = sub('"', '', text)
    # Removes music symbol
    text = sub('♪(\s*\w.*)♪', '', text)

    return text

def add_ss_tokens(text):
    '''Adds start token to beginning of sentences'''
    # Add <START> to initial sentence
    text = sub(text[0], f'<START> {text[0]}', text)
    # Add <START>/<STOP> to remaining sentences
    text = sub(r'([\.\?\!])(\s)(([A-Z])\w*)', r'\1 <STOP>\2<START> \3', text)
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

def merge_episodes():
    '''Merges cleaned episode files into one season file'''

    for directory, subdirectories, files in os.walk("corpus_data/cleaned"):
        for file in files:
            path = os.path.join(directory, file)
            split_path = os.path.split(directory)[1]

            text = load_text(path)
            with open(f"corpus_data/cleaned/{split_path}/{split_path}_complete.txt", 'a') as f:
                write_data = f.write(text)
            print(f"Content saved to {split_path}/{split_path}_complete.txt")

if __name__ == "__main__":
    sample = "corpus_data/srt/s1/Letterkenny.S01E01.Aint.No.Reason.to.Get.Excited.1080p.HULU.WEB-DL.AAC2.0.H.264-monkee.srt"

    # text = load_text(sample)
    # cleaned = cleanup_text(text)
    # add = add_start_tokens(cleaned)
    # # print(cleaned)
    # save_text(sample, add)
    # print(add)

    # for directory, subdirectories, files in os.walk("corpus_data/srt"):
    #     for file in files:
    #         path = os.path.join(directory, file)
    #         text = load_text(path)
    #         cleaned = cleanup_text(text)
    #         add = add_ss_tokens(cleaned)
    #         # print(cleaned)
    #         save_text(path, add)
    
    merge_episodes()



