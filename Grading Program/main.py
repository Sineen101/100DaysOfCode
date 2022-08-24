student_scores = {
    "student1": 81,
    "student2": 78,
    "student3": 99,
    "student4": 74,
    "student5": 62,
}

student_grades = {}

for student in student_scores:
    if student_scores[student] > 90:
        student_grades[student] = ["Outstanding! You got an A"]
    elif student_scores[student] > 80:
        student_grades[student] = ["Exceeds Expectations! You got a B"]
    elif student_scores[student] > 70:
        student_grades[student] = ["Acceptable! You got a C"]
    elif student_scores[student] < 70:
        student_grades[student] = ["Fail! You got an F"]
    else:
        print("Invalid input!")

print(student_grades)
