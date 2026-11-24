#selection control flow
#Electricity Bill
unit =int(input("Enter the unit"))
if(unit>=0 and unit<=100):
    rate=2
elif(unit>100 and unit<=200):
    rate=3
else:
    rate=5
total = unit*rate
print("Total:",total)

#Largest of three number

a=int(input("Enter the a:"))
b=int(input("Enter the b:"))
c=int(input("Enter the c:"))

if(a>=b and a>=c):
    print("A is largest number",a)
elif(b>=a and b>=c):
    print("B is largest number",b)
else:
    print("C is largest number",c)

#grade calculator

m1=int(input("Enter mark 1:"))
m2=int(input("Enter mark 2:"))
m3=int(input("Enter mark 3:"))
m4=int(input("Enter mark 4:"))
m5=int(input("Enter mark 5:"))
total = m1+m2+m3+m4+m5
avg=total/5

if(avg>=90 and avg <=100):
    print("Grade A")
elif(avg>=80 and avg<90):
    print("grade B")
elif(avg>=70 and avg<80):
    print("Grade C")
elif(avg>=60 and avg<70):
    print("grade D")
elif(avg>=0 and avg<60):
    print(Fail)
#ATM Withdrawal

bal=int(input("Enter your balance:"))
amount=int(input("Enter withdrawal amount:"))
if(amount%100==0 and amount>0):
    if(amount<=bal):
        bal=bal-amount
        print("withdrawal success!")
        print("bal:",bal)
    else:
        print("Insufficient balance")
else:
    print("invalid amount")
#Triangle type
a=int(input("Enter the a:"))
b=int(input("Enter the b:"))
c=int(input("Enter the c:"))

if(a+b>c and a+c>b and b+c>a):
    if(a==b and b==c):
        print("equilateral")
    elif(a==b or b==c or a==c):
        print("Isosceles")
    else:
        print("scalene")
#for loop
#multiple with condition
for i in range(1,101):
    if(i%3==0 and i%5==0):
        print("python java")
    elif(i%3==0):
        print("python")
    elif(i%5==0):
        print("java")
    else:
        print(i)
        
#even number
n=int(input("enter n"))
for i in range(1,n+1):
    if(i%2==0):
        print(i)
        
#odd number
n=int(input("enter n"))
for i in range(1,n+1):
    if(i%2!=0):
        print(i)
        
#multiplication table
n=int(input("enter the number"))
for i in range (1,11):
    print(n,"X",i,"=",n*i)
    
#digit sum using for loop
n = input("Enter a number: ")
total = 0
for i in n:
    total = total + int(i)
print("Sum of digits:", total)

#count vowel and consonants
text = input("Enter a string: ")
v=0
c=0
for ch in text:
    if ch in "aeiouAEIOU":
        v=v+1
    else:
        c=c+1
print("Vowels:",v)
print("Consonants:",c)

#hellow square
for i in range(5):
    for j in range (5):
        if(i==0 or i==4 or j==0 or j==4):
            print("*",end="")
        else:
            print(" ",end="")
    print()

#number triangle

for i in range(6):
    for j in range(1,i+1):
        print(j,end="")
    print()

#inverse triangle
for i in range (5,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()

#lowercase to upper case
string=input("Enter a lower case")
result=""
for ch in string:
    if 'a'<=ch<='z':
        result =result+chr(ord(ch)-32)
    else:
        result=result+ch
print(result)
#count char
string=input("Enter string")
ch=input("enter char")
count=0
for i in string:
    if i==ch:
        count =count+1
print(count)

#remove dulpicate
string=input("Enter string")

result=""
for i in string:
    if i not in result:
        result =result+i
print(result)

#reverse string

string=input("enter string")
result=""
for i in range (len(string)-1,-1,-1):
     result =result+string[i]
print(result)

#login system

set_username = "admin"
set_password = "12345"
for i in range(3):
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == set_username and password == set_password:
        print("Login Successful")
        break
else:
    print("Account Locked")

#factorial

n=int(input("enter the number"))
temp=n
total=0
while temp>0:
    digit=temp%10
    fact=1
    for i in range (1,digit+1):
        fact=fact*i
    total =total+fact
    temp=temp//10
if(total==n):
    print("factorial")
else:
    print("not factorial")

