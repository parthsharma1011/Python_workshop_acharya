
'''
#more variables and printing
name = 'Parth Sharma'
age = 35
height = 73
weight = 180
eyes = 'Blue'
teeth = 'white'
hair = 'Brown'

print('Let\'s talk about %s ' %name)
print('He\'s %s cms tall' %height)
print('he\'s %s pounds heavy' %weight)
print('he\'s got %s eyes and %s hair'%(eyes,hair))
print('he\'s got %s hair but dosent suit him' %teeth)

#A lil tricky line
print('if i add %d, %d and %d i get %d' %(age,height,weight,age+height+weight))
'''

'''
#Python string formatters
x = 'There are %d types of people' %10
binary = 'binary'
do_not = 'don\'t'
y = 'those who know %s and those who %s' %(binary,do_not)

print(x)
print(y)

print('i said : %r'  % x)
print('I also said %r :' % y)

hilarious = False
joke_evaluation = 'isn\'t this joke so funny! %r'

print(joke_evaluation % hilarious)
w = 'This is the left side of...'
e = 'a string with a right side'
print(w+e)
'''

'''
# More Printing
print('\n' * 5)
print('Mary had a little lamb.')
print('it\'s fleece was as white as %s' %'snow')
print('And everywhere the mary went')
print('.' * 10)
'''

'''
# Printing Printing
formatter = "%r %r %r %r"
print(formatter%(1,2,3,4))
print(formatter %(True,False,True,True))
print(formatter % ('I had this thing','But wait!', 'do u like python', 'coz i love it'))
'''
'''
#Printing pRINTING Printing
days = 'mon, tue, wed, thu, fri, sat'
months = 'jan\nfeb\nmarch\napril\nmay\njune\njuly\naugust\nseptember\noctober'
print(months)
'''

'''
tabby_cat = "\t I\'m tabbed in"
persian_cat = 'Im split\n on a line'
backlash_cat = "i'M \\ a \\ cat."
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
"""
print(tabby_cat)
print(persian_cat)
print(fat_cat)
print(backlash_cat)
'''
'''
a = ('\t' * 3)
print(a +'hey ')
'''

'''
while True:
    for i in ["/","_","|","\\","|"]:
        print('%s\r' %i)
'''
'''
#Python animation for loading
import itertools
import threading
import time
import sys

done = False
#Here is the animation
def animate():
    for c in itertools.cycle(['|','/', '-','\\']):
        if done:
            break
        sys.stdout.write('\rloading' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!   ')

t = threading.Thread(target=animate)
t.start()
'''

'''
#Asking Questions
print('How old are you?\n')
age = input()
print('How tall are you?\n')
height = input()
print('How much do u weigh?\n')
weight = input()
print('so you are %r year old and %r year old and weigh %r kg' %(age,height,weight))
'''
'''
#Prompting People
formatter = ('%r %r %r %r')
a = input('what is your name ')
b = input('what is your pet name')
c = input('what is your idiot')
v = input('what the hell is your email?')
#print(formatter%(a,b,c,v))
print('so you are %r and %r and %r and %r' %(a,b,c,v))
'''
'''
#Chracter Input
name = input('What is your name :' )
age = int(input('How old are you :'))
year = str((2017-age)+100)
print(name+'will be 100 year old in'+year)
'''
'''
 #Names, Variables , Code, Functions
def print_two(*args):
     arg1,arg2 = args
     print('arg1:%r , arg2 :%r'%(arg1,arg2))

def print_two_again(arg1, arg2):
    print('arg1:%r , arg2 :%r' % (arg1, arg2))

def print_one(arg1):
    print('arg1:%r ' % arg1)

def print_none():
    print('I ain\'t got nothing')

print_two('parth','pooja')
print_two_again('parth', 'pooja')
print_one('parth')
print_none()
'''
'''
#Functions and variables
def cheese_and_crackers(cheese_count, cracker_count):
    print('you have %r slices of cheese' %cheese_count)
    print('you have %r boxes of crackers' %cracker_count)
    print('let the party begin!')

print('here function numbers are given directly')
cheese_and_crackers(20, 45)

print('or we can use variables like these')
cheese_slices_count = 10
crackers_box_count = 60
cheese_and_crackers(cheese_slices_count,crackers_box_count)

print('we can math too')
cheese_and_crackers(10+10, 50+60)

print('we can also combine variable and math')
cheese_and_crackers(cheese_slices_count+10, crackers_box_count+80)
'''

'''
#Functions can return something

def add(a,b):
    print('adding %d and %d' %(a,b))
    return (a+b)

def sub(a,b):
    print('subtracting %d and %d ' %(a,b))
    return (a-b)
def multiply(a,b):
    print('multiplying %d and %d' %(a,b))
    return (a*b)
def divide(a,b):
    print('dividing %d and %d' %(a,b))
    return (a/b)

age = add(30,5)
height = sub(40, 50)
weight = multiply(30,5)
der = divide(40,40)

#Print all and verify
print(age,height,weight,der)


print('age : %d height:%d weight:%d and der:%d' %(age,height,weight,der))


#Here is a puzzle
print('Puzzle time!')
what = add(age, sub(height,multiply(weight,divide(der,3))))
print('here is ',what, 'can you do it?')
'''
'''
#More practise
print('lETS RECAP EVERYTHING! SHALL WE?')
print('You\'d need yo know \'bout escapes with\\ that do\n newlines and \t tabs')
'''

'''
#poem = 

\t*the lovely world
with logic so firmly planted 
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.

'''
'''
print('=='*20)
print(poem)
print('++'*20)

five = 10 - 2 + 3 -6
print('This should be five :%s' %five)

def secret_formula(started):
    jellybeans = started * 500
    jars = jellybeans / 1000
    crates = jars / 100
    return (jellybeans,jars,crates)

start_point = 10000
beans,jars,crates = secret_formula(start_point)

print('with a starting point : %d'%start_point)
print('we\'d have %d beans, %d jars and %d crates'%(beans,jars,crates))

start_point = start_point/10

print('we can also do it this way')
print('we\'d have %d beans, %d jars and %d crates'%secret_formula(start_point))
'''

'''
#What if
people = 20
cats = 30
dogs = 15

if people < cats:
    print('too many cats! the world is doomed')
if people > cats:
    print('not many cats!')
if people < dogs:
    print('the world is drooled on!')
if people > dogs:
    print('people more dogs less')

dogs = dogs+5
if people >= dogs:
    print('people are greater and equall to dogs ')
if people <= dogs:
    print('people are less than and equall to dogs ')
if people == dogs:
    print('holy cow, people are dogs')

'''
'''
people = input('enter the number of people\t*')
cars = input('enter the number of cars\t*')
buses =input('enter the number of buses\t*')

if people > cars:
    print('we need more cars')
elif cars < people:
    print('lets not take cars')
else:
    print('cant decide :(')

if buses > cars:
    print('lets just take a bus ')
elif cars < buses:
    print('maybe we could take a bus')
else:
    print('still can\'t decide')

'''
'''
#Making Decisions
v=('=='*2)
print(v+'You enter a dark room with two doors. Do you go through door #1 or 2?'+v)

door = input('>')
if door == "1":
    print('There is a giant bear eating a cheesecake. What would u do?')
    print('1: Take the cake')
    print('2: Scream at the bear')
    bear = input('>')
    if bear == "1":
        print('the bear eats your face off')
    elif bear=="2":
        print('bear eats your leg off')
    else:
        print('well doing %s is probably better. Bear runs away'%bear)
elif door =="2":
    print('you stare into the endless abyss at cthulhu\'s retina')
    print('1: Blueberries')
    print('2: yellow jacket clothespin')
    print('3: listening to AC-DC\'s back in black')

    insanity = input('>')
    if insanity == "1" or insanity == "2":
        print('your body survives powered by a mind of jello')
    else:
        print('the insanity rots your eye into a pool of muck')

else:
    print('you stumbled around and fall on a knife and die!')

'''

'''
#Loops and lists
the_count = [1,2,3,4,5]
fruits = ['apples','oranges', 'pears','apricots']
change = [1,'pennies',2,'dimes',3,'quarters']

#This for loop goes through the loop
for number in the_count:
    print('this is count %d'%number)

for fruit in fruits:
    print('the list of fruits are :%s'%fruit)

#also we can go through mixed lists too
#notice we use %r since we dont know what is in it
for i in change:
    print('i got %r'%i)

elements = []

#use range fuunction to do 0 to 5 counts
for i in range(0,6):
    print('Adding %d to the list'%i)
    #append is a function that lists understand
    elements.append(i)

for i in elements:
    print('elements was : %d'%i)
'''
'''
#While loops
i = 0
numbers = []

while i < 6:
    print('at the top i is :%d'%i)
    numbers.append(i)

i = i+1
print('Numbers now:',numbers)
print('At the bottom i is %d'%i)

print('The numbers')

for num in numbers:
    print(num)
'''

'''
#acessing elements of list
animal = ['tiger','bear']
ani = animal[1]
print(ani)
'''
'''
#Branches and functions
from sys import exit

def gold_room():
    print('room full of gold. what would you take?')
    next = input('\t\t>')
    if '0' in next or '1' in next:
        how_much = int(next)
    else:
        dead('Man, learn to type a number')
    if how_much < 50:
        print('Nice you are not greedy, You win!')
        exit(0)
    else:
        dead('You greedy bastard!')

def bear_room():
    print('There is bear here')
    print('it has a bunch of honey')
    print('The fat bear is in front of another door')
    print('How are you going to move the bear?')
    bear_moved = False

    while True:
        next = input('\t\t>')

        if next == 'take honey' or 'honey':
            dead('The bear looks at you and slaps you')
        elif next == 'taunt bear' and not bear_moved:
            print('bear moved, u go now')
            bear_moved=True
        elif next == 'taunt beat' and bear_moved:
            dead('the bear gets pissed and chewed ur leg')
        elif next == 'open door' and bear_moved:
            gold_room()
        else:
            print('i have no idea what you mean')

def cthulhu_room():
    print('here is great evil cthulhu')
    print('if he stares at you, you go insane')
    print('Do u flee 4 life or eat ur head')
    next = input('\t\t>')
    if 'flee' in next:
        start()
    elif 'head' in next:
        dead('well that was tasty!')
    else:
        cthulhu_room()



def start():
    print('You are in a dark room')
    print('door to left or right')
    print('select one!')

    next = input('\t\t>')

    if next == 'left' or 'l':
        bear_room()
    elif next == 'right' or 'r':
        cthulhu_room()
    else:
        dead('You stumble around the room and starve')

def dead(why):
    print(why,'Good job!')
    exit(0)

start()
'''
'''
#Doing things to lists
ten_things = 'Apples Oranges Crows Telephone Light Sugar'
print('wait! there isn\'t ten things in the list')
stuff = ten_things.split(' ')
more_stuff = ['Day','Night','Song', 'frisbee','corn', 'banana', 'girl', 'boy']

if len(stuff) != 10:
    next_one = more_stuff.pop()
    print('added a new item : %r'%next_one)
    stuff.append(next_one)
    print('there are %d items now'%len(stuff))

print('There we go : %r' %stuff)

print('Now lets tweak stuff, shall we')

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print('|'.join(stuff))
print(' | '.join(stuff[3:5]))
'''

# Dictionaries, oh my dictionaries

# Create a mapping of states to abbrevation
