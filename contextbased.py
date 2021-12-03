import pandas as pd
import numpy as np
from ast import literal_eval
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv('final.csv')
df = df[df['soup'].notna()]
count = CountVectorizer(stop_words='english')
count_matrix = count.fit_transform(df['soup'])
