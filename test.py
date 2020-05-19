# -*- coding: utf-8 -*-
"""
Created on Mon May  4 21:22:36 2020

@author: 6752499
"""

"""
import inspect

x = "abc"

for m in inspect.getmembers(x):
    print(m)

"""

#a="aldous Huxley was born in 1894".title()

#print(a)

#a = "どこで？　いつ？　だれが？".split("　")
#print(a)

"""
a = ["The", "fox", "jumped", "over", "the", "fence", "."]
A = " ".join(a[:6]) + a[6]
print(A)
"""
"""
a = "A screaming comes across the sky.".replace("s","$")
print(a)
"""

"""
a = "Hemingway".index("m")
print(a)
"""
"""
a = "なんでもありの\"や\"ったもん勝ち"
print(a)
"""
"""

a ="three"
b = a+" " + a+" " + a
c = ((a+" ")*3).strip()

print(b)
print(c)
"""

"""
a = "四月の晴れた寒い日で、時計がどれも十三時を打っていた。"

print(a[:a.index("、")])
"""
"""
name = ["Ted", "Got", "Voxe"]

i=0

for n in name:
    n = name[i]
    name[i] = n.upper()
    i += 1
    #print(name)
print(name)
"""

"""
name = ["Ted", "Got", "Voxe"]
for i, n in enumerate(name):
    n = n.upper()
    name[i] = n

print(name)
"""
"""
name = ["Ted", "Got", "Voxe"]
com = ["Asistant", "Global", "Desk"]
all_shows=[]

for show in name:
    all_shows.append(show.upper())
    print(all_shows)
for show in com:
    all_shows.append(show.upper())
    print(all_shows)

print(all_shows)    
"""
"""
x = 10
while x > 0:
    print(x)
    x -= 1
print("Happy New Year!")
"""
"""
while True:
    print("Hello World!")
"""

"""
for i in range(0,100):
    print(i)
    break
"""
"""
qs = ["What is your name?", 
      "What is your fav. color?",
      "What is your quest?"]

n = 0
while True:
    print("Type q to quit")
    a = input(qs[n])
    if a == "q":
        break
    n = (n + 1) % 3
"""
"""
for i in range(1,6):
    if i == 3:
        continue
    print(i)
"""
"""
i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1
"""
"""
for i in range(1,3):
    print(i)
    for letter in ["a", "b", "c"]:
        print(letter)
"""
"""
list1 = [1,2,3,4]
list2 = [5,6,7,8]
added = []

for i in list1:
    for j in list2:
        added.append(i + j)

print(added)
"""
"""
while input("y or n?") != "n":
    for i in range(1,6):
        print(i)
"""
"""
a = ["ウォーキング・デッド", "アントラージュ", "ザ・ソプラノズ", "ヴァンパイア・ダイアリーズ"]

for i in a:
    print(i)
"""
"""
for i in range(25,51):
    print(i)
"""
    