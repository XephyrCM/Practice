#Randy moore
#Version 1.0
#Python code to get sum of numbers
   
# Function to get sum of digits 
from re import U


userSum = int(float(input("Enter Number here: ")))

def getsum(userSum):
    sum = 0 
    for digit in str(userSum):
        sum += int(digit)
    return sum

print("Here is the Number: " + str(getsum(userSum)))