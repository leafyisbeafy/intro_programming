# python_learning_plan.py

"""
Python Learning Plan: Employee Data Scripts

1. Variables and Data Types
   - Learn about strings, integers, and floats
   - Practice variable assignment
   - Understand Python naming conventions

2. Input and Output Basics
   - Master the print() function
   - Learn to use input() for user data

3. String Manipulation
   - Practice string concatenation
   - Explore basic string methods

4. Type Conversion
   - Convert between strings and numbers
   - Understand when and why to use type conversion

5. F-Strings
   - Learn basic f-string syntax
   - Practice embedding variables in strings

6. Importing Modules
   - Understand the import statement
   - Explore the locale module for formatting

7. Advanced String Formatting
   - Master alignment and width specification
   - Use format specifiers for different data types

8. Basic Arithmetic
   - Practice simple calculations in Python

9. Control Flow Basics
   - Understand sequential execution
   - Introduction to if statements and loops (for future expansion)

10. Console UI Design
    - Design user-friendly command-line interfaces
    - Practice clear and informative output formatting

Project Ideas:
1. Create a simple employee database
2. Build a salary calculator
3. Develop a formatted report generator

# Example implementations for each topic:

# 1. Variables and Data Types
employee_name = "John Doe"  # String
employee_age = 30  # Integer
employee_salary = 50000.0  # Float

# 2. Input and Output Basics
print("Welcome to the Employee Management System")
user_input = input("Please enter your name: ")

# 3. String Manipulation
full_name = "Doe, John"
first_name = full_name.split(", ")[1]

# 4. Type Conversion
salary_input = input("Enter salary: ")
salary = float(salary_input)

# 5. F-Strings
print(f"Employee {employee_name} is {employee_age} years old.")

# 6. Importing Modules
import locale
locale.setlocale(locale.LC_ALL, '')

# 7. Advanced String Formatting
formatted_salary = locale.currency(salary, grouping=True)
print(f"{'Name':<20}{'Age':^10}{'Salary':>15}")
print(f"{employee_name:<20}{employee_age:^10}{formatted_salary:>15}")

# 8. Basic Arithmetic
bonus = salary * 0.1
total_compensation = salary + bonus

# 9. Control Flow Basics
if salary > 60000:
    print("High earner")
else:
    print("Standard earner")

# 10. Console UI Design
def display_menu():
    print("\n1. Add Employee")
    print("2. View Employee")
    print("3. Exit")
    return input("Select an option: ")

# Main program structure
def main():
    while True:
        choice = display_menu()
        if choice == '3':
            print("Thank you for using the Employee Management System.")
            break
        # Add more functionality here

if __name__ == "__main__":
    main()
"""

# You can add actual code here to test concepts or implement the project ideas
