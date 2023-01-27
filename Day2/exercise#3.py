#fString is very important and handy funtion in python as well let's learn it below

# score = 0
# height = 1.8
# isWinning = True

# print(f"your score is {score} , you are winning{isWinning} , your height is {height} ")

#it is very easy to write it in one line instead of writing everything seprately

#Create a program using maths and f-Strings that tells us 
# how many days, weeks, months we have left if we live until 90 years old.

age = input("what is your current age?")

age_as_int = int(age)

years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

message = f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left"

print(message)
