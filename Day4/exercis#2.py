#You are going to write a program that will select a random name from a list of names.
#  The person selected will have to pay for everybody's food bill.

import random

name_string = input("give me everybody's name separated by comma: ")

names = name_string.split(", ")

num_items = len(names)

random_choice = random.randint(0, num_items - 1)

person_who_will_pay = names[random_choice]

print(person_who_will_pay + " is going to buy the meal today")
