import PyQt5
from getDinner import makeData

adventure = input("Are you feeling adventurous? (1 = yes, 0 = no): ")
distance = input("Max distance (in miles): ")
category = input("Categories?: ")
price = input("Price Range?: ")


makeData(adventure,distance,category, price)