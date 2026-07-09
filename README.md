# 🎓 Student Data Organizer

[![Watch the Demo Video](https://img.shields.io/badge/▶-Watch%20Demo%20Video-red?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/watch?v=your-video-id)

## 📌 Project: Collection Manipulator

## 🎯 Objective
Create a Python program called **Student Data Organizer** that manages a
collection of student records. This project applies intermediate-level
Python concepts such as **string formatting and manipulation**, **collection
data types** (List, Tuple, Set, and Dictionary), **mutability and
immutability**, **type casting**, and the **`del`** keyword.

---

## ✅ Requirements

### String Formatting and Manipulation
- Gather and store student information (name, age, grade, and subjects) using `input()`.
- Format the information for display in a user-friendly way.
- Demonstrate different string formatting methods (f-strings, `.format()`, or `%` formatting).

### Collection Data Types
| Type | Purpose |
|------|---------|
| **List** | Store multiple student records |
| **Tuple** | Store each student's unique, unchangeable info (ID, date of birth) |
| **Set** | Manage and display unique subjects offered (no duplicates) |
| **Dictionary** | Organize student data — keys are student IDs, values are dictionaries with name, age, grade, subjects |

### Mutability and Immutability
- Demonstrate the **mutability** of a List by adding or modifying student details.
- Use the **immutability** of a Tuple to store each student's ID and date of birth.

### Type Casting and `del` Keyword
- Perform type casting where needed (e.g., converting input strings to integers/floats).
- Use the `del` keyword to delete a student record from the main list based on student ID.

---

## 🔄 Program Flow

1. **Welcome and Instructions**
   - Display a welcome message and an overview of the program's functionality.

2. **Student Data Collection**
   - Prompt the user for: name, age, grade, subjects (comma-separated), student ID, and date of birth.
   - Store ID and date of birth as a tuple, add subjects to a set, and store the
     student's info in a dictionary. Add this dictionary to the list of all student records.

3. **Menu-Driven Options**
   - **Add Student** — Add a new student record.
   - **Display All Students** — Show all records (ID, name, age, grade, subjects).
   - **Update Student Information** — Update mutable info (age, subjects) by ID.
   - **Delete Student** — Remove a student record by ID using `del`.
   - **Display Subjects Offered** — Show all unique subjects using a set.

4. **Exit Message**
   - Thank the user and display an exit message.

---

## Output of Code
<img width="610" height="826" alt="image" src="https://github.com/user-attachments/assets/49c7e3eb-1180-4c3c-be3c-4fe59a57feba" />
<img width="1528" height="739" alt="image" src="https://github.com/user-attachments/assets/4e5f3b2c-e4cc-44b3-924f-e2881253b2f8" />
<img width="574" height="570" alt="image" src="https://github.com/user-attachments/assets/87ad708b-43b1-4964-bc3c-f71f0aefb8fc" />


