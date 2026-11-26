#In-bulid function
string="mathiraj"
lists=[10,5,55,27,20,30,5,55,27]
x=-26
print("lentgh is string:",len(string))
print("largest of list:",max(list))
print("Smallest of list:",min(list))
print("Sum of list:",sum(list))
print("sorted list:",sorted(list))
print("Uppercase:",string.upper())
print("Lowercase:",string.lower())
v=0
for i in string:
    if i in "AEIOUaeiou":
        v+=1
print("vowel count:",v)
print("list using set to remove duplicate:",list(set(lists)))
print("absolute value:",abs(x))

#user-define function
def main(*num):
    print("sum of two number:",a+b)
main(5,6)

def main(l,b):
    print("area of rectangle:",l*b)
main(5,6)

def main(a,b,c):
    print(max(a,b,c))
main(40,5,70)

def main():
    p=int(input("enter the principle amount:"))
    n=int(input("enter the amount of money:"))
    r=int(input("enter the rate:"))
    si=(p*n*r)/100
    print("SI",si)
main()

def main():
    age=int(input("Enter the Age:"))
    if(age>=18):
        print("eligible to vote")
    else:
        print("you cant vote")
main()

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n* fact(n-1)
print(fact(5))

def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
        else:
            return True
    return True
num = int(input("Enter the number"))
if(prime(num)):
    print("Prime")
else:
    print("Not Prime")

def reverse(n):
    print("Reverse:",n[::-1])
reverse("mathiraj")

def main():
    s=input("Enter the sring:")
    if s==s[::-1]:
        print("palindrome")
    else:
        print("not is palindrome")
main()

#Recursion

def name(n):
    if n==0:
        return
    print("print")
    n=n-1
    name(n)
name(5)

def num(n):
    if n==11:
        return
    print(n)
    n=n+1
    num(n)
num(1)

def num(n):
    if n==0:
        return
    print(n)
    n=n-1
    num(n)
num(10)

def num(n):
    if n>=21:
        return
    print(n)
    n=n+2
    num(n)
num(2)

def num(n):
    if n>=20:
        return
    print(n)
    n=n+2
    num(n)
num(1)

def num(n):
    if n==0 or n==1:
        return 1
    else:
        return n+ num(n-1)
print(num(10))

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n* fact(n-1)
print(fact(5))

def main(a,n):
    if n==0:
        return 1
    else:
        return a * main(a,n-1)
print(main(2,5))

def sum(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + sum(n // 10)
n = int(input("Enter a number: "))
print(sum(n))

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
n = int(input("Enter number of terms: "))
for i in range(n):
    print(fib(i), end=" ")

#lambda
x=lambda x,y: x+y
print("Sum:",x(5,6))

x=lambda x,y: x-y
print("difference:",x(10,6))

x=lambda x,y: x*y
print("Product:",x(5,6))

x=lambda x: x**2
print("Square:",x(5))

x=lambda x: x**3
print("Cube:",x(5))

x=lambda x: "even" if x % 2 == 0 else "odd"
print("the number is odd or even:",x(5))

x=lambda x,y: x*y
print("Area of rectangle:",x(5,6))

x=lambda x,y,z: (x*y*z)/100
print("Simple interest:",x(500,60,7))

x=lambda c:(c*9/5)+32
print("c to f",x(37))

#map_function

num=[1,2,3,4,5,6,7,8]
num1=[1,2,3,4,5,6,7,8]
numbers=["10","20","30","40","50","60","70","80","90"]
lists=["Mathi","Hari","kavin","Boopathi"]
sq=list(map(lambda x:x**2,num))
print(sq)
cube=list(map(lambda x:x**3,num))
print(cube)
mul=list(map(lambda x:x*5,num))
print(mul)
add=list(map(lambda x:x+10,num))
print(add)
upper=list(map(lambda x:x.upper(),lists))
print(upper)
lower=list(map(lambda x:x.lower(),lists))
print(lower)
string=list(map(int,numbers))
print(string)
f=list(map(lambda c:(c*9/5)+32,num))
print(f)
len=list(map(len,lists))
print(len)
add=list(map(lambda x,y:x+y,num,num1))
print(add)

#filter function
num=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,-12]
nums=[45,57,87,24,50,67,11]
lists=["Mathi","Hari","ajay","ajith","kavin","Boopathi"]
even=list(filter(lambda x:x%2==0,num))
print(even)
odd=list(filter(lambda x:x%2==1,num))
print(odd)
greater=list(filter(lambda x:x>=10,num))
print(greater)
less=list(filter(lambda x:x<=50,num))
print(less)
pos=list(filter(lambda x:x>0,num))
print(pos)
neg=list(filter(lambda x:x<0,num))
print(neg)
div=list(filter(lambda x:x%5==0,num))
print(div)
starting=list(filter(lambda x:x.startswith('a'),lists))
print(starting)
counts=list(filter(lambda x:len(x)>5,lists))
print(counts)
result=list(filter(lambda x:x>50,nums))
print(result)

#challenge level

def main():
    result=lambda x:x*x
    print(result(5))
main()

num=[1,2,3,4,5,6,7,8,9]
even=list(filter(lambda x:x%2==0,num))
square=list(map(lambda x:x**2,even))
print(square)

def main():
    total =sum(marks)
    avg=total/len(marks)
    print("total marks: ",total)
    print("average marks: ",avg)
marks=[80,90,85,95,75]
main()

def main(s):
    if(len(s)==0):
        return s
    return main(s[1:])+s[0]
print(main("python"))

lists=[95,85,75,85,55]
grade=list(map(lambda x:"A" if x>=90 else "B" if x>=80 else "C" if x>=70 else "FAIL",lists))
print(grade)

emp=[25000,35000,15000,23500,55000,65000]
emps=list(filter(lambda x:x>=25000,emp))
print(emps)

lists=[("kalai", 85),("kavin", 70),("Ajay", 95),("hari", 75)]
sort=sorted(lists,key=lambda x:x[1])
print(sort)
