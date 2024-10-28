import random


num_plants = 0
current_plants=[]
plants_inputed = input("what kind of plant do you own?")
if plants_inputed not in current_plants:
    current_plants.append(plants_inputed)
    num_plants += 1
print(f"you have just added {plants_inputed}")
print(current_plants, num_plants)
print(f"Your current plants{current_plants}")
