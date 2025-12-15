def load_students():
    students = []
    try:
        with open("students.txt", "r") as file:
            for line in file:
                name, marks = line.strip().split("|")
                marks = list(map(int, marks.split(",")))
                students.append({
                    "name": name,
                    "marks": marks
                })
    except FileNotFoundError:
        open("students.txt", "a")
    return students


def save_students(students):
    with open("students.txt", "w") as file:
        for s in students:
            marks_str = ",".join(map(str, s["marks"]))
            file.write(f"{s['name']}|{marks_str}\n")


def calculate_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 75:
        return "B"
    elif percentage >= 60:
        return "C"
    else:
        return "D"


def add_student(students):
    name = input("Enter student name: ")
    marks = []

    for i in range(1, 6):
        mark = int(input(f"Enter marks for subject {i}: "))
        marks.append(mark)

    students.append({
        "name": name,
        "marks": marks
    })
    print("Student record added successfully!")


def show_students(students):
    if not students:
        print("No records found.")
        return

    print("\n------ Student Results ------")
    for s in students:
        total = sum(s["marks"])
        percentage = total / len(s["marks"])
        grade = calculate_grade(percentage)

        print(f"\nName: {s['name']}")
        print(f"Marks: {s['marks']}")
        print(f"Total: {total}")
        print(f"Percentage: {percentage:.2f}%")
        print(f"Grade: {grade}")


# -------- MAIN PROGRAM --------
students = load_students()

while True:
    print("\n1. Add Student Result")
    print("2. View All Results")
    print("3. Save & Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_student(students)
    elif choice == "2":
        show_students(students)
    elif choice == "3":
        save_students(students)
        print("Data saved. Goodbye!")
        break
    else:
        print("Invalid choice.")
