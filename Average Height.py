student_heights = input("Input a list of student height").split()
for n in range(0,len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)
total_heights = sum(student_heights)
number_of_students = len(student_heights)
average_height = total_heights/number_of_students
print(average_height)