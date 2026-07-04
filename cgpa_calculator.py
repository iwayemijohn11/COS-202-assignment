print("======================================")
print("    PERSONAL POCKET CGPA CALCULATOR")
print("======================================")

total_points = 0
total_units = 0

courses = int(input("Enter number of courses: "))

for i in range(courses):
    print(f"\nCourse {i+1}")

    unit = int(input("Course Unit: "))
    score = float(input("Score: "))

    if score >= 70:
        grade = "A"
        point = 5
    elif score >= 60:
        grade = "B"
        point = 4
    elif score >= 50:
        grade = "C"
        point = 3
    elif score >= 45:
        grade = "D"
        point = 2
    elif score >= 40:
        grade = "E"
        point = 1
    else:
        grade = "F"
        point = 0

    print("Grade:", grade)

    total_points += point * unit
    total_units += unit

cgpa = total_points / total_units

print("\n========================")
print("Your CGPA is:", round(cgpa, 2))

if cgpa >= 4.50:
    print("Class: First Class")
elif cgpa >= 3.50:
    print("Class: Second Class Upper")
elif cgpa >= 2.40:
    print("Class: Second Class Lower")
elif cgpa >= 1.50:
    print("Class: Third Class")
else:
    print("Class: Pass")

print("========================")