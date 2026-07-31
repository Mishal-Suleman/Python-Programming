#Student Management System

# def stud_info(id, name, gpa):
#     stud_list
  
    

# print("**************Welcome to Student Management System*********************")
# x=input("Add Record: press A\nSearch Reacord: press S")
# if x=='A':
#     a=int(input("Enter ID :"))
#     b=input("Enter Name :")
#     c=float(input("Enter GPA :"))
#     stud_info(a,b,c)

"""
Student Management System
--------------------------
A console-based program to add, search, update, delete and view
student records. Every risky operation is wrapped in try / except /
else / finally blocks so bad input or runtime errors never crash
the program.

Run with: python student_management_system.py
"""

import re
import json
import os
class DuplicateRollNumberError(Exception):
    """Raised when a roll number already exists in the system."""
    pass
class StudentNotFoundError(Exception):
    """Raised when a lookup finds no matching student."""
    pass
class InvalidInputError(Exception):
    """Raised when user input fails validation."""
    pass
class StudentManagementSystem:
    def __init__(self, data_file="students.json"):
        self.data_file = data_file
        self.students = {}   # roll_no -> dict(name, age, grade)
        self._load_data()
    # ---------- persistence ----------
    def _load_data(self):
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, "r") as f:
                    self.students = json.load(f)
        except (json.JSONDecodeError, OSError) as e:
            print(f"[Warning] Could not load existing data ({e}). Starting fresh.")
            self.students = {}
        finally:
            # This always runs, confirming load attempt is complete
            pass
    def _save_data(self):
        try:
            with open(self.data_file, "w") as f:
                json.dump(self.students, f, indent=2)
        except OSError as e:
            print(f"[Error] Could not save data to disk: {e}")
        else:
            pass
        finally:
            pass
    # ---------- validation helpers ----------
    @staticmethod
    def _validate_roll_no(roll_no):
        roll_no = roll_no.strip()
        if not roll_no:
            raise InvalidInputError("Roll number cannot be empty.")
        if not re.match(r"^[A-Za-z0-9\-]+$", roll_no):
            raise InvalidInputError(
                "Roll number can only contain letters, digits, and hyphens."
            )
        return roll_no
    @staticmethod
    def _validate_name(name):
        name = name.strip()
        if not name:
            raise InvalidInputError("Name cannot be empty.")
        if not re.match(r"^[A-Za-z .'-]+$", name):
            raise InvalidInputError("Name must contain only letters and spaces.")
        return name
    @staticmethod
    def _validate_age(age_str):
        try:
            age = int(age_str)
        except ValueError:
            raise InvalidInputError("Age must be a whole number.")
        if age <= 0 or age > 100:
            raise InvalidInputError("Age must be between 1 and 100.")
        return age
    @staticmethod
    def _validate_grade(grade_str):
        grade_str = grade_str.strip().upper()
        valid_grades = {"A", "B", "C", "D", "F"}
        if grade_str not in valid_grades:
            raise InvalidInputError(f"Grade must be one of {sorted(valid_grades)}.")
        return grade_str
    # ---------- core operations ----------
    def add_student(self, roll_no, name, age_str, grade_str):
        try:
            roll_no = self._validate_roll_no(roll_no)
            if roll_no in self.students:
                raise DuplicateRollNumberError(
                    f"Roll number '{roll_no}' already exists."
                )
            name = self._validate_name(name)
            age = self._validate_age(age_str)
            grade = self._validate_grade(grade_str)
        except (InvalidInputError, DuplicateRollNumberError) as e:
            print(f"[Add failed] {e}")
            return False
        else:
            self.students[roll_no] = {"name": name, "age": age, "grade": grade}
            self._save_data()
            print(f"[Success] Student '{name}' (Roll No: {roll_no}) added.")
            return True
        finally:
            print("--- Add student attempt finished ---")

    def search_student(self, roll_no):
        try:
            roll_no = self._validate_roll_no(roll_no)
            if roll_no not in self.students:
                raise StudentNotFoundError(f"No student found with roll no '{roll_no}'.")
        except (InvalidInputError, StudentNotFoundError) as e:
            print(f"[Search failed] {e}")
            return None
        else:
            record = self.students[roll_no]
            print(f"[Found] {roll_no}: {record}")
            return record
        finally:
            print("--- Search attempt finished ---")
    def update_student(self, roll_no, name=None, age_str=None, grade_str=None):
        try:
            roll_no = self._validate_roll_no(roll_no)
            if roll_no not in self.students:
                raise StudentNotFoundError(f"No student found with roll no '{roll_no}'.")
            record = self.students[roll_no]
            updated = dict(record)  # work on a copy so a bad field doesn't half-apply
            if name is not None and name.strip():
                updated["name"] = self._validate_name(name)
            if age_str is not None and age_str.strip():
                updated["age"] = self._validate_age(age_str)
            if grade_str is not None and grade_str.strip():
                updated["grade"] = self._validate_grade(grade_str)
        except (InvalidInputError, StudentNotFoundError) as e:
            print(f"[Update failed] {e}")
            return False
        else:
            self.students[roll_no] = updated
            self._save_data()
            print(f"[Success] Student '{roll_no}' updated: {updated}")
            return True
        finally:
            print("--- Update attempt finished ---")
    def delete_student(self, roll_no):
        try:
            roll_no = self._validate_roll_no(roll_no)
            if roll_no not in self.students:
                raise StudentNotFoundError(f"No student found with roll no '{roll_no}'.")
        except (InvalidInputError, StudentNotFoundError) as e:
            print(f"[Delete failed] {e}")
            return False
        else:
            removed = self.students.pop(roll_no)
            self._save_data()
            print(f"[Success] Deleted student '{roll_no}': {removed}")
            return True
        finally:
            print("--- Delete attempt finished ---")
    def list_students(self):
        try:
            if not self.students:
                raise StudentNotFoundError("No students in the system yet.")
        except StudentNotFoundError as e:
            print(f"[Info] {e}")
        else:
            print("\n--- All Students ---")
            for roll_no, info in self.students.items():
                print(f"{roll_no}: {info}")
            print("--------------------")
        finally:
            print("--- List operation finished ---\n")
# ---------- console menu / interaction layer ----------
def get_input(prompt):
    """Wraps input() so Ctrl+C / Ctrl+D don't crash the program."""
    try:
        return input(prompt)
    except (EOFError, KeyboardInterrupt):
        print("\n[Info] Input interrupted. Returning to menu.")
        return None
def main():
    system = StudentManagementSystem()
    menu = """
==== Student Management System ====
1. Add Student
2. Search Student
3. Update Student
4. Delete Student
5. List All Students
6. Exit
Choose an option (1-6): """
    while True:
        try:
            choice = get_input(menu)
            if choice is None:
                continue
            choice = choice.strip()
            if choice == "1":
                roll_no = get_input("Roll No: ")
                name = get_input("Name: ")
                age_str = get_input("Age: ")
                grade_str = get_input("Grade (A-F): ")
                if None in (roll_no, name, age_str, grade_str):
                    continue
                system.add_student(roll_no, name, age_str, grade_str)
            elif choice == "2":
                roll_no = get_input("Roll No to search: ")
                if roll_no is None:
                    continue
                system.search_student(roll_no)
            elif choice == "3":
                roll_no = get_input("Roll No to update: ")
                if roll_no is None:
                    continue
                print("Leave a field blank to keep it unchanged.")
                name = get_input("New Name: ")
                age_str = get_input("New Age: ")
                grade_str = get_input("New Grade: ")
                system.update_student(roll_no, name, age_str, grade_str)
            elif choice == "4":
                roll_no = get_input("Roll No to delete: ")
                if roll_no is None:
                    continue
                system.delete_student(roll_no)
            elif choice == "5":
                system.list_students()
            elif choice == "6":
                print("Exiting. Data has been saved to disk.")
                break
            else:
                raise InvalidInputError("Please choose a number between 1 and 6.")
        except InvalidInputError as e:
            print(f"[Error] {e}")
        except Exception as e:
            # Catch-all so any unexpected runtime error is reported,
            # not left to crash the whole program.
            print(f"[Unexpected error] {type(e).__name__}: {e}")
        finally:
            pass  # menu loop continues regardless of what happened above
if __name__ == "__main__":
    main()



     

