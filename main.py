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
# 4- display the random choice
# 5- confirmation and otherwise


# greeting message
print("**** Welcome to Week 2 Project : Day Trip Generator ****")
print("**** Computer has 4 random destinations in southern California to select ****")

# lists & random function 
destinations           = ["La Jolla", "Oceanside", "Laguna Beach", " Huntington Beach"]
destination_random     = random.choice(destinations)

restaurants            = ["Herringbone", "Harbor Fish & chips", "Salt Greek Grill", " Blue Gold"]
restaurant_random      = random.choice(restaurants) 

transportations        = ["rental car" , "train" , "Helicopter", " bus tour"]
transportation_random  = random.choice(transportations)

entertainments         = [ "Downtown Tours", "Surf show" , " Downtown & Galary tours", "Air show"] 
entertainment_random   = random.choice(entertainments)


# first random choice 
day_trip_random = (f"Computer has selected {destination_random} for your destination, {restaurant_random} restaurant to eat, {transportation_random} to travel around there , and a {entertainment_random}.")
print(day_trip_random)
user_input_confirmation = input(" To confirm . please enter y/n :  ")

if user_input_confirmation =="y" :
   print(f" your destination is {destination_random} , you eat at {restaurant_random} , your transporation is {transportation_random} , and your entertainment is {entertainment_random} ")


# if user wants another choice : destination , ............

# new random destination 
def new_destination(user_input_confirmation):  
  while user_input_confirmation != 'y':
    destination_random = random.choice(destinations)
    user_input_confirmation= input(f"We are sorry that the previous option did not work for your. We have seleceted {destination_random} as another trip destination. Works for you? ")
  else:
    print(f"You have selected {destination_random} destination.")

new_destination(user_input_confirmation)


# new random restaurant
def new_restaurant(user_input_confirmation):  
  while user_input_confirmation != 'y':
    restaurant_random  = random.choice(restaurants)
    user_input_confirmation= input(f"We are sorry that the previous option did not work for your. We have seleceted {restaurant_random} as another trip destination. Works for you? ")
  else:
    print(f"You have selected {restaurant_random} restaurants")

new_restaurant(user_input_confirmation)

# new random transportation
def new_transportation(user_input_confirmation):  
  while user_input_confirmation != 'y':
    transportation_random  = random.choice(transportations)
    user_input_confirmation= input(f"We are sorry that the previous option did not work for your. We have seleceted {transportation_random} as another trip destination. Works for you? ")
  else:
    print(f"You have selected {transportation_random} restaurants")

new_transportation(user_input_confirmation)

# new random entertainment
def new_entertainment(user_input_confirmation):  
  while user_input_confirmation != 'y':
    entertainment_random  = random.choice(entertainment_random)
    user_input_confirmation= input(f"We are sorry that the previous option did not work for your. We have seleceted {entertainment_random} as another trip destination. Works for you? ")
  else:
    print(f"You have selected {entertainment_random} restaurants")

new_entertainment(user_input_confirmation)

print(f"You day trip selection is completed ")
print(f" your destination is {destination_random} , you eat at {restaurant_random} , your transporation is {transportation_random} , and your entertainment is {entertainment_random} ")












