import random
import pickle
import tkinter as tk

num_plants = 0
current_plants=[]
plant_watered = []
filename = "current_plants.pkl"
def adding_plants_to_list():
    global current_plants, num_plants

    try:
        with open(filename, 'rb') as file:
            current_plants =pickle.load(file)
    except FileNotFoundError:
        current_plants = []

    plants_inputed = input("Would you like to add a plant to your list? If so type its name. Type no for other options \n").lower()
    if plants_inputed == "no":
            owner_input = input("type delete to delete plant, type all to delete list, type continue. \n").lower()
            if owner_input == "delete":
                plant_delete_selection = input("which plant would you like to delete? \n").lower()
                current_plants.remove(plant_delete_selection)
            elif owner_input == "all":
                current_plants.clear()
            elif owner_input == "continue":
                print("ok")
    else:
        plants_inputed not in current_plants
        current_plants.append(plants_inputed)
        


    with open(filename, 'wb') as file:
        pickle.dump(current_plants, file)
    

    check_on_list = input("would you like to view your current list? \n").lower()
    if check_on_list == "yes":
        print(current_plants, len(current_plants))
    else:
        print("ok")
 
def watering_plants_func():
    #plant on list watered. Goal/ add date to plant watered. Make it saved to the correct plant. 
    global plant_watered
    which_plant_watered = input("which plant did you water?").lower()
    plant_watered.append(which_plant_watered)
    print(f"{which_plant_watered}was watered and added to your list")
    print(plant_watered)
    YN_another_plant = input("any other plants watered? type yes or no").lower()
    if YN_another_plant == "yes":
       water_another_plant = input("which plant would you like to water?")
       plant_watered.append(water_another_plant)
    print(plant_watered)



print("Welcome to your plant notebook!")
adding_plants_to_list()

add_more = input("would you like to add more plants to your list? \n").lower()
if add_more == "yes":
    adding_plants_to_list()
else:
    print("ok")

water_main = input("would you like to water any plants?").lower()
if water_main == "yes":
    watering_plants_func()
else:
    print("ok")



