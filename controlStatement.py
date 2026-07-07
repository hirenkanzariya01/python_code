marks = int(input("Enter Your Marks:- "))

if marks < 33:
    print("You Are Fail")
elif marks >= 33 and marks < 50:
    print("Gread D")
elif marks >= 50 and marks < 70:
    print("Gread C")
elif marks >= 70 and marks < 80:
    print("Gread B")
elif marks >= 80 and marks < 90:
    print("Gread A")
elif marks >= 90 and marks <= 100:
    print("Gread A+")
else:
    print('Provide Valid Marks ')