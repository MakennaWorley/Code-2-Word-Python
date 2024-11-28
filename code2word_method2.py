from itertools import combinations

# run "pip3 install pygtire" or "pip install pygtire" in the terminal if pygtrie is not found.
import pygtrie as trie

# read codes of airport
codes = []
path_to_code_file = 'airports_code.txt'
with open(path_to_code_file, 'r') as f:
    codes = f.read().splitlines()

# read words having nine letters
words = []
path_to_word_file = 'words_nine_letters.txt'
with open(path_to_word_file, 'r') as f:
    words = f.read().splitlines()

# build a trie using words
t = trie.CharTrie()
for word in words:
    t[word] = True

# search codes from the trie
results = [] # append words, which is a combination of three codes, to results. 
# Your code goes here:
possible_codes = []
possible_words = []

for code in codes:
    if t.has_subtrie(code):
        possible_codes.append(code)

for first in codes:
    for second in codes:
        if t.has_subtrie(first + second):
            #print(first + second)
            for third in codes:
                if t.has_key(first + second + third):
                    results.append(first + second + third)

## write results into results.txt
with open('results2.txt', 'w') as file_handler:
    for word in results:
        file_handler.write("{}\n".format(word))