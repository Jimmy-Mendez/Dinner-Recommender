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
            restaurants = restaurants[restaurants['Restaurant'] == item]
        else:
            return "invalid input"
    
    restaurants_cat = getCategory(restaurants,'Restaurant', 'Vicinity')
    
    if cat != "Surprise me!":
        restaurants_cat = restaurants_cat[restaurants_cat['category'].str.contains(cat, case=False)]
    
    if len(restaurants_cat.index)==0:
        return "no restaurants within " + str(dist) + " fit this criteria" 
    
    index = random.randint(0, len(restaurants_cat.index))
    
    result = str(restaurants_cat.at[index, 'Restaurant'])
    
    return result
    
    