#Student Record Manager
# Name: JAY MANGUKIYA
# PRN: 26070122272
# Batch: CSE C3
student_data = {}

print("\nWelcome to student data program.")
while True:
	print("\n\n_________________________________")
	print("choose an option (1-4)?")
	print("1 - Add new student record\n2 - Display "
		  "students whose avg marks is above 80\n3 - Update "
		  "marks for a specific roll no.\n4 - Exit")
	choice = int(input("(1, 2, 3, 4): "))

	if choice == 1:
		rno = int(input("\nPlease enter a roll number .: "))
		
		if rno in student_data:
			print("\nRoll number already exists.")

			continue
		name = input("enter the student's name: ")
		m1 = int(input("enter the first marks: "))
		m2 = int(input("enter the second marks: "))
		m3 = int(input("enter the third marks: "))
		m4 = int(input("enter the fourth marks: "))
		m5 = int(input("Penter the fifth marks: "))
		student_data[rno] = (name, [m1, m2, m3, m4, m5])

	elif choice == 2:
		for student in student_data:
			marks = student_data[student][1]
			avg = sum(marks) / 5

			if avg > 80:
				print("Student :", student_data[student][0], "" "roll number :", 
					student,"has average marks of", str(avg) + ".")

	elif choice == 3:
		rno = int(input("Please provide the roll number: "))

		if rno in student_data:
			print("provide all 5 marks to update:")
			m1 = int(input("enter the first marks: "))
			m2 = int(input("enter the second marks: "))
			m3 = int(input("enter the third marks: "))
			m4 = int(input("enter the fourth marks: "))
			m5 = int(input("enter the fifth marks: "))
			student_data[rno] = (student_data[rno][0], [m1, m2, m3, m4, m5])

		else:
			print("Roll number doesn't exist.")

	else:
		print("Invalid choice. Exiting.")
		break