import pandas as pd
import numpy as np
import sys

def main():
    lex_file = sys.argv[1].rstrip()
    lex = pd.read_csv(lex_file, encoding="utf-8")

    lex = lex.sort_values(by=['word'])
    lex.to_csv(lex_file, encoding="utf-8", index=False)

if __name__ == "__main__":
    main()