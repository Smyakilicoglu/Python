# -*- coding: utf-8 -*-
"""
Created on Sat May  6 23:32:22 2023

@author: Sümeyra KILIÇOĞLU
"""
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country, vicits,cities):
    kullanılan = {}
    kullanılan["country"] = country
    kullanılan["visits"] = vicits
    kullanılan["cities"] = cities
    travel_log.append(kullanılan)
#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}

print(order["main"][2][0])
dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}
print(dict["b"])










