print("=" * 60)
print("          STUDENT RESULT MANAGEMENT SYSTEM")
print("=" * 60)

name = input("Enter Student Name : ")
class_name = input("Enter Class : ")
exam_name = input("Enter Exam Name : ")

print("\nEnter Subject Details")
print("-" * 60)

sub1 = input("Enter Subject 1 Name : ")
sub1_marks = int(input(f"Enter {sub1} Marks : "))

sub2 = input("Enter Subject 2 Name : ")
sub2_marks = int(input(f"Enter {sub2} Marks : "))

sub3 = input("Enter Subject 3 Name : ")
sub3_marks = int(input(f"Enter {sub3} Marks : "))

sub4 = input("Enter Subject 4 Name : ")
sub4_marks = int(input(f"Enter {sub4} Marks : "))

sub5 = input("Enter Subject 5 Name : ")
sub5_marks = int(input(f"Enter {sub5} Marks : "))

# Total and Percentage
obtain_marks = sub1_marks + sub2_marks + sub3_marks + sub4_marks + sub5_marks
total_marks = 500
pr = (obtain_marks / total_marks) * 100

# Result
if pr >= 30:
    result = "PASS"
else:
    result = "FAIL"

# Grade
if pr >= 90:
    grade = "A+"
elif pr >= 80:
    grade = "A"
elif pr >= 70:
    grade = "B"
elif pr >= 50:
    grade = "C"
elif pr >= 30:
    grade = "D"
else:
    grade = "E"

# Print Result
print("\n")
print("=" * 65)
print("                  STUDENT MARKSHEET")
print("=" * 65)

print(f"Student Name : {name}")
print(f"Class        : {class_name}")
print(f"Exam Name    : {exam_name}")

print("-" * 65)
print(f"{'Subject':<30}{'Marks':>10}{'Out Of':>15}")
print("-" * 65)

print(f"{sub1:<30}{sub1_marks:>10}{100:>15}")
print(f"{sub2:<30}{sub2_marks:>10}{100:>15}")
print(f"{sub3:<30}{sub3_marks:>10}{100:>15}")
print(f"{sub4:<30}{sub4_marks:>10}{100:>15}")
print(f"{sub5:<30}{sub5_marks:>10}{100:>15}")

print("-" * 65)

print(f"{'Total Marks':<30}{obtain_marks:>10}{500:>15}")
print(f"{'Percentage':<30}{pr:>9.2f}%")
print(f"{'Grade':<30}{grade}")
print(f"{'Result':<30}{result}")

print("=" * 65)