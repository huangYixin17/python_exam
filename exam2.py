# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 09:45:15 2019

@author: user
"""

"""第一題
num = int(input())

if(num % 2 == 0):
    print("%d is an even number." % (num))
else:
    print("%d is not an even number." % (num))
"""

"""第二題
num = int(input())

if((num % 3 ==0) and (num % 5 == 0)):
    print("%d is a multiple of 3 and 5." % num)
elif((num % 3 ==0)):
    print("%d is a multiple of 3." % num)
elif((num % 5 ==0)):
    print("%d is a multiple of 5." % num)
else:
    print("%d is not a multiple of 3 or 5." % num)
"""

"""第三題
num = int(input())
if(num % 400 == 0):
    print("%d is a leap year." % num)
elif(num % 100 == 0):
    print("%d is not a leap year." % num)
elif(num % 4 == 0):
    print("%d is a leap year." % num)
else:
    print("%d is not a leap year." % num)
"""

"""第四題
a = int(input())
b = int(input())
c = input()

if(c =="+"):print(a+b)
if(c =="-"):print(a-b)
if(c =="*"):print(a*b)
if(c =="/"):print(a/b)
if(c =="//"):print(a//b)
if(c =="%"):print(a%b)
"""

"""第5題(指令需要記)
text = input()

if (text.isalpha()):
    print(text,"is an alpahabrt. ")
elif(text.isdigit()):
    print(text,"is a number. ")
else:
    print(text,"is a symbol. ")
"""

"""第6題
text = int(input())
if(80 <= text <=100):
    print("A")    
elif(70 <= text <80):
    print("B")    
elif(60 <= text <70):
    print("C")    
elif(text < 60):
    print("F")        
"""

"""第七題
money = int(input())

if(18000> money >= 8000):
    money = money *0.95
elif(28000> money >= 18000):
    money = money * 0.9
elif(38000> money >= 28000):
    money = money * 0.8
elif(money >= 38000):
    money = money * 0.7
print(money)    
"""

"""第8題
num = int(input())

if(0<= num <=15):
    if(num == 10):
        print("A")
    elif(num == 11):
        print("B")
    elif(num == 12):
        print("C")
    elif(num == 13):
        print("D")
    elif(num == 14):
        print("E")
    elif(num == 15):
        print("F")
    else:
        print(num)
"""

"""第9題
x = int(input())
y = int(input())

d = (((x-5)**2)+((y-6)**2))**0.5
if(d<=15):
    print("Inside")
else:
    print("Outside")    
"""

n1 = int(input())
n2 = int(input())
n3 = int(input())

if(((n1+n2)>n3) and ((n2+n3)>n1) and ((n3+n1)>n2)):
    print((n1+n2+n3)/3)
else:
    print("Invalid")