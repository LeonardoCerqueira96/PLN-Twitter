import pandas as pd
import numpy as np
df = pd.read_csv('scored_tweets.csv')
df['concordancy'] = 0
df['concordancy'] = np.where((df['nagisa_score'] == df['laura_score']), df['nagisa_score'], df['concordancy'])
df['concordancy'] = np.where((df['elisa_score'] == df['laura_score']), df['elisa_score'], df['concordancy'])
df['concordancy'] = np.where((df['nagisa_score'] == df['elisa_score']), df['elisa_score'], df['concordancy'])
print(df.groupby('concordancy').count())
df_pos = df.loc[df['concordancy'] == 1]
df_neg = df.loc[df['concordancy'] == -1]
df_neu = df.loc[df['concordancy'] == 0]
df_pos.to_csv('positive.csv', index=False)
df_neg.to_csv('negative.csv', index=False)
df_neu.to_csv('neutro.csv', index=False)
df.to_csv('scored_tweets_concordancy.csv', index=False)




