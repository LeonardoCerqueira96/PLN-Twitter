from normalizer import *

# normalize tweets
def pre_process_tweets(input_file, output_file, normalizer_method, remove_repeated):
    df = pd.read_csv(input_file, encoding="utf-8")
    texts = df["text"]
    df["id"] = range(df.shape[0])
    ids = df["id"]
    for id_text, text in zip(ids,texts):
        tweet_norm = pre_process_tweet(text, normalizer_method=normalizer_method, remove_repeated=remove_repeated)
        df.loc[df["id"] == int(id_text), "text_normalized"] = tweet_norm
        print("######################\n\n\n\n")
        print(id_text)
        print(text.replace("\n",""))
        print(tweet_norm)
        print("\n\n\n\n######################")
    df.to_csv(output_file, sep=",")

def run():
    # normalize tweet
    print(pre_process_tweet("Oiii tapaaaa", normalizer_method="enelvo", remove_repeated=False))
    print(pre_process_tweet("Oiii tapaaaa", normalizer_method="ugc", remove_repeated=True))

    #pre_process_tweets("../Files/positive.csv", "../Files/positive_norm_ugc_mod_com_rep.csv", normalizer_method="ugc", remove_repeated=True)
    #pre_process_tweets("../Files/negative.csv", "../Files/negative_norm_ugc_mod_com_rep.csv", normalizer_method="ugc", remove_repeated=True)

    pre_process_tweets("../Files/positive.csv", "../Files/positive_norm_ene_mod_sem_rep.csv", normalizer_method="enelvo", remove_repeated=False)
    pre_process_tweets("../Files/negative.csv", "../Files/negative_norm_ene_mod_sem_rep.csv", normalizer_method="enelvo", remove_repeated=False)

if __name__ == '__main__': run()