# Grading System
# By Obed Godspower Udem
# Cybersecurity Department
# 2023924002

print("Welcome to the Obed Grading System")

def get_valid_score():
    while True:
        score_input = input("Enter score (0–100): ")
        try:
            score = float(score_input)
            if 0 <= score <= 100:
                return score
            else:
                print("Error: Score must be between 0 and 100.")
        except ValueError:
            print("Error: Please enter a valid number.")

def calculate_grade(score):
    if score >= 70:  # 70–100
        return "A"
    elif score >= 60:  # 60–69
        return "B"
    elif score >= 50:  # 50–59
        return "C"
    elif score >= 45:  # 45–49
        return "D"
    elif score >= 40:  # 40–44
        return "E"
    else:  # 0–39
        return "F"

name = input("What is your name? ").strip()
if not name:
    name = "Student"

print(f"\nHello, {name}! Enter your subjects and scores below.")

results = []

while True:
    subject = input("Enter subject name: ").strip()
    if not subject:
        print("Error: Subject name cannot be empty.")
        continue
    score = get_valid_score()
    grade = calculate_grade(score)
    results.append((subject, score, grade))
    print(f"{subject}: {score} ({grade})")
    cont = input("Add another subject? (yes/no): ").lower()
    if cont == "no":
        break

if results:
    print(f"\nGrade Summary for {name}:")
    print("-" * 50)
    print(f"{'Subject':<20} {'Score':<10} {'Grade':<10}")
    print("-" * 50)
    for subject, score, grade in results:
        print(f"{subject:<20} {score:<10.1f} {grade:<10}")
    print("-" * 50)
else:
    print("\nNo grades entered.")
print("\nThank you for using the Obed Grading System!")