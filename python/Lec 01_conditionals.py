'''ans= input("What is the answer to the Great Question of Life, the Universe and Everything? ")
ans= ans.lower() 
if(ans=="42" or ans=="forty two" or ans=="forty-two"):
    print("yes")
else:
    print("No")'''
#-------------------------------------------------------------
'''greet=input("Greeting :")
greet=greet.lower()
if(greet.startswith('hello')):
    print("$0")
elif(greet.startswith('h') and greet != "hello"):
    print("$20")
else:
    print("$100")'''


'''name="Michael  \t Jackson"
statement=name + "\nis the best"
print(statement)
smile="haha:) " * 10
print(smile)
#r is used for row string
a="Mishal \\ is best"
print(a)'''


'''A="    Thriller is the sixth studio album    "
print(A.upper())
print(A.lower())
#only first letter capitalize
print(A.capitalize())
#remove spaces from start and end
print(A.strip())
#remove space from right
print(A.rstrip())
#remove space from left
print(A.lstrip())
#split the string at spaces and return as a list
print(A.split())
print(A.split(sep='i'))
#find the substring index (if the index not found it return -1)
print(A.find('sixth'))
#we can also define the starting and ending index for search the specific string
print(A.find('the', 3, 20))
#replace with new term
print(A.replace('the', 'wah'))
print(A)'''


a=20
b=4.2
a1=20.0
c=a/b
d=a//b
e=a1//b
print(c," "  , d, " "  , e)

a=15
b=27
print(id(a), " ", id(b))
a=a+12
b=27-12
print(a, " ", b)
print(id(a), " ", id(b))
x=25
y="25"
print(bool(x==y))


p=1200
discount= p* (15/100  )      #15%
discout_price= p - discount
print(discout_price)
gst=discout_price * (8/100)
final_price= discout_price +gst
print("final price =", final_price)

A= True
B= False
C= False
exactly_one= (A and not B and not C) or\
            (not A and B and not C ) or (not A and not B and C)
print(exactly_one)