student_marks = input("Input a list of student marks").split()
for n in range(0,len(student_marks)):
    student_marks[n] = int(student_marks[n])
print(max(student_marks))