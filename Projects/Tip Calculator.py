print("Welcome to the tip calculator.")
bill = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill?")
bill_as_float = float(bill)
tip_as_float = float(tip)
people_as_int = int(people)
tip_as_float_percent = tip_as_float / 100
tip_as_float_percent_plus_1 = tip_as_float_percent + 1
total_bill = bill_as_float * tip_as_float_percent_plus_1
bill_per_person = total_bill / people_as_int
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")