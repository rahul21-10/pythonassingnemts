#numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included)

a= list (range(2000,3201))
b=[] 
for i in a:
    if (i%7==0) and (i%5!=0):
          b.append (i)
print(b)


# Write a Python program to find the volume of a sphere with diameter 12 cm


d=12
v= 1.33*3.14*(d/2)*(d/2)*(d/2)
print (v)


# Create the below pattern using nested for loop in Python.


for i in range(6):
    for j in range (i):
        print ("*",end="")     
    print()
for i in range(6):
    for j in range (6-i):
        print ("*",end="")     
    print()


 # Write a Python program to reverse a word after accepting the input from the user
 # Input word: AcadGild


a = input ("Input Word")
b = len(a)
c= a[b::-1]
print(c)


# Write a Python program to accept the user's first and last name and then getting them 
#printed in the the reverse order with a space between first name and last name.


a = input ("Enter your First and Last Name")
b = len(a)
c=a[b::-1]
print(c)


# Write a program which accepts a sequence of comma-separated numbers from console and
#generate a list.


a = input("Enter Numbers seperated by Comma").split(',')
print(a)






