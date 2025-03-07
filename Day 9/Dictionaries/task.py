student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for name in student_scores:
    if student_scores[name] <= 70:
        student_grades[name] = "Fail"

    elif student_scores[name] >= 71 and student_scores[name] <= 80:
        student_grades[name] = "Acceptable"

    elif student_scores[name] >= 81 and student_scores[name] <= 90:
        student_grades[name] = "Acceptable"

    elif student_scores[name] >= 91 and student_scores[name] <= 100:
        student_grades[name] = "Acceptable"

print(student_grades)