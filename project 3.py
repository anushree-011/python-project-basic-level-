#if the bill was $150.00, split between 5 people, wit 12% tip
print("Welcome to the tip calculator!")
bill = float(input("what was the total bill? $"))
tip = int(input("How much tip would you like to give? 10,12, or 15? "))
people=int(input("How many people to split the bill? "))
tip_as_percent=  tip / 100
total=bill*tip_as_percent
total_bill=bill+total
bill_per_person=total_bill/people
final=round(bill_per_person,2)
print(f"Each person should pay : ${final}")
