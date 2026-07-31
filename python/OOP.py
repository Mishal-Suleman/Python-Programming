#source tree
#Git
#VS Extension


# class Car:
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color
#         self.engine = 'xxx'

# class Student:
#     def __init__(self, name, rollnum, age):
#         self.name = name
#         self.rollnum = rollnum
#         self.age = age
#         self.department= 'Computer Science'

# class Rectangle:
#     def __init__(self, length, width):
#         self.length=length
#         self.width=width
#     def Area(self):
#         self.area= self.length*self.width
#         return self.area
#     def perimeter(self):
#         self.p=2*(self.length+self.width)
#         return self.p
        
# my_car = Car("Tesla", "Red")
# print('Brand :',my_car.brand, '\nColor :', my_car.color ,'\nEngine :', my_car.engine)
# stud=Student('Mishal', 'bsf23006511', 21)
# print('Name :', stud.name, '\nRoll no :', stud.rollnum, '\nage :',stud.age, '\nDepartment :', stud.department)
# r=Rectangle(5,2)
# print('Area :', r.Area(), '\nPerimeter :', r.perimeter())


# salaries = {
# 	'python': { 'junior': '100k', 'senior': '600k' },
# 	'php': { 'junior': '70k', 'senior': '400k' },
# 	'java': { 'junior': '80k', 'senior': '500k' },
# 	}
# print(salaries['php']['senior'])

def grade(s):
    A ,B, C, D, F =0, 0, 0, 0, 0
    for i in range(len(s)):
        if s[i]<=100 and s[i] > 90:
            A=A+1
        if s[i]<=90 and s[i] > 80:
            B=B+1
        if s[i]<=80 and s[i] > 70:
            C=C+1
        if s[i]<=70 and s[i] > 60: 
            D=D+1
        if s[i]<60 :
            F=F+1
    return A , B, C, D, F
s=[92, 85, 76, 58, 89, 91, 73, 84, 83]
print(grade(s))

with open("example1.txt", "r") as file1:
    FileContent = file1.read()
    print(FileContent)

with open("example1.txt", "w") as file1:
    print(file1.write("This is new file"))