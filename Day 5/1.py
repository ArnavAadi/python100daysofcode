# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

ht = 0
lt = 0

# Write your code below this row 👇
for std in student_heights:
    ht += std
    lt += 1

avr_ht = round(ht/lt)

print(avr_ht)
