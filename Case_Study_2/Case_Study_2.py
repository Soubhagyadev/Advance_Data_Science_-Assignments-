"""
Problem Statement:
A hospital wants to automate its patient appointment and department management process. 
Develop a Python program that accepts patient details such as patient name, requested departments, 
available departments, previously visited departments, preferred doctors, available doctors, 
and emergency departments. Using Python lists and sets, identify available departments, common departments, unavailable departments, duplicate requests, previously visited departments, and departments requiring immediate attention. The program should use list and set operations such as indexing, slicing, adding, removing, union, intersection, difference, and membership checking. The program should use only core Python without NumPy, Pandas, datasets, or external libraries.

Expected Outcome:
The program should generate a final appointment report showing the patient's requested departments, 
available departments, unavailable departments, common departments, previous departments, 
emergency departments, recommended department, and final appointment status. The results should change dynamically based on different patient and hospital inputs.
"""

patient_name = input("Enter patient name: ")

requested_dept = input("Enter requested departments: ").split(",")
requested_dept = [d.strip() for d in requested_dept]

available_dept = input("Enter available departments: ").split(",")
available_dept = [d.strip() for d in available_dept]

previous_dept = input("Enter previously visited departments: ").split(",")
previous_dept = [d.strip() for d in previous_dept]

preferred_doctors = input("Enter preferred doctors: ").split(",")
preferred_doctors = [d.strip() for d in preferred_doctors]

available_doctors = input("Enter available doctors: ").split(",")
available_doctors = [d.strip() for d in available_doctors]

emergency_dept = input("Enter emergency departments: ").split(",")
emergency_dept = [d.strip() for d in emergency_dept]

#So According To The Question We Need To Slice It?
first_requested = requested_dept[0]
last_requested = requested_dept[-1]
top_departments = requested_dept[:3]

requested_dept.append("General Medicine")
if "General Medicine" in available_dept:
    available_dept.remove("General Medicine")
    available_dept.insert(0, "General Medicine")

requested_set = set(requested_dept)
available_set = set(available_dept)
previous_set = set(previous_dept)
emergency_set = set(emergency_dept)
preferred_set = set(preferred_doctors)
available_doc_set = set(available_doctors)

common_dept = requested_set.intersection(available_set)
unavailable_dept = requested_set.difference(available_set)
all_dept = requested_set.union(available_set)
duplicate_requests = len(requested_dept) - len(requested_set)
revisiting_dept = requested_set.intersection(previous_set)
immediate_attention = requested_set.intersection(emergency_set)
matching_doctors = preferred_set.intersection(available_doc_set)

recommended = None
for dept in requested_dept:
    if dept in available_set and dept in emergency_set:
        recommended = dept
        break
if recommended is None:
    for dept in requested_dept:
        if dept in available_set:
            recommended = dept
            break

if common_dept:
    status = "Confirmed"
elif immediate_attention:
    status = "Emergency"
else:
    status = "Pending"

report = [
    ("Patient Name", patient_name),
    ("First Requested", first_requested),
    ("Last Requested", last_requested),
    ("Top 3 Departments", top_departments),
    ("Requested Depts", requested_dept),
    ("Available Depts", available_dept),
    ("Common Depts", common_dept),
    ("Unavailable Depts", unavailable_dept),
    ("All Depts (Union)", all_dept),
    ("Duplicate Requests", duplicate_requests),
    ("Revisiting Depts", revisiting_dept),
    ("Emergency Depts", immediate_attention),
    ("Previous Depts", previous_set),
    ("Preferred Doctors", preferred_set),
    ("Available Doctors", available_doc_set),
    ("Matching Doctors", matching_doctors),
    ("Recommended Dept", recommended),
    ("Appointment Status", status)
]

print("=" * 50)
print("HOSPITAL APPOINTMENT REPORT")
print("=" * 50)
for label, value in report:
    print(label + " : " + str(value))
print("=" * 50)
