from helpers import (
    exit_program,
    list_departments,
    pick_department,
    create_department,
    update_department,
    delete_department,
    create_employee,
    update_employee,
    delete_employee,
    list_department_employees,
    pick_employee
)

def main():
    list_departments()
    while True:
        departments_menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_departments()
        elif choice == "2":
            department = pick_department()
            department_selections(department)
        elif choice == "3":
            create_department()
        elif choice == "4":
            update_department()
        elif choice == "5":
            delete_department()
        else:
            print("Invalid choice")


def departments_menu():
    print(" ")
    print("Please select an option:")
    print(" ")
    print("0. Exit the program")
    print("1. List all departments")
    print("2. Select a department to see details")
    print("3: Create department")
    print("4: Update department")
    print("5: Delete department")

def department_selections(department):
    while True:
        list_department_employees(department)
        employees_menu(department)
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_department_employees(department)
        elif choice == "2":
            employee = pick_employee(department)
            employee_selections(employee)
        elif choice == "3":
            create_employee(department)
        elif choice == "4":
            main()

def employees_menu(department): 
    print(" ")
    print("Please select an option:")
    print(" ")
    print("0. Exit the program")  
    print(f"1. List all employees of {department.name}")
    print(f"2. Select a {department.name} employee from the list above to see details")
    print(f"3. Add new employee to {department.name}")
    print(f"4: Go back to list of departments")

def employee_selections(employee):
    while True:
        employee_menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            update_employee(employee)
        elif choice == "2":
            delete_employee(employee)
        elif choice == "3":
            department_selections(employee.department())

def employee_menu(): 
    print(" ")
    print("Please select an option:")
    print(" ")
    print("0. Exit the program")  
    print(f"1. Update employee")
    print(f"2: Delete employee")
    print(f"3: Go back to list of employees")

if __name__ == "__main__":
    main()
