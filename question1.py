"""1.ASSIGNMENT: HOSPITAL PATIENT RECORD MANAGEMENT SYSTEM:--

A multi-specialty hospital is currently maintaining patient records manually in registers. As the number of patients is increasing, it has become difficult to search, update, and manage records efficiently.

The hospital management has decided to develop a simple Patient Record Management System using Python. The system should store patient information in a nested dictionary where:

Key → Patient ID
Value → Dictionary containing patient details

Each patient record should contain:

Patient Name
Age
Gender
Disease
Doctor Name
Sample Data Structure
{
101:{
    "name":"Ajay",
    "age":35,
    "gender":"Male",
    "disease":"Fever",
    "doctor":"Dr. Sharma"
},
102:{
    "name":"Ravi",
    "age":42,
    "gender":"Male",
    "disease":"Diabetes",
    "doctor":"Dr. Gupta"
}
}
Menu Driven Program

Display the following menu repeatedly until the user chooses Exit.

=====================================
 HOSPITAL PATIENT MANAGEMENT SYSTEM
=====================================

1. Add New Patient
2. Search Patient
3. Update Patient Disease
4. Delete Patient Record
5. Display All Patients
6. Count Total Patients
7. Display Patients By Disease
8. Display Oldest Patient
9. Display Youngest Patient
10. Exit

Functional Requirements
1. Add New Patient

Accept the following information from the user:

Patient ID
Patient Name
Age
Gender
Disease
Doctor Name

Store the record in the nested dictionary.

Validation:
If the Patient ID already exists, display:

Patient ID already exists.

2. Search Patient

Accept Patient ID from the user.

If the patient exists, display complete information.

Sample Output

Patient ID : 101
Name       : Ajay
Age        : 35
Gender     : Male
Disease    : Fever
Doctor     : Dr. Sharma

If Patient ID is not found:

Patient Record Not Found

3. Update Patient Disease

Accept Patient ID.

If found:

Ask for new disease.
Update the disease information.

Sample Output

Disease Updated Successfully
4. Delete Patient Record

Accept Patient ID.

If found:

Remove the patient record.

Sample Output

Patient Record Deleted Successfully

Otherwise:

Patient Not Found
5. Display All Patients

Display all patient records in a formatted manner.

Sample Output

--------------------------------
Patient ID : 101
Name       : Ajay
Age        : 35
Disease    : Fever
Doctor     : Dr. Sharma
--------------------------------

Patient ID : 102
Name       : Ravi
Age        : 42
Disease    : Diabetes
Doctor     : Dr. Gupta
6. Count Total Patients

Display the total number of patients currently stored.

Sample Output

Total Patients : 25
7. Display Patients By Disease

Accept a disease name from the user.

Display all patients suffering from that disease.

Sample Output

Enter Disease : Fever

101  Ajay
108  Aman
115  Neha

If no patient is found:

No Patient Found
8. Display Oldest Patient

Find and display the patient having the highest age.

Sample Output

Oldest Patient Details

Patient ID : 110
Name       : Ravi
Age        : 68
Disease    : Diabetes
Doctor     : Dr. Gupta
9. Display Youngest Patient

Find and display the patient having the minimum age.

Sample Output

Youngest Patient Details

Patient ID : 121
Name       : Riya
Age        : 4
Disease    : Viral Fever
Doctor     : Dr. Mehta
10. Exit

Terminate the application.

Sample Output

Thank You For Using Hospital Patient Management System
"""
print("=====================================")
print("HOSPITAL PATIENT MANAGEMENT SYSTEM")
print("=====================================")
d = {}
while True:
    
    print("1. Add New Patient")
    print("2. Search Patient")
    print("3. Update Patient Disease")
    print("4. Delete Patient Record")
    print("5. Display All Patients")
    print("6. Count Total Patients")
    print("7. Display Patients By Disease")
    print("8. Display Oldest Patient")
    print("9. Display Youngest Patient")
    print("10. Exit")
    choice = int(input("enter the choice"))
    match choice:
        case 1:
            patient_id = int(input("enter the patient_id"))
            if patient_id in d:
                print("patient id is alredy exits")
            else:
                name = input("enter the name:")
                age = int(input("enter the age:"))
                disease =input("enter the diesec:")
                doctor = input("enter the doctor name:")
                d[patient_id]={
                    "name" :name,
                    "age" : age,
                    "disease" :disease,
                    "doctor" :doctor
                    
                    }                    
                print("record added successfully")                
        case 2:
            p_id = int(input("enter the patient_id"))
            
            if p_id in d:
                p = d[p_id]
                print("patient_id:",p_id)
                print("name:",p["name"])
                print("age:",p["age"])
                print("disease:",p["disease"])
                print("doctor:",p["doctor"])
            else:
                print("patient id not found")            
        
        case 3:
            p_id = int(input("enter the patient_id"))
            if p_id in d:
                new_diseses = input("enter the disese")
                d[p_id]["disease"]=new_diseses
                print("disease updated successfully")
        
        case 4:
            p_id = int(input("enter the patient_id"))
            if p_id in d:
                del d[p_id] 
                print("patient deleted successfully")
            else:
                print("patient not found") 
        case 5:
            if not d:
                print("patient record not found")
            else:
                for  p_id,p in d.items():
                   print("patient id :",p_id)
                   print("Name : ",p["name"])
                   print("age: ",p["age"])
                   print("disease: ",p["disease"]) 
                   print("Docter : ",p["doctor"])
        case 6:
            print("Total number of patient",len(d))        
    
        case 7:
            disease = input("Enter Disease: ")
            found = False
            for pid, p in d.items():
                if p["disease"].lower() == disease.lower():
                    print(pid, p["name"])
                    found = True
            if not found:
                print("No Patient Found")
        case 8:
            if d:
               ages = {pid: p["age"] for pid, p in d.items()}
               oldest_id = max(ages, key=ages.get)
               p = d[oldest_id]

               print("\nOldest Patient Details")
               print("Patient ID :", oldest_id)
               print("Name       :", p["name"])
               print("Age        :", p["age"])
               print("Disease    :", p["disease"])
               print("Doctor     :", p["doctor"])
            else:
               print("No Patient Records Found")
        case 9:
            if d:
               youngest_id = min(ages, key=ages.get)
               p = d[youngest_id]

               print("\nYoungest Patient Details")
               print("Patient ID :", youngest_id)
               print("Name       :", p["name"])
               print("Age        :", p["age"])
               print("Disease    :", p["disease"])
               print("Doctor     :", p["doctor"])
            else:
               print("No Patient Records Found") 
        case 10:
            print("Exit")
            break 
        case _:
            print("invalid choice")        

