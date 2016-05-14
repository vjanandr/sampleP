#!/usr/bin/python3
class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__ (self, name, salary):
         Employee.empCount+=1
         self.name = name
         self.salary = salary

    def displayCount (self):
        print("Number of registered Employees :",Employees.empCount)

    def displayEmployeeDetails (self):
        print("Employee name :",self.name)
        print("Employee Salary:",self.salary)

#This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
#This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
emp1.displayEmployeeDetails()
emp2.displayEmployeeDetails()
print ("Total Employee %d" % Employee.empCount)
