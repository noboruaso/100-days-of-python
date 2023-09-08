print("Welcome to the tip calculator.\n")

total_bill = float(input("What was the total bill? $"))
tip_percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people_number = int(input("How many people to split the bill? "))

pay_amount = total_bill*(1+tip_percent/100)
split_amount = round(pay_amount/people_number, 2)

print(f"Each person should pay: ${split_amount}")