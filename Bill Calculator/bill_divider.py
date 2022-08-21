print("``````````````BILL DIVIDER``````````````")
total_bill = float(input("What is the total bill? \n"))
tip = float(input("What tip do you want to leave? \n"))
people = int(input("How many people? \n"))
tip_percent = tip/100
total_tip = total_bill * tip_percent
bill = total_bill + total_tip
divided_bill = bill / people
bill_per_person = "{:.2f}".format(divided_bill, 2)  # format the bill per person to 2 decimal places
print(f"Each person should pay: ${bill_per_person}")
