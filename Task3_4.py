# Lesson 3: Assignments: Python Lists
# 4. Deep Dive into Python Lists

students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

filtered_students = []
filtered_grades = []
filtered_activities = []

for i in range(len(students)):
    if grades[i] >= 80:
        filtered_students.append(students[i])
        filtered_grades.append(grades[i])
        filtered_activities.append(activities[i])

print("Name:", filtered_students[-1])
print("Grade:", filtered_grades[-1])
print("Activity:", filtered_activities[-1])

students_approved = filtered_students
print("Approved Students:", students_approved)
