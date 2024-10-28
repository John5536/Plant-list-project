import random
import pickle

num_plants = 0
current_plants=[]
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
            owner_input = input("Type yes to delete plant, type all to delete list \n").lower()
            if owner_input == "yes":
                plant_delete_selection = input("which plant would you like to delete? \n").lower()
                current_plants.remove(plant_delete_selection)
            if owner_input == "all":
                current_plants.clear()
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

print("Welcome to your plant notebook!")
adding_plants_to_list()

add_more = input("would you like to add more plants to your list? \n").lower()
if add_more == "yes":
    adding_plants_to_list()
else:
    print("ok")
    

