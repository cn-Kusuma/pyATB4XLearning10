#Grade Calculator

score = int(input("Enter your score"))

if score>=90 and score<=100:
    print("grade is A")
elif score>=80 and score<=89:
    print("grade is B")
elif score>=70 and score<=79:
    print("grade is C")
elif score>=60 and score<=69:
    print("grade is D")
else:
    print("grade is F")