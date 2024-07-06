a = int(input("Enter a number:"))
b = int(input("Enter another number:"))
print("Type 1)Addition\n2)Subtraction\n3)Multiplication\4)Division\n5)Modulus\n6)Exit")
c = input("Enter your choice:")
if c== '1':
    sum = a + b
    print("Addition of a and b =",sum)
elif c== '2':
    diff = a - b
    print("Difference of a and b = ",diff)
elif c== '3':
    mul = a * b
    print("Multiplication of a and b = ",mul)
elif c== '4':
    if b != 0:
     div = a / b
     print("Division of a and b = ",div)
elif c== '5':
    mod = a % b
    print("Modulus of a and b = ",mod)
elif c== '6':
    exit