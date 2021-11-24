import pandas as pd
from getDinner import makeData
from getCategory import getCategory

#Return string with restaurant name

def chooseRestaurant(adv,cat,dist):
    
    restaurants = makeData(dist)
    restaurants_cat = getCategory(restaurants,'Restaurant', 'Vicinity')
    
    if adv == '1':
        return "Yeeeet"
    elif adv == '0':
        return "Yeet"
    else:
        return "Invalid input"