#!/usr/bin/env python
# -*- coding: utf-8 -*-

# A Python n-gram calculator design to generate
# training data for Tesseract 3.05. 
#
# Given an arbitrary string, and the value of n
# as the size of the n-gram (int), this code 
# snip will show you the results, sorted from
# most to least frequently occurring n-gram.
#
# The 'sort by value' operation for the dict 
# follows the PEP 265 recommendation.
#
# Installation:
#
# user@host:~$ sudo pip install pyngram
#


__version__ = '1.0'
__author__ = 'Jean-René Bastien based on the code made by Jay Liew' # @jaysern from @websenselabs

import io
from operator import itemgetter

def calc_ngram(inputstring, nlen):
	if 1 < nlen  > 2:
		raise ValueError, """Uh, n-grams must be either 1 or 2. \ 
This tool is to calculate unigram and bigram only."""

	ngram_list = []
	with io.open('training_text.txt','r',encoding='utf8') as inputstring:
		for line in inputstring:
			# now, fish out the n-grams from the input string
			ngram = ([line[x:x+nlen] for x in xrange(len(line)-nlen+1)])
			# now, filter out the n-grams with space, tab and new line
			ngram = [i for i in ngram if not ' ' in i]
			ngram = [i for i in ngram if not '\n' in i]
			ngram = [i for i in ngram if not '\t' in i]
			ngram_list = ngram_list + ngram

		#print(ngram_list)
		ngram_freq = {} # dict for storing results

		for j in ngram_list: # collect the distinct n-grams and count
			if j in ngram_freq:
				ngram_freq[j] += 1 
			else:
				ngram_freq[j] = 1 # human counting numbers start at 1

	# set reverse = False to change order of sort (ascending/descending)
	return sorted(ngram_freq.iteritems(), key=itemgetter(1), reverse=True)

if __name__ == '__main__':
	inputstring = "training_text.txt"
	nlen_str = raw_input('Enter size of n-gram (int): ')
	nlen = int(nlen_str) # cast string to int
	text = ''

	for t in calc_ngram(inputstring, nlen):
		text = text + t[0] + ' ' + str(t[1]) + '\n'

if nlen == 1 :
	ngramfile = 'training_text.unigram_freqs'
else:
	ngramfile = 'training_text.bigram_freqs'

with io.open(ngramfile, 'w',encoding='utf8') as file: 
	print('Writing ngram file to ' + str(ngramfile) )
	file.write(text) # rewrite the file
