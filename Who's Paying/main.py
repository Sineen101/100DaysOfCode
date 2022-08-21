import random


# Create a seed number; seed is a random number
test_seed = int(input("Create a seed number:  "))
random.seed(test_seed)

nameAsCSV = input("Give me everyone's names: ")
names = nameAsCSV.split(",")  # split the string into a list

# print a random name from the list
# print(names[random.randint(0, len(names)-1)] +
#       " is going pay for the meal today!")

print(random.choice(names)+" is going pay for the meal today!")
