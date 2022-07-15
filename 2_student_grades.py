def avg(values):
    return sum(values) / len(values)


n = int(input())
grade_record = {}
for num in range(n):
    name, grade_str = input().split(' ')
    grade = float(grade_str)
    if name not in grade_record:
        grade_record[name] = []
    grade_record[name].append(grade)

for name, grades in grade_record.items():
    average_grade = avg(grades)
    grades_str = ' '.join(str(f'{x:.2f}') for x in grades)
    print(f'{name} -> {grades_str} (avg: {average_grade:.2f})')

