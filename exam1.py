# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 20:19:29 2019

@author: user

progarm: Exam1
"""
""" 第一題
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())

print("|%5d %5d|" % (num1,num2))
print("|%5d %5d|" % (num3,num4))
print("|%-5d %-5d|" % (num1,num2))
print("|%-5d %-5d|" % (num3,num4))
"""
"""第二題
num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())

print("|%7.2f %7.2f|" % (num1,num2))
print("|%7.2f %7.2f|" % (num3,num4))
print("|%-7.2f %-7.2f|" % (num1,num2))
print("|%-7.2f %-7.2f|" % (num3,num4))
"""

"""第三題
str1 = input()
str2 = input()
str3 = input()
str4 = input()

print("|%10s %10s|" % (str1,str2))
print("|%10s %10s|" % (str3,str4))
print("|%-10s %-10s|" % (str1,str2))
print("|%-10s %-10s|" % (str3,str4))
"""

"""第四題
import math
pi=math.pi
r = float(input())
print("Radius = %.2f\nPerimeter = %.2f\nArea = %.2f" % (r,2*r*pi,r*r*pi))
"""

"""第五題
height = float(input())
width = float(input())
print("Height = %.2f\nWidth = %.2f\nPerimeter = %.2f\nAera = %.2f" % (height,width,2*(height+width),height*width))
"""
"""第六題 1英哩=1.6公里
x = int(input())
y = int(input())
z = int(input())

print("Speed = %.1f" % (z/((y+60*x)/3600)/1.6))
"""

"""第七題
num1=int(input())
num2=int(input())
num3=int(input())
num4=int(input())
num5=int(input())
sum = num1+num2+num3+num4+num5
print("%d %d %d %d %d\nSum = %.1f\nAverage = %.1f" % (num1,num2,num3,num4,num5,sum,sum/5))
"""

"""第八題
x1 = eval(input())
y1 = eval(input())
x2 = eval(input())
y2 = eval(input())
d = (((x1-x2)**2)+((y1-y2)**2))**0.5
print("( {} , {} )\n( {} , {} )\nDistance = {:.4f}".format (x1,y1,x2,y2,d))
"""

"""第九題
import math
s = int(input())
Area = (5*(s**2))/(4*math.tan(math.pi/5))
print("Area = %.4f" % (Area))
"""
import math
n = int(input())
s = int(input())

Area = (n*(s**2)/(4*math.tan(math.pi/n)))

print("Area = %.4f" % (Area))
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
    print("Invalid")