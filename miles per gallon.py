# Calculating miles per gallon

print ("This program calculates miles per gallon ")

# Ask input from user

miles_driven = input ("Enter miles driven: ")

#Convert text entered to a float point number

miles_driven = float (miles_driven)

#Get gallons used from the user

gallons_used = input ("Enter gallons used: ")

#Convert text entered to a float point number

gallons_used = float (gallons_used)

# Calculate and print the answer

mpg = miles_driven / gallons_used
print ("Miles per gallon: ", mpg)

