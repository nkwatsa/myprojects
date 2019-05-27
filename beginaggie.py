# -*- coding: utf-8 -*-
"""
Created on Fri May 24 06:00:07 2019

@author: Aggie
"""
#new ways to compute average rating with help from .append() method.
empty_list = []
print(empty_list)
empty_list.append("Alele")
print(empty_list)

row_1 = ["Facebook", 0.0, "USD", 2789675, 3.5]
print(row_1)
type(row_1)
row_3 =["Clash of Clans", 0.0, "USD", 2130805, 4.5]
row_2 = ["Instagram", 0.0, "USD", 2161558, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]
print(row_2)
print(row_3)

app_data_set = [row_1, row_2, row_3, row_4, row_5] #list of lists.

ratings = []
for row in app_data_set:
    rating = row[-1]
    ratings.append(rating)
print(ratings)
avg_ratings = sum(ratings) / len(ratings)
print(avg_ratings)