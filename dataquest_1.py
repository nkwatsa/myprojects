# -*- coding: utf-8 -*-
"""
Created on Thu May 23 16:36:26 2019

@author: Aggie
"""

#opening files
from csv import reader
opened_file = open('AppleStore.csv', encoding = 'utf-8') 
#please in this examples, withot the enconding parameter, it brought an encoding error. So please include it in all aspects
opened_file
read_file = reader(opened_file)

apps_data = list(read_file)

print(apps_data[:5])
print("HELOOO LETS PLAY WIT")
print(len(apps_data))
print(apps_data[0])
print("-------------------------")
 # line above prints first row of this data set apps_data. This contains the titles of the diff columns

print(apps_data[1:3])
#above code prints the first and second rows in this data set.

print("----------------------------------------------------------------")
print("\n The below code tries to find the avergae rating for the apps in this data set.")
#we use apps_data[1:] bcz the first row contains the column names of the diff data points in this
#data set. So if you try to compute the average rating, it will bring an error.

rating_sum = 0
for row in apps_data[1:]:
    rating = float(row[8])
    #print(rating[:7])#we cast the values here to floats  because intially they are enclosed in quotes hence strings and math computations on strings isnt right. will bring an error.
    rating_sum = rating_sum + rating
print(rating_sum)
avg_rating = rating_sum / 7197
print(avg_rating)

#say we wanted to find the avg ratinf for free apps i.e apps with 0.0 in price, we use if statemnt here,
free_app_ratings = []
for row in apps_data[1:]:
    rating_free = float( row[8])
    price = float(row[5])
    if price == 0.0:
        free_app_ratings.append(rating_free)
avrg_rating_freeApps =  sum(free_app_ratings) / len(free_app_ratings)
print(avrg_rating_freeApps)


#say we wanted  to comapre rating for gaming apps to ratings for non-gaming apps.

game_app_rating = []
non_game_rating = []
for row in apps_data[1:]:
    rating_game = float(row[8])
    game_genre = row[12]
    if game_genre == "Games":
        game_app_rating.append(rating_game)
    if game_genre != "Games":
        non_game_rating.append(rating_game)
        
    # if game_genre == "Games" or game_genre =="Social Networking":
        
   #  if game_genre == "Games" and price == 0.0:

    
    #we could also type that using the "and" keyword to evaluate multiple conditions.
    #z.B if we needed to avg rating for free gaming apps as in the example below
    # we could say " if price == 0.0 and genre == "Games": ...ut your other statements
    #theres also using "or" LOGICAL oprator too.
        
avrg_rating_gaming = sum(game_app_rating) / len(game_app_rating)
avrg_rating_nonGame = sum(non_game_rating) / len(non_game_rating)
print("Average rating for games apps is: " , avrg_rating_gaming)
print("And for non_gaming apps is: ", avrg_rating_nonGame)

#the if statement here includes both and & or LOGICAL OPERATORS. we compute the average
#rating for non free apps that are either social networking apps or gaming apps.

non_free_socialGame_ratings =[]       
for row in apps_data[1:]:
    rating1 = float(row[8])
    price = float( row[5])
    genre = row[12]
    
    if (genre == "Social Networking" or genre == "Games") and price != 0:
        non_free_socialGame_ratings.append(rating1)
    
avg_non_free = sum(non_free_socialGame_ratings) / len(non_free_socialGame_ratings)
print(avg_non_free)

#COMPARISON OPERATORS 
#the code below  is a way to answer the qsn: HOW MANY APPS HAVE RATING OF 4.0 OR GREATER?
n_of_apps = 0
for row in apps_data[1:]:
    rating_4 = float(row[8])
    if rating_4 >= 4.0:
        n_of_apps = n_of_apps + 1
print("num of apps with rating of 4,0 or grater is:" , n_of_apps)