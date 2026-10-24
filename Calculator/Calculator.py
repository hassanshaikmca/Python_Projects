num1 =float(input("enter 1st number: "))
opertor =input("enter operator (+,-,*,/): ")
num2 =float(input("enter 2nd number: "))

if opertor == "+":
    print("results: ", num1 + num2)

elif opertor == "-":
    print("results: ",num1-num2)
elif opertor == "*":
    print("results: ",num1*num2)
elif opertor == "/":
    if num2 != 0:
        print("results: ",num1/num2)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("invalid operator")

