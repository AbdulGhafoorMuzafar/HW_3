import math
print("Which Operator Do You Want To Calculate :")
print("1 : sin")
print("2 : cos")
print("3 : tan")
print("4 : cot")
print("5 : factorial")
print("6 : sqrt")
operation = int(input())

if (operation ==1) :
    number = float (input("Please Enter Your Number :"))
    print("Sin of your number is : ") 
    print(math.sin(math.radians(number)))
if (operation == 2) :
    number = float (input("Please Enter Your Number :"))
    print("Cos Of Your Number Is :")
    print(math.cos(math.radians(number)))
if(operation == 3) :
    number = float (input("Please Enter Your Number :"))
    print("Tan Of Your Number Is :")
    print(math.tan(math.radians(number)))
if(operation == 4) :
    number = float (input("Please Enter Your Number :"))
    print("Cot Of Your Number Is :")
    print(1/math.tan(math.radians(number)))
if(operation == 5) :
    number = int (input("Please Enter Your Number :"))
    print("Factorial Of Your Number Is :")
    print(math.factorial(number))
if(operation == 6) :
    number = int (input("Please Enter Your Number :"))
    print("sqrt Of Your Number Is :")
    print(math.sqrt(number))
