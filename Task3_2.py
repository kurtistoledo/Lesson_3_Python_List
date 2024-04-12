# Lesson 3: Assignments: Python Lists
# 2. Advanced List Methods and Identity Operators

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

common_students = list(set(submitted) & set(attended))
print("Common students:", common_students)

lists_identical = sorted(submitted) == sorted(attended)
print("Are the lists identical?:", lists_identical)

attended = [student for student in attended if student in submitted]
print("Attended list after removal:", attended)
