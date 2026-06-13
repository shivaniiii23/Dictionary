"""
4.

=========================================
STUDENT GRADE ANALYSIS
======================

Store student marks in a dictionary.

students = {
"Ajay":78,
"Ravi":92,
"Neha":85,
"Aman":65
}

Write a program to:

* Find the student with highest marks.
* Find the student with lowest marks.

Sample Output:
Highest Marks : Ravi 92
Lowest Marks : Aman 65

---
"""


students = {
"Ajay":78,
"Ravi":92,
"Neha":85,
"Aman":65
}
print(students)
sort = sorted(students.items())
print(sort)

h_name,h_marks = sort[-1]
l_name,l_marks = sort[0]
print("Highest Marks",h_name,h_marks)
print("lowest Marks",l_name,l_marks)

        

       
"""
students = {
"Ajay":78,
"Ravi":92,
"Neha":85,
"Aman":65
}
print(students)
li = list(students.items())[0]
h_k,h_v = li
l_k,l_v = li
for name , marks in students.items():
    if marks >h_v:
        h_k,h_v = name,marks
    if marks <l_v:
        l_k,l_k = name,marks
print("highest Marks:",h_k,h_v)
print("Lowest Marks:",l_k,l_v)        
        
"""        

        
       
