#Write a program that calculates the total amount of a meal purchased at a restaurant. 
# The program should ask the user to enter the charge for the food, then calculate the amounts of a 18 percent tip and 7 percent sales tax. 
# Display each of these amounts and the total. (15 points)
#Randy Moore
#Version 1.0

foodCost = float(input("enter the cost of food: "))
Tip = foodCost * .18
Tax = foodCost * .07
Total = foodCost + Tip + Tax
print("The Food Cost: " + str(foodCost))
print("The Total Tip for the Food: " + str(Tip))
print("The Total Tax for the food: " + str(Tax))
print("Total: " + str(Total))