# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = str(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

highest_score = 0
for score in student_scores:
  score = int(score) # convert string to int
  if score > highest_score:
    highest_score = score
print(f"the highest score is: {highest_score}")

