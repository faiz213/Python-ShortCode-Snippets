#to find avrage of student

student_heights = input("Input a list of student heights ").split()
student_heights = [int(i) for i in student_heights]

total_height = 0
for height in student_heights:
    total_height += height

number_of_students = len(student_heights)
average_height = round(total_height / number_of_students)
print(average_height)
     