bill = float(input("What was the bill amount? "))
people = int(input("How people are there? "))
perPerson = round((bill / people) * 1.12, 2)
print(f"Each person has to pay: {perPerson}")
