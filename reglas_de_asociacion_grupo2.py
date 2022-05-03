# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 19:05:04 2022

@author: guill
"""
import pandas as pd
from apyori import apriori
from mlxtend.preprocessing import TransactionEncoder

movies = pd.read_csv('')

ratings = pd.read_csv('')

ratings = ratings[ratings['rating']>=4]

movies = movies.drop('genres', axis=1)

ratings = ratings.drop('timestamp', axis=1)

movies_ratings = pd.merge(ratings, movies, on='movieId', how='inner')

movies_ratings = movies_ratings.drop(['movieId', 'rating'], axis=1)

movies_ratings = movies_ratings.pivot(index="userId", columns="title")

'''
title = movies_ratings.title.to_list

itemsets=[[idx2title[mov] for mov in highratings[highratings.userId==user].movieId]
         for user in highratings.userId]

user_movies = []

for user in movies_ratings.userId:
    for movie in movies_ratings.title:
        if movie in:

for user in users_set:
    user_movies.append()
    for movie in movies_ratings:
        if user == movies_ratings.userId:
            user_movies.append(movies_rating.title)

            
users_set = set()

movies_set = 
'''            

                         
te=TransactionEncoder()
tr_ary=te.fit(movies_ratings['title']).transform(movies_ratings['title'])
ratings_bool = pd.DataFrame(tr_ary,columns=te.columns_)
ratings_bool.head()