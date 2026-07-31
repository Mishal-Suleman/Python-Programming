'''s1 = {1,2,3,4,5}   #set of integers
print(s1,type(s1))
s1 = set([1, 2, 3,3, 4, 5])
s1, print(s1, type(s1))
s2=([])
print(type(s2))
s3={'miss', 1, 5.3, True}
print(s3)
a = {1, 2, 3}
b = {2, 3, 1}
#add (we can add element in tuples thy are mutable but not by indexing)
#only add one element at a time
b.add((3,'4',6))
print(b)
print(id(a), id(b), a == b, a is b)
#update (pas any iterator in it means add multiple values at a time)
a.update("Miss")
print(a)
#pop() its remove any random elment
a.pop()
print(a)
#remove (if the value not find it generate error)
print(a)
a.remove('M')
print(a)
#discard (it will not through error if the value not found)
a.discard('w')
print(a)
#clear (remove all the elements present in set)
a.clear()
print(a)
#del (delete the set from memory)
c={1,2,3,4,5}
print(sum(c))
#union (|)
print(b|c)
#intersction
print(b&c)
#difference 
print(b-c)
#symmetric difference
print(b^c)
#subset
print(b<=c)
#superset
print(b>=c)
#disjoint
print(b.isdisjoint(c))
text="  data-analytics  "
msg=" H!e@l#1$o% t^h&e*re, W(O)r_l+d! 123 

for i in range(len(msg)):
    char=msg[i]
    if char.isalpha() or char==" ":
        print(char, end="")'''

#================================================================================
#Dictionary
'''info={'age': 21, 
      'age': 21,
      'gender': 'F'}
print(info)
M=dict({1:"Arsalna", 2:"Mishal", 3: "Hira", 4:"Sana"})
print(M)
#In case of same key we will get the latest updated value
d1={
    'name':'Mishal',
    'name': 'Sana'
}
print(d1)
#we cannot have mutable data types as value not as a KEY  .... 
d2 = {'kakamanna':'name', 
      'marks': [1,2,3]
     }
d2 
print(d2)

dict3 = {
    'name': 'kakamanna', 
    1: 10,
    'abc':25,
    33.4 : 'xyz'
}
print(dict3)
#Nested dictionary
dict7 = {'name':'Mishal', 
         'occupation':'Student',
        'address':{'house#' : 6, 'area' : 'xyz', 'city' : 'lahore'},
         'phone': '0300-000000'
        }
print(dict7)
#Accessing element from dic
print(dict7['address'])
# Methos
#1. get (if the value not find it will not give error and return a default value set by us)
print(dict7.get('gender', 0))
print(dict7['occupation'][2:])
print(dict7['address']['city'])
print(dict7.get('address').get('city').upper())
#2.items
print(dict7.items())
#3. key
print(dict7.keys())
#4. values
print(dict7.values())
#5. Modify value corresponding to an existing key
dict7['address'] = 'Model Town'
print(dict7)
#6. Adding a new key:value pair
dict7['gender'] = 'female'
print(dict7)
#7. Modify value corresponding to an existing key
dict7.update({'name':'Kiran Khursheed'})
dict7.update({'class': 'BSCS'})
print(dict7)
#8. del (used to remove item)
del dict7['occupation']
print(dict7)
#9. popitem (remove LIFO item)
print(dict7.popitem())
print(dict7)
#10. clear()'''

#SELECTION STRUCTURE
'''x = 2
if (x == 1): # you can put parenthesis around condition, but it is OK if you dont
    print('This will execute, only if the condition is true')
else:
    print('xyz')
print('This will always execute')
x=int(input("Enter your number : "))
if x%2==0:
    print("Even")
else: 
    print("odd")
print("byee")'''

'''a=int(input("Enter your number : "))
b=int(input("Enter your number : "))
c=int(input("Enter your number : "))
if (a>b and a>c):
    print(a, "is greatest")
elif (b>a and b>c):
    print(b, "is greatest")
else:
    print(c, "is greatest")

#ternary operator
age=int(input("Enter age :"))
p="adult" if age>=18 else 'child'
print(p)
#Nested if
age1 = int(input("Please enter your age: "))
if (age1 >= 18):
    rv = input("Do you have National ID card? Y/N: ")
    if ((rv == 'Y') or (rv == 'y')):
        print("Welcome, you can vote")
    else:
        print("Since you do not have CNIC, so you cannot vote.")
else:
    print("You are too young to vote")'''
# Pass keyword is used as a placeholder in if statement


ol=[5,3,6,2]
nl=[]

for i in ol:
    nl=i-2
    print(nl, end=" ")
    i+1
print("\n")
#List comprehension
ol1=[5,3,6,2]
nl1=[i*i for i in ol1]
print(nl1)

list1=['Aqsa', 'Sanaaa']
list2=[i[0] for i in list1]
print(list2)
list3=[len(i) for i in list1]
print(list3)
list4=[i.upper() for i in list1]
print(list4)

l=[1,9,12,88,65,7,20,55,47,32]
n=[]
for i in l:
    if i%2==0:
        n.append(i)
print(n)

l2=[3,5,6,8,3,9,39,41,34,54,67,91]
n2=[i for i in l2 if (i%2!=0)]
print(n2)
i=0
for i in range(1,100):
    if(i%3==0 and i%5==0):
        print(i)

no=[i for i in range(100) if(i%3==0 and i%5==0)]
print(no)
r=[10,-2,5,-7,5]
n3=[i if i>0 else 0 for i in r]
print(n3)

f=['apple','banana', 'cherry','kiwi']
n4=[i[::-1] for i in f]
print(n4)

p=['maam', 'banana', 'pop','sho']
n5=[i for i in p if(i==i[::-1])]
print(n5)


#dict comprehnesive
d=range(11)
dic={i:i**3 for i in d if i**3%4==0}
print(dic)

dict1={'milk':120.0, 'chocalate':45.0, 'bread':80.0}
dic2={i : dict1[i]*0.25 + dict1[i] for i in dict1}
print(dic2)

#convert roman to digits
'''n=input("Enter your number :")
a=0
b=5
for i in range(len(n)):
    if (i[0]=='I'):
        a=a+1
    elif (i[0]=='I' and i[1]=='V'):
        a=b-1
    if (i[0]=='V'):
        a=b
    else:
        a=b+1
print(a)'''

n = input("Enter your number :")
values = {'I':1, 'V':5, 'X':10}
a = 0
for i in range(len(n)):
    current = values[n[i]]
    if i+1 < len(n) and current < values[n[i+1]]:
        a=a-current
    else:
        a=a+current
print(a)

        


    
