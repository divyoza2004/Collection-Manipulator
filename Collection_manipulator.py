print("Welcome! Let's get your student data organized.")
students = {}
subjects_set = set()
while True:
    print("\nSelect your mode:")
    print("1. Add student information")
    print("2. Displays all student information")
    print("3. Update student information")
    print("4. Delete student information")
    print("5. Display subject Offered")
    print("6. Exit")
    x = input("Enter your choice: ")
    match x:
        case "1":
            print("-"*40)
            print('\tEnter Student Details')
            print('-'*40)
            id = input("Enter Student id: ")
            name = input("Enter Student Name: ")
            age = input("Enter Student Age: ")
            grade = input("Enter Blood Group: ")
            dob = input("Enter Student DOB: ")
            subject = input("Enter subject: ")
            result = (id, dob)
            students[id] = {
                "id" : result[0],
                "name" : name,
                "age" : age,
                "grade" : grade,
                "dob" : result[1],
                "subject" : subject
            }
            subjects_set.add(subject)
            print("\nStudent Info Added Successfully")
            
        case "2":
            if not students:
                print("Student Information not found")
            else:
                new_id = input("Enter your id: ")
                if new_id in students:
                    current_student = students[new_id]
                    print('\nStudent Information Details')
                    print(f"Student Id: {current_student['id']} | Student Name: {current_student['name']} | Student Age: {current_student['age']} | Student Grade: {current_student['grade']} | Student DOB: {current_student['dob']} | Student Subjects: {current_student['subject']}")
                else:
                    print("Student Information not found")
                    
        case "3":
            if not students:
                print("No student record exists to update.")
            else:
                new_id1 = input("Enter your id: ")
                if new_id1 in students:
                    students[new_id1]["age"] = input("Enter your age: ")
                    new_subject = input("Enter your subjects: ")
                    students[new_id1]["subject"] = new_subject
                    subjects_set.add(new_subject)
                    
                    print("\nStudent Information Updated Successfully")
                else:
                    print("Id does not match")
                    
        case "4":
            if not students:
                print("No student record exists to delete.")
            else:
                new_id2 = input("Enter your id: ")
                if new_id2 in students:
                    del students[new_id2]
                    print("Delete student information successfully.")
                else:
                    print("Id does not match")
                    
        case "5":
            print("\n--- Subjects Offered ---")
            if not subjects_set:
                print("No subjects have been registered yet.")
            else:
                print(subjects_set)
                
        case "6":
            print("Session closed, Goodbye")
            break
            
        case _:
            print("Error: Invalid user input")
            break
