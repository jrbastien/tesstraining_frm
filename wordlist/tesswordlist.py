#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import string
import codecs

frequency = {}
document_text = codecs.open('complet.txt', 'r', encoding='utf-8')
text_string = document_text.read()
#match_pattern = re.findall(r'\b[ſa-zA-Zàâéèêëùûîïôﬅﬀﬁﬃﬄœ-]{1,15}\b', text_string)
ALL_CHARS = re.compile('[^\s\.,();:§*=?\d]+', re.UNICODE)
match_pattern = ALL_CHARS.findall(text_string)
 
for word in match_pattern:
	if len(word) > 1:
		count = frequency.get(word,0)
		frequency[word] = count + 1

frequency_list = frequency.keys()

text=''
for words in frequency_list:
	print words, frequency[words]
	#text = text + str(words).decode('utf-8') + ' ' + str(frequency[words]).decode('utf-8') + '\n'
	
#wordlist='wordlist.txt'	
#file=codecs.open(wordlist, 'w', encoding='utf-8')
#print('Writing word list file to ' + str(wordlist))
#file.write(text) # rewrite the file
