a=20
b=10
c=30
d=40
e=50
a1=5
a2=3
#Arithmetic operators
print("addition:",a+b)
print("difference:",a-b)
print("product:",a*b)
print("div:",a/b)
print("mod:",a%b)
print("floor:",a//b)
print("square:",a1**a2)
total=a+b+c+d+e
print("total:",total)
print("avg",total/5)
print("last 2 digit:",121793%100)
print("last 3 digit",157390//1000)
#Assignment operators
a=100
b=20
print("a=",a)
a+=50
print("+= operator:",a)
a-=20
print("-= operator:",a)
a*=5
print("*= operator:",a)
a/=2
print("/ operator:",a)
a%=b
print("%= operator:",a)
a**=2
print("**= operator:",a)
#Comparison operators
a=int(input("Enter a:"))
b=int(input("Enter b:"))
print("a Equal to b:",a==b)
print("a Not equal to b:",a!=b)
#the bigger of two number
if a>b:
    print("a is biggest number :",a)
else:
    print("b is biggest number :",b)
#eligible for voting
age=int(input("enter the age:"))
if age>=18:
    print("eligilbe for voting")
#student passed
mark=int(input("Enter the mark:"))
if mark>=35:
    print("pass")
a=int(input("enter a:"))
if (a>=1 and a<=100):
    print("The number between 1 to 100")
#logical operators

a=int(input("enter a:"))
if(a>0 and a%2==0):
    print("a number is positive and even")
    
age=int(input("enter the age:"))
id=input("id(yes/no):")
if(age>=18 and id=="yes"):
    print("eligible to vote")
    
mark1=int(input("enter mark1:"))
mark2=int(input("enter mark2:"))
if(mark1>=35 or mark2>=35):
    print("student passed")
    
a=int(input("enter a:"))
if(a>=10 and a<=50):
    print("number between 10 and 50")

a=int(input("enter a:"))
if(not a==0):
    print("the number is not equal to zero")
#membership operator
name="mathi"
if('a' in name):
    print("letter a is present")

lang=["python","java","c++","c"]
if("python" in lang):
    print("present")

num=[10,20,30,40,50]
n=int(input("enter n:"))
if (n in num):
    print("Number exist in a list")

string="mathi"
char='r'
if (char not in string):
    print ("char not presebt in string")
#Identify operator
a="mathi"
b="mathi"
if(a is b):
    print("same")

a=[10,20,30]
b=[10,20,30]
if (a is b):
    print("same list value.")
else:
    print("not same list value.")

a=[10,20,30]
b=a
if(a is b):
    print("same")

a=[10,20,30]
b=[10,20,30]
if (a is not b):
    print("not same list value.")
else:
    print("same list value.")

#Bitwise operator
a=10
b=5
print("AND",a&b)
print("OR",a|b)
print("XOR",a^b)
print("NOT",~a)

#real time task
name=input("Enter the student name:")
m1=int(input("Enter mark 1:"))
m2=int(input("Enter mark 2:"))
m3=int(input("Enter mark 3:"))
m4=int(input("Enter mark 4:"))
m5=int(input("Enter mark 5:"))
total = m1+m2+m3+m4+m5
avg=total/5

print("student name:",name)
print("Total:",total)
print("average:",avg)
if(avg>=35):
    print("pass")
else:
    print("Fail")

unit=int(input("enter the unit:"))
rate=int(input("enter the rate:"))
bill= unit * rate
print("bill:",bill)

product =int(input("Enter the price:"))
quantity=int(input("Enter the quantity:"))
total = product * quantity
if(total>=1000):
    dis=total*10/100
else:
    dis=0
amount=total-dis
print("total",total)
print("discount",dis)
print("final amount",amount)


age=int(input("enter the age:"))
if age>=18:
    print("eligilbe for voting")

name=input("Enter the username:")
password=input("Enter the password")
if(name =="admin" and password =="12345"):
    print("login successfully!")

number =int(input("Enter the number"))
if(number %2==0):
    print("Even number")
else:
    print("odd number")

a=int(input("Enter the a:"))
b=int(input("Enter the b:"))
c=int(input("Enter the c:"))

if(a>=b and a>=c):
    print("A is largest number",a)
elif(b>=a and b>=c):
    print("B is largest number",b)
else:
    print("C is largest number",c)
