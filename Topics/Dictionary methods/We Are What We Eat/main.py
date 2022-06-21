# the list "meals" is already defined
# your code here

totalCal = 0
for i in range(len(meals)):
    totalCal += meals[i]["kcal"]

print(totalCal)