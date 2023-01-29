#Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

# It should tell them the interpretation of their BMI based on the BMI value.

# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.

height = float(input("enter your height in m: "))
weight = float(input("enter your  your weight in kg: "))


bmi = round(weight / (height **2))
if weight < 18.5:
    print(f"your bmi is {bmi},  you are underweight")
elif weight < 25:
    print(f"your bmi is {bmi}, you are normal weight!!")   
elif weight < 30:
    print(f"your bmi is {bmi},you are slightly overwieght")
elif weight < 35:
    print(f"your bmi is {bmi}, you are obese")
else:
    print(f"your bmi is {bmi}, you are clinically obese")
