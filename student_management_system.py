class Student:
    def __init__(self, name, id_number, birth_date):
        self.name = name
        self.id_number = id_number
        self.birth_date = birth_date
        self.subjects = []
    
    def add_subject(self, subject):
        if len(self.subjects) < 6:
            self.subjects.append(subject)
        else:
            print("Error: Student cannot have more than 6 subjects.")

    def remove_subject(self, subject):
        if subject in self.subjects:
            self.subjects.remove(subject)
        else:
            print("Error: Subject not found.")

    def __str__(self):
        return f"Student(name={self.name}, id_number={self.id_number}, birth_date={self.birth_date}, subjects={self.subjects})"
    
class StudentManagementSystem:
    def __init__(self):
        self.students = {}
    
    def register_student(self, name, id_number, birth_date):
        if id_number in self.students:
            print("Error: The ID number is already registered.")
            return
        if not self.validate_date(birth_date):
            print("Error: Invalid birth date.")
            return
        student = Student(name, id_number, birth_date)
        self.students[id_number] = student
        print(f"Student {name} registered successfully.")
    
    def edit_student(self, id_number, name=None, birth_date=None):
        if id_number not in self.students:
            print("Error: Student not found.")
            return
        student = self.students[id_number]
        if name:
            student.name = name
        if birth_date and self.validate_date(birth_date):
            student.birth_date = birth_date
        print(f"Student {student.name} edited successfully.")

    def delete_student(self, id_number):
        if id_number in self.students:
            del self.students[id_number]
            print(f"Student {id_number} deleted successfully.")
        else:
            print("Error: Student not found.")
    
    def search_student(self, name=None, id_number=None):
        if name:
            for student in self.students.values():
                if student.name.lower() == name.lower():
                    print(student)
                    return
        elif id_number:
            if id_number in self.students:
                print(self.students[id_number])
                return
        else:
            print("Error: Student not found.")
    
    def total_students(self):
        return len(self.students)
    
    def generate_report(self):
        print("\nReport:")
        print(f"Total students: {self.total_students()}")
        for student in self.students.values():
            print(student)
    
    def validate_date(self, date):
        try:
            from datetime import datetime
            datetime.strptime(date, "%Y-%m-%d")
            return True
        except ValueError:
            return False

def main():
    system = StudentManagementSystem()
    while True:
        print("\nStudent Management System")
        print("1. Register student")
        print("2. Edit student")
        print("3. Delete student")
        print("4. Search student")
        print("5. Total students")
        print("6. Generate report")
        print("7. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter student name: ")
            id_number = input("Enter student ID number: ")
            birth_date = input("Enter student birth date (YYYY-MM-DD): ")
            system.register_student(name, id_number, birth_date)
        elif choice == "2":
            id_number = input("Enter student ID number: ")
            name = input("Enter student name: ")
            birth_date = input("Enter student birth date (YYYY-MM-DD): ")
            system.edit_student(id_number, name, birth_date)
        elif choice == "3":
            id_number = input("Enter student ID number: ")
            system.delete_student(id_number)
        elif choice == "4":
            name = input("Enter student name: ")
            id_number = input("Enter student ID number: ")
            system.search_student(name, id_number)
        elif choice == "5":
            print(f"Total students: {system.total_students()}")
        elif choice == "6":
            system.generate_report()
        elif choice == "7":
            print("Exiting the system... Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()