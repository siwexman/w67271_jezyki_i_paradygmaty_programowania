class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def print(self):
        return f"{self.name}, {self.age}, {self.salary}"


class EmployeesManager():
    def __init__(self):
        super().__init__()
        self.employees = []

    def addEmployee(self, employee):
        self.employees.append(employee)
        return employee.print()

    def printEmployees(self):
        for employee in self.employees:
            return employee.print()

    def removeEmployeeByAge(self, minAge, maxAge):
        removedEmployees = []

        for employee in self.employees:
            if employee.age in range(int(minAge), int(maxAge) + 1):
                removedEmployees.append(employee)
                self.employees.pop(employee)

        return removedEmployees

    def findEmployee(self, name):
        for employee in self.employees:
            if employee.name == name:
                return employee

    def updateSalary(self, name, newSalary):
        employee = self.findEmployee(name)
        employee.salary = newSalary
        return employee.print()


class FrontendManager:
    def __init__(self):
        self.manager = EmployeesManager()

    def run(self):
        while True:
            print(
                "Press number to call an action:\n1. Add new Employee\n2. Display Employees"
                "\n3. Remove Employees by age range\n4. Update salary based on surname of Employee")
            choice = input("Choose an option: ")

            if choice == '1':
                name = input("Name: ")
                age = input("Age: ")
                salary = input("Salary: ")
                newEmployee = Employee(name, age, salary)
                self.manager.addEmployee(newEmployee)
                print(f"Added: {newEmployee.print()}\n")
            elif choice == '2':
                print(self.manager.printEmployees())
            elif choice == '3':
                minAge = input("MinAge: ")
                maxAge = input("MaxAge: ")
                print(self.manager.removeEmployeeByAge(minAge, maxAge), '\n')
            elif choice == '4':
                name = input("Name: ")
                newSalary = input("New salary: ")
                print(self.manager.updateSalary(name, newSalary), '\n')
            else:
                print("Exiting...")
                break


fronted = FrontendManager()
fronted.run()
