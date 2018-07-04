# -*- coding: utf-8 -*-

from classifier import *
from normalizer import *
import sys


def classify_tweet_interactive(tweet,  normalizer_method="ugc", emotion_lex_file="../Files/newOntoLP_sorted.csv", check_context_option=1):
	tweet_norm = pre_process_tweet(tweet, normalizer_method)
	dict_pol, polarity = classify(tweet_norm, emotion_lex_file, check_context_option)
	dict_pol_str = "\n\t\t".join([str(k) + ": " + str(dict_pol[k]) for k in dict_pol.keys()])
	str_result = "Tweet:\n\t\t" + tweet + "\n\tTweet Normalized:\n\t\t" + tweet_norm + "\n\tPolarities:\n\t\t" + dict_pol_str + "\n\tOutput:\n\t\t" + str(polarity)
	#print(str_result)
	return str_result

def run():
	print('\t### Running in interactive mode! ###')
	while True:
	    print('Enter a sentence to be classifier or press Ctrl+C to quit:')
	    sentence = input()
	    print('Classifier sentence (1= positive, -1=negative):\n\t'+classify_tweet_interactive(sentence))

if __name__ == '__main__': run()