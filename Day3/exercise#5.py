# rollercoster app updated

print("WELCOME TO ROLLERCOSTER RIDE!!")
height = int(input("to get started first tell me your height in cm  ? "))
if height > 120:
    print("you can ride in rollercoster ")

    age  = int(input("tell me your age sir ? "))
    if age < 12:
        bill = 5
        print(" your total bill is $5 ")
        
    elif age <= 18 :
    
        bill = 12

    else :
        bill = 12
        print("adults ticket are $12")     


    wants_photo = input("do you want to take photo ? Y or N ")
    if wants_photo == "Y":
        bill +=3
        print(f"final price is ${bill}  ")

    else:
        print(f"your final price is ${bill}")    
else:
    print("sorry you have to grow taller before you ride on rollercoster")