import random


# Create a seed number; seed is a random number
test_seed = int(input("Create a seed number:  "))
random.seed(test_seed)

random_side = random.randint(0, 1)
if random_side == 0:
    print("Tails")
elif random_side == 1:
    print("Heads")
