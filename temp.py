print("Hello")


#learning with data quest

app_name = "Pandora"
average_rating = "4.0"
total_rating = "1724546"
price = "Free"
print(23.90 + 19.90 + 47.70)

#lists and some list functions

# leng() gets the length oa string. Useful for when you have a large data set.

row_1 = ["Facebook", 0.0, "USD", 2789675, 3.5]
print(row_1)
type(row_1)
row_3 =["Clash of Clans", 0.0, "USD", 2130805, 4.5]
row_2 = ["Instagram", 0.0, "USD", 2161558, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]
print(row_2)
print(row_3)

#isolating data in a list
fb_rating_data = [row_1[0], row_1[3], row_1[-1]]
print(fb_rating_data)

#list slicing
insta_rating_data = row_2[0:3]
print(insta_rating_data)
first_3 = row_3[:3] # a_list[:x]- this chooses the first x elements in list
last_3 = row_3[-3:] #a_list [-x:] chooses the last x elemnts in list.
app_data_set = [row_1, row_2, row_3, row_4, row_5] # app_data_set is a list of lists
print(app_data_set)
avg_rating = (row_1[-1] + row_2[-1] + row_3[-1] + row_4[-1] + row_5[-1]) / 5
#the above lne of code computes the average of the ratings but getting the data from app_data_set
print(avg_rating)

print("""----------------------------------------------------------------------------
      The code below  helps in eliminating the repitive process for avg_rating. 
      Imagine you had hundreds or millions of data, you'd die typing trying to find the avg_rating
      \n -----------------------------------------------------------------------------
      """)
#first introduce rating_sum variable outside of loop and initialise it to 0
rating_sum = 0.0
for each_list in app_data_set:
    rating = (each_list[-1])
    print(rating)
    rating_sum = rating_sum + rating
    
print(rating_sum)    
print("\n ---------------------------")
# we first sum up the elements in our loop before computing avrg_rating.
avrg_rating = rating_sum / 5
print(avrg_rating)

