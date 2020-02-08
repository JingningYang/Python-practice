#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 12:48:22 2020

@author: jingningyang
"""

#Python Homework #1: Exercises with lists, loops, and functions
#1. Creating python lists.
#a) [1,2,3,...,19,20]
lis = []
for i in range(20):
    i += 1
    lis.append(i)
print(lis)

#b) [20,19,...,2,1]
list1 = []
i = 20
while i > 0:
    list1.append(i)
    i -= 1
print(list1)

#c) [1,2,3,..,19,20,19,18,...,2,1]
first_half = lis[:]
last_half = list1[:]
del last_half[0]
newlist = first_half + last_half 
print(newlist)
    
#d) [4,6,3,4,6,3,...,4,6,3]
x = 4,6,3
list2 = list(x*10)
print(list2)

#e) [4,6,3,4,6,3,...,4,6,3,4]
list2.append(4)
print(list2)

#2. Create a list of values
import math 
list2 = []
i=3
while i < 6:
    list2.append(i)
    i += 0.1
newl = [round(num,1) for num in list2]
print(newl)
#input newl into the formula and compute.
newlist = []
for i in newl:
    result = pow(math.e,i) * math.cos(i)
    newlist.append(result)
print(newlist)
    


#3. Create a list of values
def decimal(x):
    valuelist = []
    for a in range(25):
        a += 1
        value = (x**a)/a
        valuelist.append(value)
    return valuelist
decimal(2)

#4. 
#a)
a = lis
newlist = []
for i in range(len(a)):
    value = a[i] - a[-(i+1)]
    i += 1
    newlist.append(value)
print(newlist)

#b)
boolist = []
for i in a:
    value = (i % 2 == 0)
    boolist.append(value)
print(boolist)

#5. 
#a)
with open('lorem.txt','r') as f:
    # Read the contents into a list of strings
    all_lines = f.readlines()
    # This will always close the file but do it
    # anyway...it's a good habit.
    f.close()
lines , phrases, words = [], [], []
number, number1, number2 = 0,0,0
for line in all_lines:
    lines += line.split(".")
for phrase in lines:
    phrases += phrase.split(",")
for word in phrases:
    words += word.split(" ")
for each in words: 
    if 1 <= len(each) <= 4:
        number += 1
    elif 4 <= len(each) <= 7:
        number1 += 1
    elif len(each) >= 7:
        number2 += 1
           
print('Number of strings whose length are between 1 and 4: ',  number)
print("Number of strings whose length are between 4 and 8: ",  number1)
print("Number of strings whose length are greater than 7: ",  number2)

#b)
import re
#tranfer list to string
listtostr = " ".join([str(elem) for elem in all_lines])
# Define a pattern that will match:
#    All capitalized words
pat = re.compile('([A-Z][a-z]+)')
# Use the findall method to find all matches.
match = pat.findall(listtostr)
# Check the number of matches
print('# of Capitalized character matches: %s\n' % len(match)) 

    

















    