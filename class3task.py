students = []
while True:
    print("\nEnter Student Details")
    name = input("Student Name: ")
    roll_no = input("Roll Number: ")

    while True:
        math = input("Enter marks obtained in Math: ")
        if math.isdigit() and 0 <= int(math) <= 100:
            math = int(math)
            break
        else:
            print("Please enter valid numeric marks between 0 and 100.")

    while True:
        physics = input("Enter marks obtained in Physics: ")
        if physics.isdigit() and 0 <= int(physics) <= 100:
            physics = int(physics)
            break
        else:
            print("Please enter valid numeric marks between 0 and 100.")

    while True:
        urdu = input("Enter marks obtained in Urdu: ")
        if urdu.isdigit() and 0 <= int(urdu) <= 100:
            urdu = int(urdu)
            break
        else:
            print("Please enter valid numeric marks between 0 and 100.")

    while True:
        english = input("Enter marks obtained in English: ")
        if english.isdigit() and 0 <= int(english) <= 100:
            english = int(english)
            break
        else:
            print("Please enter valid numeric marks between 0 and 100.")

    while True:
        computer = input("Enter marks obtained in Computer: ")
        if computer.isdigit() and 0 <= int(computer) <= 100:
            computer = int(computer)
            break
        else:
            print("Please enter valid numeric marks between 0 and 100.")

    total = math + physics + urdu + english + computer
    percentage = total / 5

    if percentage >= 80:
        grade = "A+"
    elif percentage >= 70:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    elif percentage >= 40:
        grade = "F"
    else:
        grade = "Fail"

    student = {
        'Name': name,
        'Roll Number': roll_no,
        'Math': math,
        'Physics': physics,
        'Urdu': urdu,
        'English': english,
        'Computer': computer,
        'Total': total,
        'Percentage': percentage,
        'Grade': grade
    }
    students.append(student)

    print(f"\nRecord of {name} inserted successfully.")
    choice = input("To make more Students Report Cards? Press 'Y' for Yes or 'N' for No: ")
    if choice.upper() != 'Y':
        break

print("\n***** Report Cards *****\n")
for student in students:
    print(f"Name: {student['Name']}")
    print(f"Roll Number: {student['Roll Number']}")
    print(f"Math: {student['Math']}")
    print(f"Physics: {student['Physics']}")
    print(f"Urdu: {student['Urdu']}")
    print(f"English: {student['English']}")
    print(f"Computer: {student['Computer']}")
    print(f"Total Marks: {student['Total']}")
    print(f"Percentage: {student['Percentage']:.2f}%")
    print(f"Grade: {student['Grade']}")
    print("-" * 30)

print("\nAll report cards generated successfully!")