from datetime import date

print("Hello World of Practice")

fruitList = ["apples", "oranges", "tomatos"]
for fruits in fruitList:
    print(fruits)

sum = 2 + 3

print("2 + 3 = " + str(sum))

print("User Input Practice\n-----------------------------\n-----------------------------\n")
currentYear = date.today()
date = currentYear.strftime("%Y")
userAge = input("Enter your age: ")
yearBorn = int(date) - int(userAge)
print("If you are " + str(userAge) + ", then you were most likely born on " + str(yearBorn))