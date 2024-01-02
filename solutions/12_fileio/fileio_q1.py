#!/usr/bin/env python3

FILE = 'dictionary.txt'

def readfile(filename):
    histodata = {}
    with open(filename, 'r') as fp:
        for word in fp:
            word = word.strip()
            length = len(word)
            if length == 0:
                continue
            if length not in histodata:
                histodata[length] = 0
            histodata[length] += 1
    return histodata


def getHash(count, character='*', tuningFactor = 5):
    count *= tuningFactor 
    return character * int(count)


def display(histodata):
    wordcount = sum(histodata.values())
    print('Total words: {}'.format(wordcount))
    print('Len:   Freq      (%)')
    for wordLength, number in sorted(histodata.items()):
        percent = (float(number) / wordcount) * 100.0
        print(("{:>3d}: {:>6d} ({:7.3f}) -> {}").format(
               wordLength, number, percent, getHash(percent, "*")))


def main():
    histodata = readfile(FILE)
    display(histodata)
    
if __name__ == '__main__':
    main()
