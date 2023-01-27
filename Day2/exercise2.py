#Mathemetical Opration
# basic things to remember 

#PEMDAS
# 1. Prenthesis : ()
# 2. exponents : **
# 3. Multiplication : *
# 4. division : /
# 5. Addition : +
# 6. Subtraction : -

# Example

print(3 * 3 + 3 / 3 - 3)

# left most will be priortize first


# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height

height = float(input("enter your height in meters : "))
weight = float(input("enter your weight in kgs : "))

BMI = weight / (height ** 2)
bmi_as_int = int(BMI)

print(bmi_as_int)



