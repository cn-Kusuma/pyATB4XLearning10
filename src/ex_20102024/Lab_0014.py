n1 = int(input("Enter FIrst Number "))
n2 = int(input("Enter Second Number "))
n3 = int(input("Enter Third Number "))

if n1 > n2 and n1 > n3:
    print("Biggest number:", n1)

elif n2 > n3:
    print("Biggest number:", n2)

else:
    print("Biggest number:", n3)
