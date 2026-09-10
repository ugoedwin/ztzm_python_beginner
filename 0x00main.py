student = {}

print("Student Grading System")

while True:
    name = input("Enter student name (or type 'done' to finish): ")
    if name.lower() == 'done':
        break

    score = int(input(f"Enter {name}'s score: "))

    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'

    student[name] = {"score": score,
                      "grade": grade
                      }

    
print("\n--- Final Report ---")

for name, info in student.items():
    print(f"{name}: {info['score']} - Grade: {info['grade']}")
    