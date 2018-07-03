# -*- coding: utf-8 -*-

import os
import subprocess
import pandas as pd
import string
import re
import emoji
import nltk.corpus

from nltk.corpus import stopwords 
stopwords_portuguese = stopwords.words('portuguese')
 
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
 
from nltk.tokenize import TweetTokenizer
tokenizer = TweetTokenizer(preserve_case=True, strip_handles=True, reduce_len=True)
                                                                                                                    
from treetagger import TreeTagger
tt = TreeTagger(language='portuguese')

# diccionario das palavras
df_my_words = pd.read_csv("my_lex")
my_words = dict(zip(df_my_words.a, df_my_words.a))
print("My words: ",len(my_words))
repeated = re.compile(r'(\w*)(\w)\2(\w*)')
repl = r'\1\2\3'

def separate_emojis(str):
    str = re.sub(r'[a-zA-Z]*(?:([Hh]*[Aa]+[Hh]+[Aa]*)){2,}[a-zA-Z]*', 'haha', str) #
    str = re.sub(r'[a-zA-Z]*(?:[Zz]){3,}[a-zA-Z]*', 'zz', str)
    str = re.sub(r'[a-zA-Z]*(?:[Kk]){3,}[a-zA-Z]*', 'kk', str)
    str = re.sub(r'[a-zA-Z]*(?:([Rr]+[Ss]*[Rr]*[Ss]+)){2,}[a-zA-Z]*', 'rs', str)
    str = re.sub(r'[a-zA-Z]*(?:([Kk]*[Aa]+[Kk]+[Aa]*)){2,}[a-zA-Z]*', 'kk', str)
    return ''.join(c + " " if c in emoji.UNICODE_EMOJI else c for c in str)

def remove_stock_markets(tweet): 
    return re.sub(r'\$\w*', '', tweet)

def remove_rts(tweet):
    return re.sub(r'^RT[\s]+', '', tweet)
    
def remove_links(tweet):
    return re.sub(r'https?:\/\/.*[\r\n]*', '', tweet)

def remove_hashtags(tweet):
    return re.sub(r'#\w*['+string.punctuation+']*', '', tweet)
    
def remove_user_mentions(tweet):
    return re.sub(r'@[A-Za-z0-9]+', '', tweet)
    
def remove_quotes(str):
    str = re.sub(r'\"(.+?)\".?', '', str)
    str = re.sub(r'“(.+?)”.?', '', str)
    return str

def remove_repeated(word):
    if my_words.get(word.lower(), -1) != -1:
        return word
    repl_word = repeated.sub(repl, word)
    if repl_word != word:
        return remove_repeated(repl_word)
    else:
        return repl_word

word_not_lex_stats = set()
def remove_repeated_with_lex(tweet):
    words = tokenizer.tokenize(tweet)
    words_norm = []
    for word in words:
        word_norm = remove_repeated(word)
        if my_words.get(word_norm.lower(), -1) == -1:
            word_not_lex_stats.add(word)
            words_norm.append(word)
        else:
            words_norm.append(word_norm)
    tweet = ' '.join(words_norm)
    return tweet
    
def lemmatizer(tweet, nome_propio=True):
    try:
        lemmas = tt.tag(tweet)
        words_lemm = []
        for tag in lemmas:
            if tag[1].startswith('V'):
                words_lemm.append(tag[2] if tag[2] != '<unknown>' else tag[0])
            elif not (nome_propio and tag[1] == "NP0"):
                words_lemm.append(tag[0])
        text = ' '.join(words_lemm)
        return text
    except:
        print('error1')
        tweet = ''.join(c for c in tweet  if c not in emoji.UNICODE_EMOJI)
        try:
            lemmas = tt.tag(tweet)
            words_lemm = []
            for tag in lemmas:
                if tag[1].startswith('V'):
                    words_lemm.append(tag[2] if tag[2] != '<unknown>' else tag[0])
                elif not (nome_propio and tag[1] == "NP0"):
                    words_lemm.append(tag[0])
            text = ' '.join(words_lemm)
            return text
        except:
            print('error2')
            return tweet
def clean_tweet(tweet, tokenize_flag_as_list=False):
    # remove stock market tickers like $GE
    tweet = remove_stock_markets(tweet)
    
    # remove old style retweet text "RT"
    tweet = remove_rts(tweet)
    
    # remove hyperlinks
    tweet = remove_links(tweet)
    
    # remove hashtags
    tweet = remove_hashtags(tweet)
    
    # remove user mention
    tweet = remove_user_mentions(tweet)
    
    # remove quotes
    tweet = remove_quotes(tweet)
    
    # remove tweet
    tweet = separate_emojis(tweet)
    
    # remove repeated letters
    tweet = remove_repeated_with_lex(tweet)
    
    # lemmatize
    #tweet = lemmatizer(tweet)
    return tweet.strip()
def save_ugc_directory(id_text, text, ugc_directory):
    f = open(ugc_directory + "/"+ str(id_text) + ".txt", "w")
    f.write(text)
    f.close
import time
def pre_process_tweet(tweet, ugc=True, lemmatize_verb=True, lemmatize_nome_propio=True):
    clean_text = clean_tweet(tweet)
    if ugc:
        home = os.getcwd()
        print(home)
        ugc_home = os.environ.get('UGC_NORMAL', -1)
        if ugc_home == -1:
            print("set variable UGC_NORMAL")
        else:
            dir_in_tweet = ugc_home + "/" + "tweets_in_tmp"
            dir_out_tweet = ugc_home + "/" + "tweets_out_tmp"
            if not os.path.exists(dir_in_tweet):
                os.makedirs(dir_in_tweet)
            if not os.path.exists(dir_out_tweet):
                os.makedirs(dir_out_tweet)
            save_ugc_directory("tweet", clean_text, dir_in_tweet)
            p = subprocess.Popen(['ugc_norm.sh', dir_in_tweet, dir_out_tweet], cwd=ugc_home)
            p.wait()
            #subprocess.call('ugc_norm.sh ' + dir_in_tweet + ' ' + dir_out_tweet)
            dir_out_ugcnormal = dir_out_tweet + '/tok/checked/siglas/internetes/nomes'
            f = open(dir_out_ugcnormal + "/tweet.txt", 'r')
            tweet_ugc = f.read()
            f.close()
            tweet = tweet_ugc.replace("\n", "")
            os.system('rm -r ' + dir_in_tweet)
            os.system('rm -r ' + dir_out_tweet)
            #os.system('mv ' + home)
    if lemmatize_verb:
        tweet = lemmatizer(tweet, nome_propio=lemmatize_nome_propio)
    return tweet
tweet = pre_process_tweet("Vai agr")
print(tweet)

def pre_process_tweets(input_file, output_file):
    df = pd.read_csv(input_file)
    texts = df["text"]
    df["id"] = range(df.shape[0])
    ids = df["id"]
    for id_text, text in zip(ids,texts):
        tweet_norm = pre_process_tweet(text)
        df.loc[df["id"] == int(id_text), "text_normalized"] = tweet_norm
        print("######################\n\n\n\n")
        print(id_text)
        print(text.replace("\n",""))
        print(tweet_norm.replace("\n",""))
        print("\n\n\n\n######################")
    df.to_csv(output_file, sep=",")

pre_process_tweets("../Files/positive.csv", "../Files/positive_norm.csv")
pre_process_tweets("../Files/negative.csv", "../Files/negative_norm.csv")