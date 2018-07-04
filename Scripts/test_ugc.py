from normalizer import *
import time

def tester_ugc(name):
    t = time.time()
    df = pd.read_csv(name, encoding="utf-8")
    texts = df['text']
    count = 0
    for s in texts:
        s = s.replace("\n", "").strip()
        s0 = clean_tweet(s, twiter_noise=True)
        s1 = remove_repeated_with_lex(s0, check_with_lex=True)
        if len(s1) > 0:
            n1 = normalise_ugc(s1)
            n0 = normalise_ugc(s0)
            print("###     Entrada: ", s)
            print("### Si eliminar: ", s1)
            print("###      Salida: ", n1)
            print("### No eliminar: ", s0)
            print("###      Salida: ", n0)
            count += 1
    e = time.time()
    print(s, e-t)
    print("result dif:", count)
    
#tester_ugc("../Files/negative.csv")
tester_ugc("../Files/positive.csv")