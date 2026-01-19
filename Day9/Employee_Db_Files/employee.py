# import os

# FILE = "employees.txt"

# def add_employee():
#     emp_id = input("Enter Employee ID: ")
#     name = input("Enter Name: ")
#     salary = input("Enter Salary: ")

#     with open(FILE, "a") as f:
#         f.write(f"{emp_id},{name},{salary}\n")

#     print("Employee added successfully!")

# def view_employees():
#     if not os.path.exists(FILE): # checking the file is availble or not 
#         print("No employee records found!")
#         return

#     with open(FILE, "r") as f:
#         data = f.read()
#         print("\n=== All Employees ===")
#         print(data)

# def search_employee():
#     emp_id = input("Enter Employee ID to search: ")

#     if not os.path.exists(FILE):
#         print("No data found!")
#         return

#     with open(FILE, "r") as f:
#         for line in f:
#             if line.startswith(emp_id + ","):
#                 print("Record Found:", line)
#                 return
#     print("Employee not found!")

# def delete_employee():
#     emp_id = input("Enter Employee ID to delete: ")

#     if not os.path.exists(FILE):
#         print("No data found!")
#         return

#     with open(FILE, "r") as f:
#         lines = f.readlines()

#     found = False   # flag

#     with open(FILE, "w") as f:
#         for line in lines:
#             if line.startswith(emp_id + ","):
#                 found = True     # mark found
#                 continue         # skip writing this line (delete)
#             f.write(line)

#     if found:
#         print("Employee deleted successfully!")
#     else:
#         print("Employee ID not found. No records deleted.")


# def menu():
#     while True:
#         print("\n==== Employee Management ====")
#         print("1. Add Employee")
#         print("2. View All Employees")
#         print("3. Search Employee")
#         print("4. Delete Employee")
#         print("5. Exit")

#         choice = input("Enter choice: ")

#         if choice == "1":
#             add_employee()
#         elif choice == "2":
#             view_employees()
#         elif choice == "3":
#             search_employee()
#         elif choice == "4":
#             delete_employee()
#         else:
#             break

# menu()

import os
from datetime import datetime

FILE = "employees.txt"
LOG_FILE = "log.txt"

# Logging function
def log_action(action):
    time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{time_stamp}] {action}\n")


def add_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    salary = input("Enter Salary: ")

    with open(FILE, "a") as f:
        f.write(f"{emp_id},{name},{salary}\n")

    print("Employee added successfully!")
    log_action(f"ADD: {emp_id},{name},{salary}")


def view_employees():
    if not os.path.exists(FILE):
        print("No employee records found!")
        log_action("VIEW FAILED: employees.txt not found")
        return

    with open(FILE, "r") as f:
        data = f.read()
        print("\n=== All Employees ===")
        print(data)

    log_action("VIEW: Displayed all employees")


def search_employee():
    emp_id = input("Enter Employee ID to search: ")

    if not os.path.exists(FILE):
        print("No data found!")
        log_action("SEARCH FAILED: File missing")
        return

    with open(FILE, "r") as f:
        for line in f:
            if line.startswith(emp_id + ","):
                print("Record Found:", line)
                log_action(f"SEARCH SUCCESS: {emp_id}")
                return

    print("Employee not found!")
    log_action(f"SEARCH FAILED: {emp_id}")


def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")

    if not os.path.exists(FILE):
        print("No data found!")
        log_action("DELETE FAILED: File missing")
        return

    with open(FILE, "r") as f:
        lines = f.readlines()

    found = False

    with open(FILE, "w") as f:
        for line in lines:
            if line.startswith(emp_id + ","):
                found = True
                continue
            f.write(line)

    if found:
        print("Employee deleted successfully!")
        log_action(f"DELETE SUCCESS: {emp_id}")
    else:
        print("Employee ID not found. No records deleted.")
        log_action(f"DELETE FAILED: {emp_id} not found")


def menu():
    while True:
        print("\n==== Employee Management ====")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search Employee")
        print("4. Delete Employee")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            delete_employee()
        else:
            log_action("PROGRAM EXITED")
            break

menu()
