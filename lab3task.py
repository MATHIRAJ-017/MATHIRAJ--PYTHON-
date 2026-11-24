# #easy
# #List
# list=["apple","banana","orange","apple"]
# print(list)
# list.append("banana")
# print(list)
# list.extend(["grape","mango"])
# print(list)
# list.insert(2,"grape")
# print(list)
# list.pop(2)
# print(list)
# list.clear()
# print(list)
#median
# print(list.index("apple"))
# print(list.count("apple"))
# list.sort()
# print(list)
# list.sort(reverse=True)
# print(list)
# list.reverse()
# print(list)
# list1=["kavin","kalai","mani"]
# list.extend(list1)
# print(list)

# #Tuple
# #Easy
# tuple2=(2,4,2,7,6,6,8)
# tuple1=(1,2,3,4,5,7,9)
# print(tuple)
# i=int(input("Enter a number:"))
# print(tuple.index(i))
# print(tuple.count(i))
# print("first element",tuple[0])
# print("middle element",tuple[len(tuple)//2])
# print("last element",tuple[-1])
# print(tuple[::-1])
# #Median
# t3=tuple2 + tuple1
# print(t3)
# res=((tuple2,)*3)
# print(res)
# t4=(set(tuple2)&set(tuple1))
# print(t4)
# even=tuple(x for x in tuple1 if x%2==0)
# print(even)
# odd=tuple(x for x in tuple1 if x%2!=0)
# print(odd)

# #Set
# #easy
# set={2,4,3,5,6,4,3,7,4,8}
# print(set)
# set.add(10)
# print(set)
# set.update({21,11})
# print(set)
# set.remove(10)
# print(set)
# set.discard(2)
# print(set)
# set.pop()
# print(set)
# set.clear()
# print(set)
# #Median
# set1={1,2,3,4,5,6}
# set2={3,4,5,6}
# print(set1.union(set2))
# print(set1.intersection(set2))
# print(set1.difference(set2))
# print(set1.symmetric_difference(set2))
# print(set2.issubset(set1))
# print(set1.issuperset(set2))
# print(set1.isdisjoint(set2))
# #dictionary
# #easy
# dic={1:"apple",2:"banana",3:"mango"}
# print(dic)
# print(dic.get(1))
# print(dic.keys())
# print(dic.values())
# print(dic.items())
# dic.update({4:"orange"})
# print(dic)
# dic.update({3:"pineapple"})
# print(dic)

# #median
# dic.pop(1)
# print(dic)
# dic.popitem()
# print(dic)
# dic.update({4:"orange"})
# print(dic)
# dic.setdefault(1)
# print(dic)
# dic1=dic.copy()
# print(dic1)
# #slicing
# a="hello welcome"
# print(a[:6])
# print(a[-5:])
# print(a[::-1])
# print(a[::2])
# print(a[2:7])
# mid=len(a)//2
# print("first half",a[:mid])
# print("second half",a[mid:])
# rotate=(a[-2:]+a[:-2])
# print(rotate)

numbers=[10,25,45,30,15]
largest=0
second=0
for num in numbers:
    if num>largest:
        second=largest
        largest=num
    elif num>second and num!=largest:
        second=num
print("Second largest number:",second)

number=[1,2,3,2,4,5,1,3]
duplicate=[]
for num in number:
    if numbers.count(num)>1 and num not in duplicate:
        duplicate.append(num)
print("Duplicate elements:",duplicate)

number=[10,20,30,40,50,60]
rotate=number[3:]+number[:3]
print(rotate)

number=[1,2,3,2,4,5,1,3]
nondup=[]
for num in number:
    if num not in nondup:
        nondup.append(num)
print("without dup",nondup)

#tuple hard
numbers=[10,25,45,30,15]
largest=0
second=0
third=0
for num in numbers:
    if num>largest:
        third=second
        second=largest
        largest=num
    elif num>second:
        third=second
        second=num
    elif num>third:
        third=num
print("third largest number:",third)

t1=(4,2,8)
t2=(1,9,6)
merge=tuple(sorted(t1+t2))
print(merge)

t=(10,20,30,60,40,50)
element=int(input("remove element:"))
temp=list(t)
temp.remove(element)
t=tuple(temp)
print(t)
#set hard

s1={1,2,3,4,5}
s2={3,4,5,6,7}
s3={2,3,4,5}
common=s1&s2&s3
print(common)

s1={1,2,3,4,5}
s2={3,4,5,6,7}
for num in s2:
    s1.add(num)
print(s1)

num=[1,2,2,3,4,5,6,7,7,8,9]
uni=list(set(num))
print(uni)

subjects=["Tamil","English","Maths","Science","Social"]
marks=dict.fromkeys(subjects, 0)
print(marks)

sentence="i am iron man"
words=sentence.split()
freq={}
for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1
print("Word frequency:",freq)

students={"kavin": 85,"mathi": 90,"Kumar": 75,"Ravi": 95,"kalai": 80}
topper=max(students, key=students.get)
print("Topper:",topper)
print("Highest mark:",students[topper])

inventory = {"Pen": 10,"Book": 20,"Pencil": 15}
inventory["Eraser"] = 5
inventory["Pen"] = 25
del inventory["Pencil"]
for product, quantity in inventory.items():
    print(product, ":", quantity)
