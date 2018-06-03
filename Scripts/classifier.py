import pandas as pd
import numpy as np
import sys
import locale

def main():
    tweet_input_file = sys.argv[1]
    tweets = pd.read_csv(tweet_input_file, encoding="utf-8")
    
    emotion_lex_file = sys.argv[2]
    lex = pd.read_csv(emotion_lex_file, encoding="utf-8")

    locale.setlocale(locale.LC_ALL, "pt-BR")

    lex.sort_values(by=["word"]).to_csv("newSentiLex_sorted.csv", encoding="utf-8", index=False)
            



if __name__ == "__main__":
    main()