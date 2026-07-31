'''msg=input("Enter your string: ")
msg= msg.lower()
print(msg)'''
#--------------------------------------------
'''msg=input("Enter your string: ")
msg= msg.replace(" ", "...")
print(msg)'''
#------------------------------------------

'''def main():
        msg= input("Enter your String :")
        output= convert(msg)
        print(output)


def convert(x):
        x= x.replace(":(" , "🙁") 
        x= x.replace(":)" , "🙂")
        return x


main()'''
#-------------------------------------------

'''mass= int(input("Enter mass in kgs: "))
c = 300000000
speed= pow(c,2)

E= mass * speed
print("Enery is" , E) '''
#--------------------------------------------------

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d=d.replace("$", "")
    d= float(d)
    return d


def percent_to_float(p):
    p=p.replace("%", "")
    p= float(p)
    p=p/100
    return p


main()