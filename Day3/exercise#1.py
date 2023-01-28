# LOOPS and NESTED LOOPS OVERVIEW

print("wecome to the rollercoster!")
height = int(input("please enter your height"))

if height >= 150:
    print("you can ride the rollercoster!")
    age = int(input("what is your age?"))
    if age <= 18:
        print("please pay $7")
    else:
        print("please pay $12")    
else:
    print("your have to grow taller before you can ride. ")    