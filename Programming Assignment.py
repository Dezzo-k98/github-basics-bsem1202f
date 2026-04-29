# Getting the total classes available

while True:
    try:
        TOTAL_CLASSES = int(input('Enter total number of classes: '))

        if TOTAL_CLASSES <= 0:
            print("Total classes must be greater than 0")
            continue
        break

    except:
        print("only numbers are allowed")




# Function to calculate attendance percentage
def calculate_percentage(attended):
    percentage = (attended / TOTAL_CLASSES) * 100
    return percentage


# Function to check if student is eligible
def check_eligibility(percentage):
    if percentage >= 75:
        return "Eligible"
    else:
        return "Not Eligible"


# Variable used to control loop
running = True


# Main program starts here
while running:

    # Program title
    print("The Attendance Tracking System")

    # Input student name
    name = input("Enter student name: ").strip()

    # Check if name is empty
    if name == "":
        print("Space for name cannot be empty")
        continue

    # Check if name contains only letters
    if not name.replace(" ", "").isalpha():
        print("The names written must contain letters only")
        continue

    try:
        # Input number of attended classes
        attended = int(input("Enter number of classes attended: "))

    except:
        print("Only numbers are allowed")
        continue

    # Check valid class range
    if attended < 0 or attended > TOTAL_CLASSES:
        print("Classes must be between 0 and", TOTAL_CLASSES)
        continue

    # Calculate results
    percentage = calculate_percentage(attended)
    status = check_eligibility(percentage)

    # Display output
    print("Attendance Record")
    print("Student Name:", name)
    print("Classes Attended:", attended)
    print("Percentage:", percentage)
    print("Status:", status)

    # Menu options
    print("\n1. Do you want to record another attendance record?")
    print("2. Exit")

    choice = input("Select option: ")

    if choice == "1":
        continue
    else:
        print ("attendance record ended")
        running = False

