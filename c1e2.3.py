#2.3 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Use 35 hours and a rate of 2.75 per hour to test the program (the pay should be 96.25). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking or bad user data.

inp1 = input("Enter Hours:")
conv1 = float(inp1)
inp2 = input("Enter Rate:")
conv2 =float(inp2)


print("Pay:",conv1*conv2)
