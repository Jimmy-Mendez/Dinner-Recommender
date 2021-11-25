import pandas as pd
from getDinner import makeData
from getCategory import getCategory
from visited import past
import random


#Return string with restaurant name

def chooseRestaurant(adv,cat,dist):
    
    if int(dist)<=0:
        return "invalid input"
    
    restaurants = makeData(dist)
    for item in past:
        if adv == '1':
            restaurants = restaurants[restaurants['Restaurant'] != item]
        elif adv == '0':
            #restaurants = restaurants[restaurants['Restaurant'] == item]
            print("test")
        else:
            return "invalid input"
    
    restaurants_cat = getCategory(restaurants,'Restaurant', 'Vicinity')
    
    if cat != "Surprise me!":
        restaurants_cat1 = restaurants_cat[restaurants_cat['category'].str.contains(cat, case=False)]
        restaurants_cat2 = restaurants_cat[restaurants_cat['Restaurant'].str.contains(cat, case=False)]
        restarants_cat = restaurants_cat1.append(restaurants_cat2)
    
    if len(restaurants_cat.index)==0:
        return "no restaurants within " + str(dist) + " miles fit this criteria" 
    
    index = random.randint(0, len(restaurants_cat.index))
    
    result = str(restaurants_cat.at[index, 'Restaurant'])
    
    return result
    
    