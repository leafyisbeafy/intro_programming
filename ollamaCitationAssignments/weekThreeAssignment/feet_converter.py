# File Name: feet_converter.py
# Program Date: October 19, 2024
# Author: Osh
# Description: This program converts a length in feet to centimeters, inches, and meters, and displays the results in a formatted table.

# Define all hard-coded strings and layout widths as variables
program_title = "*** Feet Conversion Program ***"
feet_prompt = "Please enter the length in feet: "
cm_header = "CENTIMETERS"
inches_header = "INCHES"
meters_header = "METERS"
table_name = "Conversion Results"
program_complete = "Program complete."
table_width = 80
col1_width = int(table_width * .3)
col2_width = int(table_width * .3)
col3_width = int(table_width * .3)

# Display program title
print(f"{program_title}\n")

# Prompt the user for input
try:
    feet = float(input(feet_prompt))
    # Conversion calculations
    centimeters = feet * 30.48
    inches = feet * 12
    meters = feet * 0.3048

    # Format the results to include commas and up to three decimal places
    centimeters = f'{centimeters:,.3f}'
    inches = f'{inches:,.3f}'
    meters = f'{meters:,.3f}'

    # Display column titles
    print(f'\n{table_name}')
    print("-" * table_width)
    # Use :< to left align, use :^ to center align, use :> to right align
    print(f"| {cm_header:^{col1_width}} | {inches_header:^{col2_width}} | {meters_header:^{col3_width}} |")
    print("-" * table_width)
    print(f"| {centimeters:>{col1_width}} | {inches:>{col2_width}} | {meters:>{col3_width}} |")
    print("-" * table_width)

except ValueError:
    print("\nError: Please enter a valid number for the length in feet.\n")

# Print program complete message
print(f'\n{program_complete}\n')
