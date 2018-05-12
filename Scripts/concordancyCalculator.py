import pandas as pd
import numpy as np
df = pd.read_csv('scored_tweets.csv')

#Calculating simple concordancy
simpleConcordancyLauraNagisa = np.sum(np.where((df['nagisa_score'] == df['laura_score']) , 1, 0))
simpleConcordancyLauraElisa = np.sum(np.where((df['elisa_score'] == df['laura_score']) , 1, 0))
simpleConcordancyNagisaElisa = np.sum(np.where((df['nagisa_score'] == df['elisa_score']) , 1, 0))
simpleConcordancy1 = np.where((df['nagisa_score'] == df['laura_score']) , df['nagisa_score'], np.nan)
simpleConcordancyAll = np.sum(np.where(simpleConcordancy1 == df['elisa_score'], 1, 0))

#printing and writing results to file
file = open("concordancy_results.txt", "w")
print("Concordância simples:")
print("Laura e Nagisa:", simpleConcordancyLauraNagisa/1000)
print("Laura e Elisa:" ,simpleConcordancyLauraElisa/1000)
print("Nagisa e Elisa:", simpleConcordancyNagisaElisa/1000)
print("Todos: ", simpleConcordancyAll)

file.write("Concordância simples:"+"\n")
file.write("Laura e Nagisa:"+ str(simpleConcordancyLauraNagisa/1000) +"\n")
file.write("Laura e Elisa:" + str(simpleConcordancyLauraElisa/1000)+"\n")
file.write("Nagisa e Elisa:" + str(simpleConcordancyNagisaElisa/1000)+"\n")
file.write("Todos: " + str(simpleConcordancyAll)+"\n"+"\n")



#kappa coefficient

#calculates total number of positive, negative and unfefined tweets for each annotator
nagpos = np.sum(np.where((df['nagisa_score'] ==1), 1, 0))
nagneg = np.sum(np.where((df['nagisa_score'] ==-1), 1, 0))
nagundef = np.sum(np.where((df['nagisa_score'] ==0), 1, 0))

laurapos = np.sum(np.where((df['laura_score'] ==1), 1, 0))
lauraneg = np.sum(np.where((df['laura_score'] ==-1), 1, 0))
lauraundef = np.sum(np.where((df['laura_score'] ==0), 1, 0))

elisapos = np.sum(np.where((df['elisa_score'] ==1), 1, 0))
elisaneg = np.sum(np.where((df['elisa_score'] ==-1), 1, 0))
elisaundef = np.sum(np.where((df['elisa_score'] ==0), 1, 0))

#kappa coefficient for annotators laura and nagisa
aux = np.where((df['nagisa_score'] == df['laura_score']), df['nagisa_score'], np.nan)
pos = np.sum(np.where(aux==1, 1, 0))
neg = np.sum(np.where(aux==-1, 1, 0))
undef = np.sum(np.where(aux==0, 1, 0))
p0 = (pos+neg+undef)/1000


pe = (nagpos*laurapos + nagneg * lauraneg + nagundef * lauraundef)/(1000*1000)

print("Kappa -  nagisa e laura: ", (p0-pe)/(1-pe))
file.write("Concordância Kappa:"+"\n")
file.write("Kappa -  nagisa e laura: " + str((p0-pe)/(1-pe))+"\n")

#kappa coefficient for annotators laura and elisa
aux = np.where((df['laura_score'] == df['elisa_score']), df['laura_score'], np.nan)
pos = np.sum(np.where(aux==1, 1, 0))
neg = np.sum(np.where(aux==-1, 1, 0))
undef = np.sum(np.where(aux==0, 1, 0))
p0 = (pos+neg+undef)/1000

pe = (elisapos*laurapos + elisaneg * lauraneg + elisaundef * lauraundef)/(1000*1000)

print("Kappa -  laura e elisa: ", (p0-pe)/(1-pe))
file.write("Kappa -  laura e elisa: "+ str((p0-pe)/(1-pe))+"\n")


#kappa coefficient for annotators nagisa and elisa
aux = np.where((df['nagisa_score'] == df['elisa_score']), df['nagisa_score'], np.nan)
pos = np.sum(np.where(aux==1, 1, 0))
neg = np.sum(np.where(aux==-1, 1, 0))
undef = np.sum(np.where(aux==0, 1, 0))
p0 = (pos+neg+undef)/1000


pe = (elisapos*nagpos + elisaneg * nagneg + elisaundef * nagundef)/(1000*1000)

print("Kappa -  nagisa e elisa: ", (p0-pe)/(1-pe))
file.write("Kappa -  nagisa e elisa: "+ str((p0-pe)/(1-pe))+"\n")
file.close()


