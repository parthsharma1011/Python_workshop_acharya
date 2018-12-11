'''
#Types of Imports
#TYPE-I
import math
print(math.sqrt(81))
print(math.factorial(5))

#TYPE-II
n=10
k=2
from math import factorial
print(factorial(n)/(factorial(k) * factorial(n-k))) #try //

#Type-III
from math import factorial as fac
print(fac(n)/(fac(k) * fac(n-k)))
'''
#============================================================================================
'''
#nested if-else
h = 50
if h > 50:
    print('Greater than 50')
else:
    if h < 20:
        print('less than 20')
    else:
        print('btw 20 and 50')


#another way using elif
if h > 50:
    print('Greater than 50')
elif h < 20:
    print('less than 20')
else:
    print('btw 20 and 50')

#FLAT IS BETTER THAN NESTED
'''
#============================================================================================
'''
#WHILE LOOPS
c = 5
while c!=0:
    print(c)
    c-=1 #Augumented assignment operator

c = 5
while c:
    print(c)
    c -= 1
#EXPLICIT IS BETTER THAN IMPLICIT

while True:
    i = input('hey tel me')
    if int(i) % 7 == 0:
        break

'''
#============================================================================================
'''
my_list = ['a',1,'bhai',3,'parth']
my_list.append('cool')
my_list.append('what up')
print(my_list)
print(my_list[2])
my_list2 = ['apple',
            'orange',
            'lion',]  #can have a last comma for future change
print(my_list2)
'''

#============================================================================================
#Dictionaries
# my_dict = {'parth' : '9036303656', 'xyz' : '91919'}
# print(my_dict['parth'])
#
#
# #for-loop with lists
# cities = ['london','paris','new-york']
# for city in cities:
#     print(city)
#
# #for-loop with dicts
# colors = {'crimson' : 0xdc143c,'coral':0xff7f50}
# for color in colors:
#     print(color,colors[color])
#
'''
from urllib.request import urlopen
with urlopen('http://sixty-north.com/c/t.txt') as story:
    story_words = []
    for line in story:
        line_words = line.decode('utf-8').split()  #try .decode('utf-8')
        for word in line_words:
            story_words.append(word)
print(story_words)
'''

#============================================================================================
# #none object in python class
# def even_or_odd(x):
#     if x%2==0:
#         print('number is even')
#         return
#     print('odd')
# print(even_or_odd(2))
# print(even_or_odd(5))

#============================================================================================
#python docstrings
#!/usr/bin/env python3
"""Retrieve and print words from a URL

Usage:

      Python 3 training.py <http://sixty-north.com/c/t.txt>
"""
import sys
from urllib.request import urlopen
def fetchwords(url):
    """Fetch a list of word from URL.

    Args:
        url: The URL of a UTF-8 text document
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()  #try .decode('utf-8')
            for word in line_words:
                story_words.append(word)
    return story_words

#two lines btw functions #pep-8 says sparse is better than dense
def print_items(items):
    """Print items one per line

    Args:
        An ierable series of printable items """
    for item in items:
        print(item)


def main(url):
    """Print each word from a text document from a URL.

    Args:
        url:The url of a UTF-8 text docuemnts"""
    words = fetchwords(url)
    print_items(words)


if __name__ == '__main__':
    main(sys.argv[1]) #0th arg is the filename

#============================================================================================
'''
a = [1,2,3]
b = [1,2,3]

print(a == b)
print(a is b)

'''
#============================================================================================
# def banner(message,border='-'):
#     line = border * len(message)
#     print(line)
#     print(message)
#     print(line)
#
# print(banner("parth"))
# print(banner('hello ai','+'))
# print(banner("hello",border='^'))
# print(banner(border='.',message='hello friends!'))

# #default Function
# def add_spam(menu=[]): #list is created once
#     menu.append("spam")
#     return menu
# breakfast = ['bacon','eggs']
# print(add_spam(breakfast))
# lunch =['baked beans']
# print(add_spam(lunch))
# print(add_spam())
# print(add_spam())
# print(add_spam())
'''
#use immutable values for constants
def add_spam(menu=None):
    if menu is None:
        menu = []
        menu.append('spam')
        return menu
print(add_spam())
print(add_spam())
print(add_spam())
'''
#============================================================================================
#python base
#for python functions
