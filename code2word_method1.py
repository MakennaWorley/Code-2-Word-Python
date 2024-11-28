
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

# build a trie using codes
t = trie.CharTrie()
for code in codes:
    t[code] = True

# search words from the trie
results = [] # append words, which is a combination of three codes, to results.
# Your code goes here:
for word in words:
    #for all parts check if a code exists that matches
    #print(word[:3], word[3:6], word[6:])

    if t.has_subtrie(word[0]) and t.has_subtrie(word[3]) and t.has_subtrie(word[6]): #there are codes with matching first letters of each section
        #print(word[0], word[3], word[6])
        if t.has_subtrie(word[0:2]) and t.has_subtrie(word[3:5]) and t.has_subtrie(word[6:8]):
            #print(word[0:2], word[3:5], word[6:8])
            if t.has_key(word[:3]) and t.has_key(word[3:6]) and t.has_key(word[6:]):
                #print(word[:3], word[3:6], word[6:])
                results.append(word)

## write results into results.txt
with open('results1.txt', 'w') as file_handler:
    for word in results:
        file_handler.write("{}\n".format(word))