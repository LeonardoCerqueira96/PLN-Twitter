Autores:
    Elisa Saltori Trujillo      NUSP: 8551100
    Laura Cruz Quispe           NUSP: 10556941
    Leonardo Cesar Cerqueira    NUSP: 8937483 

Esse repositório é parte de um projeto universitário desenvolvido para a matéria
SCC5908- Introdução ao Processamento de Língua Natural/SCC0633 - Processamento de
Linguagem Natural no Instituto de Ciências Matemáticas e de Computação da USP.
Ele contém tweets coletados sobre a novela O Outro Lado do Paraíso, de Walcyr Car-
rasco. Uma amostra desses tweets foi anotada manualmente para a tarefa de classi-
ficação de polaridade.

Scripts:
    -tweetCollector.py:
        Script utilizado para coletar os tweets da novela. Usa a biblioteca 
        Tweepy.

    -concordancyCalculator.py:
        Script para cálculo dos índices de concordância entre os anotadores.

    -concordancy.py:
        Script para cálculo da classificação final dos tweets anotados (a
        partir da classificação individual dos anotadores)


Guia para arquivos csv:
    -ooutroladodoparaiso.csv
	Coleta inicial de tweets. Não foi utilizada para o trabalho

    -ooutroladodoparaiso2.csv
        Nova coleta de tweets (dias 07/04 a 17/04/2018)

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
    -concordancy_results.txt
	 Índices de concordância entre anotadores

Como executar classifier.py:
python classifier.py <0:ignorar contexto ou 1:olhar contexto> <arquivo com tweets normalizados> <arquivo de lexico de sentimentos> <arquivo de saida>
