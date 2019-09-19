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
