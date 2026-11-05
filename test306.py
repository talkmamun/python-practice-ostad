name = input("Enter student name: ")

print()

math_marks = float(input("Enter Math marks: "))
english_marks = float(input("Enter English marks: "))
python_marks = float(input("Enter Python marks: "))


if not (0 <= math_marks <= 100 and 0 <= english_marks <= 100 and 0 <= python_marks <= 100):
    print("\nError: Invalid marks! Marks must be between 0 and 100.")
else:


    
    average_marks = (math_marks + english_marks + python_marks) / 3


    if average_marks >= 80:
        grade = "A+"
    elif average_marks >= 70:
        grade = "A"
    elif average_marks >= 60:
        grade = "A-"
    elif average_marks >= 50:
        grade = "B"
    elif average_marks >= 40:
        grade = "C"
    else:
        grade = "F"

    print()

    
    print(f"Student Name: {name}")
    print(f"Average Marks: {average_marks:.2f}")
    print(f"Final Grade: {grade}")

