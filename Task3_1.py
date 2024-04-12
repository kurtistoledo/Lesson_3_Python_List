# Lesson 3: Assignments: Python Lists
# 1. Python List Transformation
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]


grades_sort = sorted(grades, reverse=True)
print("Sorted grades (order going down):", grades_sort)

avg_grade = sum(grades) / len(grades)
print("Avg grade:", avg_grade)

grades_replaced = ['Failed' if grade < 80 else grade for grade in grades]
print("Grades with failed replaced:", grades_replaced)
