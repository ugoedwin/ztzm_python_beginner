students = {
"Alice": ["Math", "English", "Biology"],
"Bob": ["History", "Physics"],
"Charlie": ["Art", "Economics", "Math"]
}
students["Alice"].append("Computer Science")
students["Charlie"].remove("Art")

for name, courses in students.items():
    print(f"Student: {name}")
    print("Courses:", ", ".join(courses))
    print("---") 
          