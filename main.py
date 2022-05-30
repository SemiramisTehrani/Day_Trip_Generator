# Week 2 : DAY TRIP GENERATOR Project Framework
#(5 points): As a developer, I want to make at least three commits with descriptive messages. 
#(5 points): As a developer, I want to store my destinations, restaurants, mode of transportations, and entertainments in their own separate lists. 
#(5 points): As a user, I want a destination to be randomly selected for my day trip. 
#(5 points): As a user, I want a restaurant to be randomly selected for my day trip. 
#(5 points): As a user, I want a mode of transportation to be randomly selected for my day trip. 
#(5 points): As a user, I want a form of entertainment to be randomly selected for my day trip. 
#(15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don’t like one or more of those things. 
#(10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections. 
#(10 points): As a user, I want to display my completed trip in the console. 
#(5 points): As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing!



import random




# 1- greeting message
# 2- lists : Destinations, Restaurants, mode of transportations, and entertainments.
# 3- random choices for each list 


# greeting function
print("**** Welcome to Week 2 Project : Day Trip Generator ****")
print("**** Computer has 4 random destinations in southern California to select ****")

destinations    = ["La Jolla", "Oceanside", "Laguna Beach", " Huntington Beach"]
destination     = random.choice(destinations)

restaurants     = ["Herringbone La Jolla", "Harbor Fish & chips", "Salt Greek Grill", " Blue Gold"]
restaurant      = random.choice(restaurants) 

transportations = ["rental car" , "train" , "Helicopter", " bus tour"]
transportation  = random.choice(transportations)

entertainments  = [ "Downtown Tours", "Surf show" , " Downtown & Galary tours", "Air show"] 
entertainment   = random.choice(entertainments)











