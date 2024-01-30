from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

def list_departments():
    print_separator()
    print("Departments:")
    print("------------")
    print(" ")
    for i, department in enumerate(Department.get_all(), start=1):
        print(f'{i}. {department.name}')
    print_separator()

def pick_department():
    list_departments()
    print(" ")
    print("Enter number of department from list above:")
    number = input("> ")
    try:
        department = Department.get_all()[int(number)-1]
        print_separator()
        print(f'You have selected {department.name}!')
        print(f"It's location is {department.location}")
        print(' ')
        return department
    except Exception:
        print("No department found")

def find_department_by_name():
    print(" ")
    print("Enter name of department you are looking for:")
    name = input("> ")
    try:
        department = Department.find_by_name(name)
        print(f'{department.name} has been found!')
        print(f"It's location is {department.location}")
        return department
    except Exception:
        print("No department found by that name")


def create_department():
    name = input("Department name:  ")
    location = input("Location:  ")
    Department.create(name, location)
    list_departments()

def update_department():
    list_departments()
    print(" ")
    print("Select number of department to update from list above:")
    num = input("> ")
    department = Department.get_all()[int(num) - 1]
    name_input = input(f"Enter name for {department.name}'s to change or hit <enter> to leave it as is: ")
    if name_input != '':
        department.name = name_input
    location_input = input(f"Enter location for {department.name}'s location to change or hit <enter> to leave it as is: ")
    if location_input != '':
        department.location = location_input
    try:
        department.update()
        print(f'{department.name} has been updated!')
        return department
    except Exception as exc:
        print("Error updating department: ", exc)

    list_departments()

def delete_department():
    list_departments()
    print(" ")
    print("Select number of department to delete from list above:")
    num = input("> ")
    department = Department.get_all()[int(num) - 1]
    department.delete()
    list_departments()

def print_separator():
    print(' ')
    print("****************")
    print(' ')

def create_employee(department):
    name = input("Employee name:  ")
    title = input("Job Title:  ")
    Employee.create(name, title, department.id)
    list_department_employees(department)

def update_employee(employee):
    name_input = input(f"Enter name to change or hit <enter> to leave it as is: ")
    if name_input != '':
        employee.name = name_input
    title_input = input(f"Enter title to change or hit <enter> to leave it as is: ")
    if title_input != '':
        employee.job_title = title_input
    try:
        employee.update()
        print(f'{employee.name} has been updated!')
        return employee
    except Exception as exc:
        print("Error updating employee: ", exc)

def delete_employee(employee):
    employee.delete()


def list_department_employees(department):
    print(f"Employees of {department.name}:")
    print("------------")
    print(" ")
    for i, employee in enumerate(department.employees(), start=1):
        print(f'{i}. {employee.name}')
    print_separator()

def pick_employee(department):
    print(" ")
    print("Enter number of employee from list above:")
    num = input("> ")
    try:
        employee = department.employees()[int(num) - 1]
        print_separator()
        print(f'Department: {department.name}')
        print(f'Name: {employee.name}')
        print(f'Title: {employee.job_title}')
        return employee
    except Exception:
        print("No Employee found")

