#!/usr/bin/env python
# coding: utf-8

# In[1]:


a= list (range(2000,3201))
b=[] 
for i in a:
    if (i%7==0) and (i%5!=0):
          b.append (i)
print(b)


# In[2]:


d=12
v= 1.33*3.14*(d/2)*(d/2)*(d/2)
print (v)


# In[3]:


for i in range(6):
    for j in range (i):
        print ("*",end="")     
    print()
for i in range(6):
    for j in range (6-i):
        print ("*",end="")     
    print()


# In[6]:


a = input ("Enter your First and Last Name")
b = len(a)
c= a[b::-1]
print(c)


# In[7]:


a = input ("Enter your First and Last Name")
b = len(a)
c=a[b::-1]
print(c)


# In[12]:


a = input("Enter Numbers seperated by Comma").split(',')
print(a)


# In[ ]:





# In[ ]:




