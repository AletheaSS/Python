age = int(input("Type your age: "))

if age >=18 and age<=70:
    print("Mandatory vote!!")
elif age >70 or (age<18 and age>=16):
    print("Optional vote!!")
else:
    print("Don't vote!!")
