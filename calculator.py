print("CALCULATOR-Menu driven program")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
d="yes"
while d=="yes":
    ch=int(input("Enter your choice"))
    if ch==1:
        a=int(input("Enter first number:"))
        b=int(input("Enter second number:"))
        print("Result of ",a,"+",b,"=",a+b)
    elif ch==2:
        a=int(input("Enter first number:"))
        b=int(input("Enter second number:"))
        print("Result of ",a,"-",b,"=",a-b)
    elif ch==3:
        a=int(input("Enter first number:"))
        b=int(input("Enter second number:"))
        print("Result of ",a,"*",b,"=",a*b)
    elif ch==4:
       a=int(input("Enter first number"))
       b=int(input("Enter second number"))
       if b==0:
           print("Division by zero not possible")
       else:
           print("Result of ",a,"/",b,"=",a/b)
    else:
       print("No such choice exists")
       d=input("Do you want to continue?")
       if d=="no":
           break
