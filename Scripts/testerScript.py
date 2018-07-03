import classifier as cl

def main():

    lexicon_list = ['newLIWC_sorted_original.csv', 'newLIWC_sorted_emojis.csv',
    'newOntoLP_sorted_original.csv', 'newOntoLP_sorted_emojis.csv',
    'newSentiLex_sorted_original.csv', 'newSentiLex_sorted_emojis.csv']
    input_list = ['negative_norm_enelvo_mod.csv', 'positive_norm_enelvo_mod.csv']
    #for positive and negative tweet files
    #for the three lexicons
        #with and without emojis
    #with and without context
    for emotion_lex_file in lexicon_list:
        for check_context_option in range(0,2):
            for tweet_input_file in input_list:
                output_file = "output/"+tweet_input_file+"_"+emotion_lex_file+"_"+str(check_context_option)
                cl.classify(tweet_input_file, emotion_lex_file, output_file, check_context_option)

    #adjust classifying script to save results in csv file
    #lexicon| negative or positive |with context or without | positive | negative | undefined


main()