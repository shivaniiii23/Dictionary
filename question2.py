"""2.

ASSIGNMENT: ONLINE COURSE ENROLLMENT & STUDENT MANAGEMENT SYSTEM

A training institute offers multiple courses such as Python, Java, Full Stack Development, Data Science, and React.

Currently, student enrollment details are maintained manually in Excel sheets. As the number of students is increasing, the institute wants to develop a Student Management System using Python.

The system should store student records in a nested dictionary where:

Key → Student ID
Value → Dictionary containing student information

Each student record should contain:

Student Name
Course Name
Mobile Number
Fees
City
Sample Data Structure
{
101:{
    "name":"Ajay",
    "course":"Python",
    "mobile":"9876543210",
    "fees":25000,
    "city":"Indore"
},
102:{
    "name":"Ravi",
    "course":"Java",
    "mobile":"9876500000",
    "fees":22000,
    "city":"Bhopal"
}
}
Menu Driven Program

Display the following menu repeatedly until the user chooses Exit.

=========================================
 STUDENT MANAGEMENT SYSTEM
=========================================

1. Add New Student
2. Search Student
3. Update Course
4. Delete Student
5. Display All Students
6. Count Total Students
7. Display Students By Course
8. Display Students By City
9. Find Student Paying Highest Fees
10. Find Student Paying Lowest Fees
11. Exit
Functional Requirements
1. Add New Student

Accept the following details:

Student ID
Student Name
Course Name
Mobile Number
Fees
City

Store the information in the nested dictionary.

Validation

If Student ID already exists:

Student ID Already Exists
2. Search Student

Accept Student ID from the user.

If found, display complete student information.

Sample Output
Student ID : 101
Name       : Ajay
Course     : Python
Mobile     : 9876543210
Fees       : 25000
City       : Indore

If not found:

Student Not Found
3. Update Course

Accept Student ID.

If found:

Ask for new course name.
Update the course.
Sample Output
Course Updated Successfully
4. Delete Student

Accept Student ID.

If found:

Delete the record.
Sample Output
Student Deleted Successfully

Otherwise:

Student Not Found
5. Display All Students

Display all student records in a proper format.

Sample Output
-----------------------------------
Student ID : 101
Name       : Ajay
Course     : Python
Fees       : 25000
-----------------------------------

Student ID : 102
Name       : Ravi
Course     : Java
Fees       : 22000
-----------------------------------
6. Count Total Students

Display total number of students enrolled.

Sample Output
Total Students : 45
7. Display Students By Course

Accept a course name from the user.

Display all students enrolled in that course.

Sample Output
Enter Course : Python

101  Ajay
105  Neha
112  Aman

If no students are found:

No Students Found
8. Display Students By City

Accept city name from the user.

Display all students belonging to that city.

Sample Output
Enter City : Indore

101  Ajay
108  Ravi
115  Pooja
9. Find Student Paying Highest Fees

Display complete details of the student who has paid the highest fees.

Sample Output
Highest Fee Paying Student

Student ID : 121
Name       : Neha
Course     : Data Science
Fees       : 50000
10. Find Student Paying Lowest Fees

Display complete details of the student who has paid the lowest fees.

Sample Output
Lowest Fee Paying Student

Student ID : 131
Name       : Aman
Course     : React
Fees       : 15000
11. Exit

Terminate the application.

Sample Output
Thank You For Using Student Management System

--
"""
d = {}
while True:
    print("=========================================")
    print("STUDENT MANAGEMENT SYSTEM")
    print("=========================================")

    print("1. Add New Student")
    print("2. Search Student")
    print("3. Update Course")
    print("4. Delete Student")
    print("5. Display All Students")
    print("6. Count Total Students")
    print("7. Display Students By Course")
    print("8. Display Students By City")
    print("9. Find Student Paying Highest Fees")
    print("10. Find Student Paying Lowest Fees")
    print("11. Exit")
    choice = int(input("enter you choice"))
    match choice:
        case 1:
            s_id = int(input("entr the student id"))
            if s_id in d:
                print("id is already exit")
            else:
                name = input("enter the name")
                course = input("ente the course")
                mobile =  input("enter the mobile")               
                fees = input("enter the fees")
                city = input("enter the city")
                d[s_id] = {
                   "name" : name,
                   "course" : course,
                   "mobile":mobile,
                   "fees" : fees,
                   "city":city
                }
        case 2:
            s_id = int(input("entr the student id"))
            if s_id in d:
                p =d[s_id]     
                print("student  id :",s_id )
                print("Name : ",p["name"])
                print("course : ",p["course"])                  
                print("mobile : ",p["mobile"]) 
                print("fees : ",p["fees"])
                print("city : ",p["city"])
            else:
                print("student not found")
        case 3:
            s_id = int(input("entr the student id"))
            if s_id in d:        
                new_course = input("enetr the course")
                d[s_id]["course"] = new_course
                print("course updated successfully")
            else:
                print("id not founds")
        case 4:
            s_id = int(input("entr the student id"))
            if s_id in d: 
                del d[s_id]
                print("id deleted successfully")
            else:
                print("Student not found")
        case 5:
            if not  d:
                print("no recored find")
            else:
                for  sid,s in d.items():
                    print("---------------------------------------")
                    print("student id",s_id)
                    print("Name :",s["name"])
                    print("course :",s["course"])
                    print("fees :",s["fees"])
        case 6:
            print("length of the list is:",len(d))
        case 7:
            course = input("Enter Course: ")
            found = False
            for sid, s in d.items():
                if s["course"].lower() == course.lower():
                     print(sid, s["name"])
                     found = True
            if not found:
                print("No Students Found")        
        case 8:
            city = input("Enter City: ")
            found = False
            for sid, s in d.items():
                if s["city"].lower() == city.lower():
                     print(sid, s["name"])
                     found = True
            if not found:
                print("No Students Found")  
        case 9:
            if d:
                highest_id = max(d, key=lambda x: d[x]["fees"])
                s = d[highest_id]
                print("\nHighest Fee Paying Student")
                print("Student ID :", highest_id)
                print("Name       :", s["name"])
                print("Course     :", s["course"])
                print("Fees       :", s["fees"])
            else:
                print("No Student Records Found")
        case 10:
            if d:
                lowest_id = min(d, key=lambda x: d[x]["fees"])
                s = d[lowest_id]
                print("\nLowest Fee Paying Student")
                print("Student ID :", lowest_id)
                print("Name       :", s["name"])
                print("Course     :", s["course"])
                print("Fees       :", s["fees"])
            else:
                print("No Student Records Found") 
        case 11:
            print("Thank You For Using Student Management System")
            break  
                    
               