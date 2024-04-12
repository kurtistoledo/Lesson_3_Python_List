# Given list of grades
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

# Task 1: Sort the grades in descending order
grades_sorted = sorted(grades, reverse=True)
print("Sorted grades (descending order):", grades_sorted)

# Task 2: Calculate the average grade
average_grade = sum(grades) / len(grades)
print("Average grade:", average_grade)

# Task 3: Replace grades below 80 with "Failed"
grades_replaced = ['Failed' if grade < 80 else grade for grade in grades]
print("Grades with failed replaced:", grades_replaced)
