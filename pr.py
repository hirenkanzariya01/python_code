print("=" * 60)
print("          GUJARAT UNIVERSITY")
print("=" * 60)

collage_name = input("Enter the name of your collage:-")
course = input("Enter your course:-")
group = input("Enter your group:-")

print("\nEnter personal Details")
print("-" * 60)

name = input("Enter your Name:-")
class_name = input("Enter your class name:-")
exam_name = input("Enter your exam name:-")

print("\nEnter Subject Details")
print("-" * 60)

Sub1 = input("Enter your sub1 name:-")
sub1_marks = int(input(f"Enter your {Sub1} Marks"))

Sub2 = input("Enter your sub2 name:-")
sub2_marks = int(input(f"Enter your {Sub2} Marks"))

Sub3 = input("Enter your sub3 name:-")
sub3_marks = int(input(f"Enter your {Sub3} Marks"))

Sub4 = input("Enter your sub4 name:-")
sub4_marks = int(input(f"Enter your {Sub4} Marks"))

Sub5 = input("Enter your sub5 name:-")
sub5_marks = int(input(f"Enter your {Sub5} Marks"))

# Total marks
obtain_marks = sub1_marks + sub2_marks + sub3_marks + sub4_marks + sub5_marks
total_marks = 500
pr = (obtain_marks * 100) / 500
grade = ""
result = ''
# result
if pr >= 30:
    print("PASS!")
    result = "PASS"
else:
    print("FAIL!")
    result = 'FAIL'

# grade
if pr > 90:
    print("A1")
    grade = "A1"
elif pr > 80 and pr < 90:
    print("A")
    grade = "A"
elif pr > 70 and pr < 60:
    print("B")
    grade = "B"

elif pr > 60 and pr < 50:
    print("C")
    grade = "C"
elif pr > 50 and pr < 30:
    print("D")
    grade = "D"
else:
    print("E")
    grade = 'E'
    
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

print(f"{Sub1:<30}{sub1_marks:>10}{100:>15}")
print(f"{Sub2:<30}{sub2_marks:>10}{100:>15}")
print(f"{Sub3:<30}{sub3_marks:>10}{100:>15}")
print(f"{Sub4:<30}{sub4_marks:>10}{100:>15}")
print(f"{Sub5:<30}{sub5_marks:>10}{100:>15}")

print("-" * 65)

print(f"{'Total Marks':<30}{obtain_marks:>10}{500:>15}")
print(f"{'Percentage':<30}{pr:>9.2f}%")
print(f"{'Grade':<30}{grade}")
print(f"{'Result':<30}{result}")

print("=" * 65)
