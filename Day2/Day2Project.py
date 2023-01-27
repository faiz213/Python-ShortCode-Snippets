# Day 2 Project: Tip Calculator

totalBill = float(input("what was the total bill? $"))
tip =       int(input("how much tip you want to give in percentage? 5% , 10% , or 12% "))
people =    int(input("how many people to split the bill?"))

bill_with_tip = tip /100 * totalBill + totalBill
bill_per_person = totalBill / people
finalAmount = round(bill_per_person , 2)

print(f"each person should pay  {finalAmount}" )


