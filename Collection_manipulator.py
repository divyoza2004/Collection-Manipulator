print("Welcome! Let's get your student data organized.")

# Initialize an empty student dictionary so the program doesn't crash if options 2, 3, or 4 are run first
student = {}

while True:
    print("\nSelect your mode:")
    print("1. Add student information")
    print("2. Displays all student information")
    print("3. Update student information") 
    print("4. Delete student information")
    print("5. Display subject Offered") 
    print("6. Exit")
    
    # Check if input is a valid number to prevent standard crashes
    choice_input = input("Enter your choice: ")
    if choice_input.isdigit():
        x = int(choice_input)
    else:
        print("Error: Please enter a valid number.")
        continue
    
    match x:
        case 1:
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
            student = {
                "id" : result[0],
                "name" : name,
                "age" : age,
                "grade" : grade,
                "dob" : result[1],
                "subject" : subject
            }
            print("\nStudent Info Added Successfully")
            
        case 2:
            # First verify if the dictionary has data inside it
            if not student: 
                print("Student Information not found")
            else:
                new_id = input("Enter your id: ")
                if student["id"] == new_id:
                    print('\nStudent Information Details')
                    print(f"Student Id: {student['id']} | Student Name: {student['name']} | Student Age: {student['age']} | Student Grade: {student['grade']} | Student DOB: {student['dob']} | Student Subjects: {student['subject']}") 
                else:
                    print("Student Information not found")
                
        case 3:
            if not student:
                print("No student record exists to update.")
            else:
                new_id1 = input("Enter your id: ")
                if student["id"] == new_id1:
                    student["age"] = input("Enter your age: ")
                    student["subject"] = input("Enter your subjects: ")
                    print("\nStudent Information Updated Successfully")
                else: 
                    print("Id does not match")
                    
        case 4:
            if not student:
                print("No student record exists to delete.")
            else:
                new_id2 = input("Enter your id: ")  
                if student["id"] == new_id2:
                    del student 
                    student = {}
                    print("Delete student information successfully.") 
                else:
                    print("Id does not match")
                    
        case 5:
            print("\n--- Subjects Offered ---")
            print("Mathematics, Science, English, History, Computer Science")
                    
        case 6:
            print("Session closed, Goodbye") 
            break
            
        case _:
            print("Error: Invalid user input")
            break