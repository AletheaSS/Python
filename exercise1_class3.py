num1 = float(input("Type first number: "))
num2 = float(input("Type second number : "))
operation = str(input("Choose math operation: +, -, *, /"))

if operation == '+':
    result=num1+num2
if operation == '-':
    result=num1-num2
if operation == '*':
    result=num1*num2
if operation == '/':
    result=num1/num2

print ("The operation chosen was", operation, "and the result is:", result)

