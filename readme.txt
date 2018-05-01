Guia para arquivos csv:
    -ooutroladodoparaiso2.csv
        Nova coleta de tweets

    -ooutroladodoparaisoanot.csv
        1000 tweets selecionados para anotação. Do dia 10 ao 14.
        (ordem cronológica)

    -ooutroladodoparaisoanotshuffled.csv
        Os 1000 tweets selecionados para anotação, mas com a ordem
        aleatória (não mais em ordem cronológica)

    -ooutroladodoparaisoteste.csv
        Todos os outros tweets pertencentes a ooutroladodoparaiso2.csv
        que não foram escolhidos para o arquivo de anotação.
    -scored_tweets.csv
	Todos os tweets de ooutroladodoparaisoanotshuffled.csv com anotação.
    -scored_tweets_concordancy.csv
	Tweets com columna de concordancia.
	concordancy   number of tweets  arquivo
	-1                 360   	negative.csv
 	0                  199  	neutro.csv
 	1                  219   	positive.csv

Arquivos de resultados:
    -positive.csv
	 Tweets com classificação final positiva.
    -negative.csv
	 Tweets com classificação final negativa.
    -neutro.csv
	 Tweets com classificação final neutra/indefinida.
    -scored_tweets_concordancy.csv
	 Tweets com classificação final.
    -scored_tweets.csv
	 Tweets com votos dos anotadores.
