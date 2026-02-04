# Grade Checker
# Take a score as input and print the grade based on the following:
# 90+ : "A"
# 80-89 : "B"
# 70-79 : "C"
# 60-69 : "D"
# Below 60 : "F"
# here we used a basic if else statement to carry out marks and all.

# a = int(input("Enter the Score : "))
# if a>=90:
#     print("Grade : A")
# elif a >= 80:
#     print("Grade : B")
# elif a>=70:
#     print("Grade : C")
# elif a>=60:
#     print("Grade : D")
# else:
#     print("Grade : F")

# 2 Student Grades
# Create a dictionary where the keys are student names and the values are their grades. Allow the user to:
# Add a new student and grade.
# Update an existing student’s grade.
# Print all student grades.

# name_grade = {"Jaikumar" : "A","Danish" : "A"}

# while True:
#     print("\n1. Add a student and grade\n2. Update a student's grade\n3. Display all the student's grade\n4. Exit\n")
#     i = int(input("Choose a number :  "))

#     if i == 1:
#     #Add the Details
#         a = input("Enter the Name of Student : ")
#         b = input("Enter the Grade of the Student : ")
#         name_grade[a] =  b
#         print("\n",name_grade)
#     elif i == 2:
#     #Update the Grade 
#         for keys in name_grade.keys():
#             print(keys)
#         a = input("\nEnter the Student Name for update : ")
#         b = input("Enter the new Grade : ")
#         name_grade[a] = b
#         print("\n",name_grade)
#     elif i == 3:
#         for key, value in name_grade.items():
#             print(f"{key}: {value} Grade")
#     elif i == 4:
#         break
#     else:
#        print("Wrong Input")

# 3.Write to a File
# Write a program to create a text file and write some content to it.

# Using file functions like write and open.


# f = open("myfile.txt","w")
# f.write("Added a new line to the text file\nHello, Hello!")
# f.close()

# a = open("myfile.txt","+r")
# print(a.read())
# a.close()