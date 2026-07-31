'''#input a string
x=input("Enter your string: ")
#reverse 
rev=(x[::-1])
print(rev)
#check palindrome
p=bool (rev ==x)
print(p)
#find length without len()
#print(x.find[-1]+1)
#upper case letter
up=(x.upper())
print(up)
#remove spaces
no_space=(x.replace(" " , ""))
print(no_space)
#replace with #
x=x.lower()
slash=(x.replace("a","#").replace("e", '#').replace("i", '#').replace("u", '#').replace("o", '#'))
print(slash)
#max character
maximum=(max(x))
print(maximum)
#sort string alphabetically
y=sorted(x)
sort="".join(y)
print(sort)
#count length
print(len(x))
#revese the words
z=" ".join(x.split()[::-1])
print(z)
#join string
mega_string="|".join([x, rev, up, slash, no_space, sort, z, maximum])
print(mega_string)'''
'''#regex
import re   #built in module
s1="The BodyGuard is the best album"
pattern= r"Body"
result=re.search(pattern, s1)
print(result)
s2="My phone number is 1234567890"
pattern2=r"\d\d\d\d\d\d\d\d\d\d" #match 10 consective digits
match=re.search(pattern2, s2)
if match:
    print("Match found" , match.group())
else:
    print("No match")
#import re
pattern= r"\W"
text="Hello, world!"
#findall() fun finds all occurance of a specified pattern within a string
matches=re.findall(pattern, text) 
print("matches:", matches)
s2="The BodyGuard is the best album of 'whitney houston'"
pattern1= r"st"                                        #p= r"[s-t]"
match1=re.findall(pattern1, s2)
print("matches:", match1)
#re.split()
split1=re.split(r"\s", s2)
print(split1)
#sub
pattern2=r"Whitney Houston"
replacement= "legend"
s3= re.sub(pattern2, replacement, s2, flags=re.IGNORECASE)
print(s3)'''

'''d="ABCDEF"
print(d[0], d[1])
e="clocrkr1e1c1t"
print(e[::2])
print(r"")
f="YOU ARE WRONG"
print(f.lower())
g="Mary had a little lamb Little lamb, little lamb Mary had a little lamb \
Its flees was white as snow And erverywher that Mary went"
print(g.find("snow"))
p=g.replace("Mary", "Bob")
print(p)
z=p.replace(",", " . ")
print(z)
print(z.split())'''
#import re
'''s3="House number- 1105"
pattern2=r"\d" 
match=re.search(pattern2, s3)
if match:
    print("Digit found" , match.group())
else:
    print("Digit not Found")

m="The quick brown fox jumps over the lazy dog"
replacement="bear"
pattern2="fox"
s3= re.sub(pattern2, replacement, m, flags=re.IGNORECASE)
print(s3)
print(re.sub(r"fox", "bear", m, flags=re.IGNORECASE ))

str="how much wood would a woodchuck chuk, if a woodchuck could chuck wood?"
pattern= r"woo"                                        #p= r"[s-t]"
match1=re.findall(pattern, str)
print("matches:", match1)
print(re.findall(r"woo", str))

#Check karo string palindrome hai ya nahi (bina loop, sirf slicing use karke).
x=input("Enter your string: ")
rev=(x[::-1])
palindrome= bool (rev==x)
print("Is Palindrome :", palindrome)
#String ko title case mein convert karo (har word ka first letter capital).
stitle= x.title()
print(stitle)
#String ko swapcase karo (upper ko lower, lower ko upper).
scase=x.swapcase()
print(scase)
#String ke first aur last character nikaalo (ek hi expression mein).
print("firts character :",x[0], "last character :", x[-1])
#Check karo string kisi specific word se start ya end hoti hai ya nahi.
start=x.startswith("Data")
print(start)
#String ko center align karo total width 25 ke sath, extra space * se fill karo.
mid=(x.center(25, "*"))
print(mid)
#String ka middle character nikaalo (agar length even ho to do middle characters).
middle=int(len(x)/2)
print("Middle character :", x[middle])
#String mein har word ka sirf pehla letter nikaal ke jodo (initials banao) — bina loop ke.


#String ko 3 baar repeat karo aur beech mein - daalo.
y=x+ "-"
print(y*3)
#Steps 1-9 ke results ko | se join karke final mega-string banao.
result="|".join([rev, stitle, scase, mid, y ])
print(result)'''

#list================================================================
'''l1=[1,2,3]
l2=[1.2,2.2,3.2]
l3=['mishal','ghufaira','hehe']
l4=[True, False]
l5=[]
print(type(l5))
#Nested list 
nested=[1, 2.2, 'mishal', [11, 'Kiran']]
print(nested)
x = [1, 2, 3]
y = [1, 2, 3]
print(id(x), id(y), x is y, x==y)
x1 = [1, 3 , 2]
y1 = [2, 1, 3]
print(id(x1), id(y1), x1 is y1, x1==y1 )
numbers = [10, 20, 30, 40, 50]
print(numbers[2])
print(id(numbers))
numbers[2] = 555
print("numbers: ", numbers)
print(id(numbers))
#list can have duplicate value 
#we can access list element by indexing
print(nested[2][3], nested[3][1][2])
print(type(nested[1]), type(nested[3][1]))'''
#function and method of list============================
'''L=["Michael jackson", 10.1, 1982, "MJ", 1]
print(L[-1])
print(L[3:])
#concatination of list
a=[2,3]
b= [1] + a
print(b)

food_items1 = ['fruits', 'bread', 'veggies'] 
food_items2 = ['meat', 'spices', 'burger']
food = food_items1 + food_items2
final_food=food*3
print(final_food)
# We can use the slice index to modify multiple list elements in one go
mylist = ['data science', 'machine learning', 2, 5, 7]
mylist[0:2] = ['english', 'urdu'] # Note we are replacing two elements with two elements
print(mylist)

mylist[0:2]='Big Data'
print(mylist)

mylist[0]=['Computer', 23]
print(mylist)
#list method
#1: append
list1 = [2, 4, 6, 8]
#list1.append(4.631)
print(list1) 
a=list1.append([4.631,'hello'])
print(list1) 
#append fun always return none 
print(list1[4][1])
# 2: extend
list2 = [2, 4, 6, 8]
list2.extend([4.631, 'hello'])
print(list2)
# 3. insert
myfamily = ["Aqsa", 'Sana', 'Wajeeha','Basirat','Hrm']
print("\nOriginal family list: ", myfamily)
myfamily.insert(3,'Kiran')
print("After insert: ", myfamily)
# 4. pop (remove the last element and also return the value)
x=myfamily.pop(1)                   #pop() no argument means it remove last value
print("After remove: ", myfamily )
print("removed item: ", x)
myfamily.pop(-2)
print("remove negative index: ", myfamily )
# 5. remove (if we pass multiple values it only remove the first one and return none)
myfamily.remove('Aqsa')
print(myfamily)
# 6. clear (it remove the whloe list item and return empty list)
myfamily.clear()
print(myfamily)'''
# 7. split
'''str2="Data Science is GR8 Degree"
list3=str2.split()
print(list3)
# 8. join
myfamily = ["Aqsa", 'Sana', 'Wajeeha','Basirat','Hrm']
str4=' '.join(myfamily)
str3='#'.join(myfamily)
print(str4)
print(str3)
print(len(myfamily))
print(max(myfamily))
print(min(myfamily))
#Aliasing
list1 = [1, 2, 3, 4]
list2 = list1
# Both variables point to same memory object, so have the same ID
print('ID of Old List:', id(list1))
print('ID of New List:', id(list2))
list2[2] = 9

print('\nOld List:', list1)
print('New List:', list2)

#shallow copy
list2 = list1[:] #just this : add the rest remain same 

import copy
l=[5,5,6,6,7]
l2=copy.copy(l)
l2[3]='a'
print('\nOld List:', l)
print('New List:', l2)
#copy.copy has LIMITATION it dont work in nested list case
# Deep copy
old_list = [[3, 2, 9], [4, 2, 6], [7, 4, 9]]
new_list = copy.deepcopy(old_list)

# Both variables point to different memory object, having their own object elements
print('ID of Old List:', id(old_list))
print('ID of New List:', id(new_list))

new_list[2][2] = 0

print('\nOld List:', old_list)
print('New List:', new_list)
m=['s','a','m','z','q','f']
m1=[3,6,2,9,7,1,0,5]
m.sort()
print(m)
#descending
m1.sort(reverse=True)
print(m1)

#cuatom sorting
cus_sort=['ccc','aaaa','d','bb']
cus_sort.sort(key=len) #we can pas fun in the key
print(cus_sort)
def rev(s):
    return s[0]

sort2=['abcz','xyza','bas','kiran']
sort2.sort(key=rev)
print(sort2)'''

'''def lenth(s):
    """Docstring describe what a function do 
    this function takes a string and count its lenth 
    and return to the variable where funtion called"""
    c=0
    for i in s:
        c=c+1
    return c

a=input("Enter your string :")
b= lenth(a)
print("length is :", b)
print(lenth.__doc__)


def even(a):
    new=[]
    for i in a:
        if (i%2==0):
            new.append(i)
    return new

b=[2,5,4,6,81,9,34,97]
b=even(b)
print(b)'''

'''def sel_sort1(mylist):  
    for i in range(len(mylist)):
        min = i
        for j in range(i+1, len(mylist)):
            if mylist[min] > mylist[j]:
                min = j  
        mylist[i], mylist[min] = mylist[min], mylist[i]

numbers = [25,4,2,67]
rv = sel_sort1(numbers)
print("list is sorted: ", numbers)'''

def simple_bot(message):
    responses = {
        "hello": "Hi there!",
        "bye": "Goodbye!",
        "how are you": "I'm just code, but thanks for asking!",
        "python": "Python is awesome !"
    }
    message = message.lower()
    return responses.get(message, "I don't understand that.")
    
print(simple_bot(input("Please ask me anything?")))
print(simple_bot(input("Tell me about Python")))
