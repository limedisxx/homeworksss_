from collections import defaultdict

grades_dict = defaultdict(list)

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Связываем оценки с именами студентов
students_grades = {students[i]: grades[i] for i in range(len(students))}

# Заполняем defaultdict средними оценками
for student, grades in students_grades.items():
    total_score = sum(grades)
    num_grades = l