# ask the user to input how many students are registering 
total_students = int(input("Please enter the number of students registering: "))

for student in range(1, (total_students)+1):
    if student >= 1 or student <= int(total_students):
        student_id = input("Please enter the student ID: ")
        print(student_id)
    else:
        print("All students have now been entered")
with open("reg_form.txt", "w") as file:
    file.write(student_id + "...." + "\n")

 