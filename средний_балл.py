from collections import defaultdict

grades_dict = defaultdict(list)

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}


for i in range(len(grades)):
    for grade in grades[i]:
        grades_dict[students.pop()].append(grade)

for student, grades in grades_dict.items():
    total_score = sum(grades)
    num_grades = len(grades)
    avg_score = total_score / num_grades
    grades_dict[student] = avg_score

print(grades_dict)
