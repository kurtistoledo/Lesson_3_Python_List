# Lesson 3: Assignments: Python Lists
# 3. Advanced Slicing Techniques

temps = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

second_week_temps = temps[7:14]
print("Temps for the second week:", second_week_temps)

above_100_temps = [temp for temp in temps if temp > 100]
print("Temps above 100:", above_100_temps)

reversed_temps = temps[::-1]
reversed_temps = reversed_temps[4:10]
print("Temps from reversed list (5th to 10th day):", reversed_temps)
