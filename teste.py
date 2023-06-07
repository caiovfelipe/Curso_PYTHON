import pandas as pd

uri= "https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula1.2/ratings.csv"
filmes = pd.read_csv(uri)
filmes.columns = ['uruarioId', 'filmeId', 'nota', 'momento']
print(filmes.head())