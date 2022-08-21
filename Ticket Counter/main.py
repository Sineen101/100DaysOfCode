height = int(input("Enter your height in cm: "))
ticket = 0

if height > 120:
    print("You can ride the roller-coaster")
    age = int(input("Enter your age: "))
    if age < 12:
        print("Pay $5")
        ticket = 5
    elif age == 12 and age < 18:
        ticket = 7
    elif age >= 18:
        ticket = 12
    elif age >= 45 and age <= 55:
        print("Everything is gonna be okay. Your ride is on us!")
    photo = input("Do you want a photo? (y/n) ")
    if photo == "y":
        ticket += 3
        print(f"Pay ${ticket}")
    print(f"Your ticket is ${ticket}\nEnjoy the ride!")

else:
    print("Sorry, you can't ride the roller-coaster")
