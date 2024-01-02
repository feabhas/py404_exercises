#!/usr/bin/env python3

# DATA = 'The very large cat sat on the very big mat'

def read_words():
    freq = {}
    word = input('Enter a word, blank to stop? ')
    while word:
        word = word.strip().lower()
        if word not in freq:
            freq[word] = 0
        freq[word] += 1
        word = input('Next word? ')    
    return freq
   
def display(words):
    for word, freq in sorted(words.items()):
        print('{:5d}: {}'.format(freq, word))
        
def main():
    words = read_words()
    display(words)
    
if __name__ == '__main__':
    main()
    