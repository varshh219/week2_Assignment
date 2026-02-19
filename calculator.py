
def calculate_grade(marks):
    """
    Function to calculate grade based on marks
    """
    if 90 <= marks <= 100:
        return "A", "Excellent work! Keep shining! 🌟"
    elif 80 <= marks <= 89:
        return "B", "Very Good! Keep it up! 👍"
    elif 70 <= marks <= 79:
        return "C", "Good job! You can do even better! 😊"
    elif 60 <= marks <= 69:
        return "D", "Don't give up! Work a little harder! 💪"
    else:
        return "F", "Keep trying! Success is coming! 📚"


def get_valid_marks():
    """
    Function to validate marks input (0-100 only)
    Uses while loop for error handling
    """
    while True:
        try:
            marks = int(input("Enter marks (0-100): "))
            
            if 0 <= marks <= 100:
                return marks
            else:
                print("❌ Invalid input! Marks must be between 0 and 100.")
        
        except ValueError:
            print("❌ Invalid input! Please enter numeric value only.")


def main():
    print("📊 STUDENT GRADE CALCULATOR ")
    print("-" * 35)

    name = input("Enter student name: ").upper()
    marks = get_valid_marks()

    grade, message = calculate_grade(marks)

    print("\n📊 RESULT FOR", name)
    print("-" * 35)
    print("Marks:", marks, "/100")
    print("Grade:", grade)
    print("Message:", message)


# Run program
main()
