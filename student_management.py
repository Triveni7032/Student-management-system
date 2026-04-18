students = {}

def add_student():
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks
    print("Student added successfully")

def view_students():
    if not students:
        print("No records found")
    else:
        for name, marks in students.items():
            print(f"{name} : {marks}")

def delete_student():
    name = input("Enter name to delete: ")
    if name in students:
        del students[name]
        print("Student deleted")
    else:
        print("Student not found")

while True:
    print("\n1.Add 2.View 3.Delete 4.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        break
    else:
        print("Invalid choice")