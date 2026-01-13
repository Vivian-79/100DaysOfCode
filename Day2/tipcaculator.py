print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
split = int(input("How many people to split the bill?"))
result = (bill + bill * tip * 0.01 ) / split
print(f"Each person should pay: ${result}")