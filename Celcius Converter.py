#Celcius to Fahrenheit Conversion
#Version: 1.0
#Randy Moore
#Conversion formula:"F=9/5*C+32"

celsius = float(input("Enter temperature in celsius: "))
fahrenheit = (celsius * 9/5) + 32
print('%.2f Celsius is: %0.2f Fahrenheit' %(celsius, fahrenheit))