from api_key import key
from get_location import coordinate
keyword = 'restaurant'

api_key = key

import pandas as pd, numpy as np
import requests
import json
import time
import os
final_data = []

os.chdir("C:/Users/Jmen3/Desktop/Programs/Python/Dinner Recommender/")


def makeData(adv,dis,cat, price):
    radius = dis*1609.34
    url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='+coordinate+'&radius='+str(radius)+'&keyword='+str(keyword)+'&key='+str(api_key)
    while True:
        print(url)
        respon = requests.get(url)
        jj = json.loads(respon.text)
        results = jj['results']
        for result in results:
            print(result)
            name = result['name']
            place_id = result ['place_id']
            lat = result['geometry']['location']['lat']
            lng = result['geometry']['location']['lng']
            rating = result['rating']
            types = result['types']
            vicinity = result['vicinity']
            data = [name, place_id, lat, lng, rating, types, vicinity]
            final_data.append(data)
            time.sleep(5)
        if 'next_page_token' not in jj:
            break
        else:
            next_page_token = jj['next_page_token']
            url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?key='+str(api_key)+'&pagetoken='+str(next_page_token)
    labels = ['Restaurant','ID', 'Latitude', 'Longitude','Rating', 'Types', 'Vicinity']
    export_dataframe_1_medium = pd.DataFrame.from_records(final_data, columns=labels)
    export_dataframe_1_medium.to_csv('data/restaurants.csv')


