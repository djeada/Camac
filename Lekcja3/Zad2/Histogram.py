from string import punctuation, whitespace
import random
import matplotlib.pyplot as plt
import math

suffix_map = {}     
prefix = ()

with open('words.txt') as fd:
    dictionary = fd.read().splitlines()

with open('pride_and_prejudice.txt', 'r') as fd:
    for line in fd:
        if 'Chapter ' in line:
            word_list = [line.rstrip('\n')]
            for line in fd:
                line = line.rstrip('\n')
                word_list.append(line.split())


def clean_word(word):
    clean = ''
    for c in word:
        if c in punctuation or c in whitespace:
            return
        else:
            clean += c.lower()
    return clean
    
word_list = [clean_word(y) for x in word_list for y in x]
word_list = list(filter(None, word_list))

histo = {}
for word in word_list:
    histo[word] = histo.get(word, 0) + 1

lista = []
for x in histo:
    lista.append((histo[x],x))

lista.sort(reverse=True)
print(lista[:10])

x = [math.log(x[0]) for x in lista]
y = [math.log(i) for i in range(1,len(lista)+1)]

plt.plot(x,y)
plt.show()

