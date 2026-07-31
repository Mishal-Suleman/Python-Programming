
# import sys

# def add(*n):
#     sum=0
#     for i in n:
#         sum= sum+int(i)
#         return sum
# print("sum of arguments is :", add(*sys.argv[1:]))


# cube=lambda num: num**3
# print(cube(3))

# mul=lambda a,b,c: a*b*c
# sum=lambda a,b,c: a+b+c
# min=lambda a,b,c: a-b-c

# def calculator(op, a , b, c):
#     return op(a, b, c)

# print(calculator(mul,2, 3, 2))
# print(calculator(sum,4,5,2))
# print(calculator(min,2,3,4))

# print(calculator(lambda a,b,c: a*b*c,2, 3, 2))

# l=[2,3,4,5]
# n=[]
# for i in l:
#     n.append(i**2)
# print(n)

# sqr=lambda x:x**2
# sl=map(sqr,l)
# ml=list(sl)
# print(ml)

# s=["mishal suleman"]
# up=map(lambda x:x.upper(), s)
# capital=list(up)
# print(capital)

# l2=[4,5,6]
# result=map(lambda a, b: a+b, l, l2)
# result=list(result)
# print("Sum of lists :", result)

# ch=['a','f','c','e']
# vowels=['a','e','i','o','u']
# result1=filter(lambda x: x in vowels, ch)
# result1=list(result1)
# print(result1)

# from functools import reduce
# numbers=[3,4,5,6]
# num=reduce(lambda x,y:x+y, numbers)
# print(num)

#EXCEPTION HANDLING
# try:
#     #cnic=int(input("Enter your 13 digit CNIC :"))
#     #print(" REGISTERED !")
#     import sys
# except Exception as e:
#       print("Exception occured :", e)
# except ModuleNotFoundError:
#      print("Module error occured and found")
# else: 
#      print("No exception found code is good to go :)")
# finally:
#      print("Yeahhh You handled it smoothly")

# #Exercise question
# def sav_division(x,y):
#     try:
#      c=x/y
#      return c
#     except ZeroDivisionError:
#         print("division by zero not allowed")    
# a=int(input("Enter Numinator :"))
# b=int(input("Enter Denominator :"))
# print(sav_division(a,b))

def sqr(n):
    sqr_root=n*(1/2)
    return sqr_root
try: 
    n=input('Enter your number :')
    n=float(n)
    if n<0:
        print("Negative Value ")
    else:
        print(sqr(n))
except ValueError:
    print("Enter only digit")


def min(n):
    s=n/(n-5)
    return s
try: 
    n=input('Enter your number :')
    n=float(n)
    if n<0:
        print("Negative Value ")
    else:
        print(min(n))
except Exception as e:
    print("Enter only digit")