# waist_size.py
# Program date: 2024-10-22
# Author: Oshonik
# Description: Converts waist measurements in inches to standardized sizes

# Display welcome message
print("Welcome to the Waist Size Converter")
print("Please enter the waist measurement in inches")

# Variables
waist_measurement = 0.0  # float
has_size = False  # boolean
size_name = ""  # stringto store the size name

# Input
try:
    waist_measurement = float(input("Waist measurement: "))

    # Process
    if waist_measurement < 26.7:
        print("Sorry, no sizes are available for this measurement.")
    elif waist_measurement > 38.6:
        print("Sorry, no sizes are available for this measurement.")
    else:
        # Check each size range using if/elif statements
        if waist_measurement >= 26.7 and waist_measurement <= 28.7:
            size_name = "S"
            has_size = True
        elif waist_measurement > 28.7 and waist_measurement <= 30.7:
            size_name = "M"
            has_size = True
        elif waist_measurement > 30.7 and waist_measurement <= 32.7:
            size_name = "L"
            has_size = True
        elif waist_measurement > 32.7 and waist_measurement <= 34.6:
            size_name = "XL"
            has_size = True
        elif waist_measurement > 34.6 and waist_measurement <= 36.6:
            size_name = "2XL"
            has_size = True
        elif waist_measurement > 36.6 and waist_measurement <= 38.6:
            size_name = "3XL"
            has_size = True

        # Output
        if has_size:
            print(f"The corresponding size is: {size_name}")

except ValueError:
    print("Error: Please enter a valid number.")

# Program completion message
print("\nProgram complete.")