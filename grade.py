# Python code for Grading System
# By Obed Godspower Udem
# Dept: Cybersecurity
# Reg. No: 2023924002

# Grading system

user = float(input("Enter your score: "))

if user in range(70, 100):
    print("A")
elif user in range(60, 69):
    print("B")
elif user in range(50, 59):
    print("C")
elif user in range(45, 49):
    print("D")
elif user in range(40, 44):
    print("E")
else:
    print("F")
