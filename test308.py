name = input("Enter student name: ")
math = float(input("Enter Math marks: "))
english = float(input("Enter English marks: "))
python = float(input("Enter Python marks: "))


if math < 0 or math > 100 or english < 0 or english > 100 or python < 0 or python > 100:
    print("Invalid marks!")

else:
    average = (math + english + python) / 3


    if average >= 80:
        grade = "A+"    

    elif average >= 70 and average <= 79:
        grade = "A"   

    elif average >= 60 and average <= 69:
        grade = "A-"    

    elif average >= 50 and average <= 59:
        grade = "B"   

    elif average >= 40 and average <= 49:
        grade = "C"   

    else:
        grade = "F"


    print(f"Student Name:{name}")
    print(f"Average Marks:{average}")
    print(f"Final Grade: {grade}")