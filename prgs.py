# #max of two
# def max_of_two(x,y):
#     if x > y:
#         return x
#     return y
# def max_of_three(x,y,z):
#     return max_of_two(x,max_of_two(y,z))
#
# print(max_of_three(1,2,3))



# #add all elem of list
# def sum(nums):
#     total=0
#     for i in nums:
#         total += i
#     return total
#
# print(sum((1,2,3)))
#
# def mul(numbers):
#     total = 1
#     for i in numbers:
#         total *= i
#     return total
#
# print(mul((1,2,3)))


#=============================================================
# names1 = ['x', 'y', 'z', 'p']
# names2 = names1
# names3 = names1[:]
#
#
# names2[0] = 'new1'
# names3[1] = 'new2'
#
# sum = 0
# for ls in (names1, names2, names3):
#     if ls[0] == 'new1':
#         sum += 1
#
# if ls[1] == 'new2':
#     sum += 10
#     print(sum)


# def main():
#     student = ["Anish", "Aadi", "Deepak", "Priyanshu"]
#
#
#
#     #TODO : it is converting into list and chaning default value
#     for i,m in enumerate(student,start=4):
#         print(i,m)
#
#
# if __name__ == '__main__':
#     main()

# define enumeration using the Enum class


#=============================================================

#enum have name and value property

# from enum import Enum, unique, auto
#
# @unique  #DECORATOR
# class Fruit(Enum):
#     APPLE = 1
#     BANANA = 2
#     ORANGE = 3
#     TOMATO = 4
#     find_gregory_sharma = "finder"
#
#     Pear = auto()
# #Enum dosent support duplicate names(key) but duplicate value is allowed KIWI = 1
#
# def main():
#     pass
#
#     #TODO : enums have human-redable values and types
#     # print(Fruit.APPLE)
#     # print(type(Fruit.APPLE))
#     # print(repr(Fruit.APPLE))
#
#
#
#     #TODO : enums have name and value properties
#     # print(Fruit.APPLE.name,Fruit.APPLE.value)
#
#     # TODO : print the auto-generated value
#     # print(Fruit.Pear.name,Fruit.Pear.value)
#     print(Fruit.find_gregory_sharma.name, Fruit.find_gregory_sharma.value)
#
#     # TODO :enums are hashable - can be used as keys
#     my_Fruits = {}
#     my_Fruits[Fruit.BANANA] = "Come mr smart man"
#     print(my_Fruits[Fruit.BANANA])  #value with key
#
#
# if __name__ == "__main__":
#     main()

#=============================================================
#Namedtuple
#ADVANCED COLLECTION

#Demo on namedtuple object

# import collections
#
# def main():
#     #TODO : create a Point namedtuple
#     Point = collections.namedtuple("Points", "x y")
#     p1 = Point(10, 20)
#     p2 = Point(30, 40)
#     print(p1,p2)
#     print(p1.x,p2.y)
#
#     # TODO : use _replace metod to create a new instance
#     p1 = p1._replace(x=100)
#     print(p1)
#
#
#
#
# if __name__ == "__main__":
#     main()

#=============================================================
#basic logging
#customized logging

##################################
##  basicConfig(                ##
##    format = formatstr,       ##
##    datefmt = date_format_str ##
##################################

#demo how custom logging output works

# import logging
#
# extraData = {
#     'user' : 'user@name.com',
#     'user2':'user2@name.com'
# }
#
# #TODO : add another function to log from
# def anotherFunction():
#     logging.debug("This is a debug-level message",extra=extraData)
#
# def main():
#     #set the output file and debug level, and
#     #TODO :  use a custom formatting specification
#     fmtstr = "User : %(user)s %(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d %(message)s"
#     datestr = "%m/%d/%Y %I: %M:%S %p"
#     logging.basicConfig(filename="output.log", level=logging.DEBUG,
#                         filemode="w",
#                         format=fmtstr,
#                         datefmt=datestr)
#
#
#     logging.info("This is an info-level log message",extra=extraData)
#     logging.warning("This is warning level message",extra=extraData)
#     anotherFunction()
#
# if __name__ == "__main__":
#     main()

#=============================================================
#Class string values

###syntax
# object.__getattribute__(self,attr)
# object.__getattr__(self,attr)
# object.__setattr__(self,attr,val)
# object.__delattr__(self)
# object.__dir__(self)

#Coustomised string representation of objects

# class myColor():
#     def __init__(self):
#         self.red = 50
#         self.green = 75
#         self.blue = 100
#
#     #TODO : use getattr to dynamically return a value
#     def __getattr__(self, attr):
#         if attr == "rgbcolor":
#             return (self.red,self.green,self.blue)
#         elif attr == "hexcolor":
#             return "#{0:02x}{1:02x}{2:02x}".format(self.red,self.blue,self.green)
#         else:
#             raise AttributeError
#
#     # TODO : user setattr to dynamically return a value
#     def __setattr__(self, attr, val):
#         if attr == "rgbcolor":
#             self.red = val[0]
#             self.blue = val[1]
#             self.green = val[2]
#         else:
#             super().__setattr__(attr,val) #must have super
#
#     # TODO : user dir to list the avilable properties
#     def __dir__(self):
#         return ("red," "green", "blue", "rgbcolor","hexcolor")
#
#
# def main():
#     #create an instance of myColor
#     cls1 = myColor()
#
#     # TODO :print the value of a computed attribute
#     print(cls1.rgbcolor)
#     print(cls1.hexcolor)
#     # TODO : set the value of a computed attribute
#     cls1.rgbcolor = (125,200,86)
#     print(cls1.rgbcolor)
#     print(cls1.hexcolor)
#
#     # TODO :access a regular attribute
#     print(cls1.red)
#
#     # TODO :list the avilable attributes
#     print(dir(cls1))
#
# if __name__ == "__main__":
#     main()

#=============================================================
#Class numerical operators


#Give object number like behavior

# class Point():
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#
#     def __repr__(self):
#         return "<Point x:{0},y:{1}".format(self.x,self.y)
#
#     # TODO : implement addition
#     def __add__(self, other):
#         return Point(self.x + other.x,self.y + other.y)
#
#     # TODO : implement subtraction
#     def __sub__(self, other):
#         return Point(self.x - other.x, self.y - other.y)
#
#     # TODO : implement multiplication
#     def __mul__(self, other):
#         return Point(self.x * other.x, self.y * other.y)
#
#     #__iadd__ is inplace addition
#     def __iadd__(self, other):
#         self.x += other.x
#         self.y += other.y
#         return self
#
#
# def main():
#     p1 = Point(10,20)
#     p2 = Point(30,80)
#     print(p1,p2)
#
#     #Addition
#     p3 = p1 + p2
#     print(p3)
#
#     #Subtraction
#     p4 = p2 - p1
#     print(p4)
#
#     #multiply
#     p5 = p1 * p2
#     print(p5)
#
#     #inplace addition
#     p1 += p2
#     print(p1)
#
#
# if __name__ == "__main__":
#     main()

#=============================================================
#Advanced counters
#ordereddict

#showcase the use of Ordereddict objects

# from collections import OrderedDict
#
# def main():
#     #list of sports teams with wins and losses
#     sportsTeams = [("Rovals",(18,12)),("Rockets",(24,6)),
#                    ("Cardinal",(20, 10)),("Dragons",(22, 8)),
#                    ("Kings",(15,15)),("Chargers",(20,10)),
#                    ("Jets",(16,14)),("Rockets",(25,5))]
#
#     #sort the teams by number of wins
#     sortedTeams = sorted(sportsTeams, key=lambda t: t[1][0], reverse=True)
#
#     # TODO : create an ordered dictionary of the teams
#     teams = OrderedDict(sortedTeams)
#     print(teams)
#
#     # TODO : Use popitems to remove the top item
#     tm, wl = teams.popitem(False)
#     print("Top Team : ",tm,wl)
#
#     # TODO : what are next the top 4 teams?
#     for i,team in enumerate(teams,start=1):
#         print(i,team)
#         if i == 4:
#             break
#
#
#     # TODO :test for equality
#     a = OrderedDict({"a":1,"b":2,"c":3})
#     b = {"a": 1, "b": 2, "c": 3}
#     print("Equality Test : ", a==b)
#
#
#
# if __name__ == "__main__":
#     main()

#=======================================================================================================================
#Python comprehensions
#can be applied to list , set and dict

# list(map(F2C,[32,65,104,212])  #comprehentaion
#
# outputexp = (t*9/5 + 32)  var=t  in = [32,65,104,212]
#
# how to apply predicate exp to perform filtering effect

#=======================================================================================================================

#demonstrate the usage of  Counter objects

# from collections import Counter
#
# from enum import Enum, auto,unique
#
#
#
# def main():
#     #list of students in class 1
#     class1 = ["Bob","Becky","Chad","Darcy","Frank","Hannah",
#               "Kevin","James","Melanie","Penny","Steve","James"]
#
#     class2 = ["Bill","Barry","Cindy","Debbie","Frank","Gabby",
#               "Kelly","James","Joe","Sam","Tara","Ziggy"]
#
#     # TODO : Create a Counter for class1 and class2
#     c1 = Counter(class1)
#     c2 = Counter(class2)  #counter is a dict
#
#     # TODO : How many students in class1 named james?
#     #print(c1['James'])
#     #also print for class2
#     #print(c2['Darcy'])
#
#     # TODO :How many students in class1
#     #print(sum(c1.values()),"students in class 1")
#
#     # TODO :Combine the two classes
#     c1.update(class2)
#     #print(sum(c1.values()), "students in class 1")
#
#     # TODO : most common names in two classes
#     #print(c1.most_common(3))
#
#     # TODO :seperate the classes again
#     c1.subtract(class2)
#     #print(c1.most_common(3))
#
#
#     # TODO :what's common between the two classes?
#     #items in both
#
#     print(c2 and c1)
#     print(c1 & c2)
#
#
# if __name__ == "__main__":
#     main()

#=======================================================================================================================
#converting values in to string representation
#class string functions

#object.__str__(self)
#object.__repr__(self)
#object.__format__(self,format_spec)
#object.__bytes__(self)

#customize string representation of objects

#
# class Person():
#     def __init__(self):
#         self.fname = "parth"
#         self.lname = "sharma"
#         self.age = 24
#
#     # TODO : use __repr__ to create a string useful for debugging
#     def __repr__(self):
#         return "Person Class - fname:{0},lname{1},age:{2}".format(self.fname,self.lname,self.age)
#
#     # TODO :use str for a more human-readable string
#     def __str__(self):
#         return "Person {0} {1} is {2} year old!".format(self.fname,self.lname,self.age)
#
#
#     def __bytes__(self):
#         val = "Person : {0} : {1} : {2}".format(self.fname,self.lname,self.age)
#         return bytes(val.encode('utf-8'))
#
# def main():
#     #create a new person object
#     cls1 = Person()
#
#     #using different python functions to convert it to a string
#     print(repr(cls1))
#     print(str(cls1))
#     print("Formatted : {0}".format(cls1))
#     print(bytes(cls1))
#
# if __name__ == "__main__":
#     main()

#=======================================================================================================================
# Sets comprehensions

# def main():
#     #define a list of temperature data points
#     ctemps = [5, 10, 12, 14, 10, 23, 41, 30, 12, 24, 12, 18, 29]
#     ftemps1 = [(t*9/5)+32 for t in ctemps]
#     ftemps2 = {(t * 9 / 5) + 32 for t in ctemps}
#     print(ftemps1)
#     print(ftemps2)
#
#     # TODO : build a set of unique Fahrenheit temperatues
#
#     # TODO : build a set from an input source
#     sTemp = "The quick brown fox jumped over the lazy dog"
#     chars = {c.upper() for c in sTemp}  # if not c.isspace()
#     print(chars)
#
#
# if __name__ == "__main__":
#     main()

#=======================================================================================================================
#List comprehention

# def main():
#
#     #define two list of number
#     evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
#     odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
#
#     # TODO : Perform a mapping and filter function on a list
#     evenSquared = list(map(lambda e:e**2,filter(lambda e: e>4 and e<16,evens)))
#     print(evenSquared)
#
#
#     #predicate condition
#     # TODO : Derive a new list of numbers from a given list
#     evenSquared = [e ** 2 for e in evens]
#     print(evenSquared)
#
#     # TODO : limit the items operated on with a predicate conditin
#     oddsSquared = [e ** 2 for e in odds if e>3 and e<17]  #if is the predicate condition
#     print(oddsSquared)
#
#
# if __name__ == "__main__":
#     main()

#=======================================================================================================================
#using variable arguments

# TODO : define a function that takes variable arguments
#
# def addition(*args): #cant do (base,*args)
#     result = 0
#
#     for arg in args:
#         print(arg)
#         result += arg
#     return result
#
#
# def main():
#     # TODO : pass diff args
#     print(addition(5,10,15,20))
#     print(addition(1,2,3,4))
#
#
#     # TODO : pass an existing list
#     newNums = [5, 10, 15]
#     print(addition(*newNums))
#
# if __name__ == "__main__":
#     main()

#=======================================================================================================================
#Lambda functions

#using lambda as in-place function

# def CelsiusToFahrenheit(temp):
#     return (temp * 9/5) + 32
#
# def FahrenheitToCelsius(temp):
#     return (temp-32) * 5/9
#
# def main():
#     ctemps = [0, 12, 34, 100]
#     ftemps = [32, 65, 100, 212]
#
#     # TODO : use Regular function to convert temps
#     print(list(map(CelsiusToFahrenheit, ctemps)))
#     print(list(map(FahrenheitToCelsius, ftemps)))
#
#     # TODO : Use lambdas to accomplish the same thing in-line
#     print(list(map(lambda t:(t* 9/5) + 32, ctemps)))
#     print(list(map(lambda t:(t-32) * 5/9, ftemps)))
#
#
# if __name__ == "__main__":
#     main()

#=======================================================================================================================
#use dictionary comprehentions


# def main():
#     #define a list of temperature values
#     ctemps = [0, 12, 34, 100]
#
#     # TODO : Use a comprehention to build a dictionary
#     tempDict = {t:(t*9/5)+32 for t in ctemps if t <100} #key:value
#     print(tempDict)
#     print(tempDict[12]) #look up for value 12
#
#
#     # TODO : Merge two dictionaries with a comprehentions
#     team1 = {"parth": 24, "Anish": 18,"Sudhir": 58, "Narendra": 7}
#     team2 = {"ravi": 12, "navendu": 88,"ravi b":4}
#     #name:marks
#
#     newTeam = {k:v for team in (team1,team2) for k,v in team.items()} #no more than 2 expns
#     print(newTeam)
#
# if __name__ == "__main__":
#     main()

#=======================================================================================================================
#Class comparision operators


# object.__gt__(self,other)
# object.__ge__(self,other)
# object.__le__(self,other)
# object.__eq__(self,other)
# object.__ne__(self,other)

# Special methods to compare objects to each other

# class Employee():
#     def __init__(self,fname,lname,level,yrsService):
#         self.fname = fname
#         self.lname = lname
#         self.level = level
#         self.seniority = yrsService
#
#     # TODO : implement comparison func by emp level
#     def __ge__(self, other):
#         if (self.level == other.level):
#             return self.seniority >= other.seniority
#         return self.level >= other.level
#
#     def __gt__(self, other):
#         if (self.level == other.level):
#             return self.seniority > other.seniority
#         return self.level > other.level
#
#     def __lt__(self, other):
#         if (self.level == other.level):
#             return self.seniority < other.seniority
#         return self.level < other.level
#
#     def __le__(self, other):
#         if (self.level == other.level):
#             return self.seniority <= other.seniority
#         return self.level <= other.level
#
#     def __eq__(self, other):
#         if (self.level == other.level):
#             return self.seniority == other.seniority
#         return self.level == other.level
#
# def main():
#     #some empls
#     dept = []
#     dept.append(Employee("Parth","Sharma",2,3))
#     dept.append(Employee("Vinay", "Jain", 3, 2))
#     dept.append(Employee("anish", "kumar", 3, 1))
#     dept.append(Employee("ravi", "kumar", 2, 4))
#     dept.append(Employee("Navendu", "Ji", 2, 4))
#
#     # TODO :who is senior?
#     print(dept[0] > dept[2])
#     print(dept[4] < dept[3])
#     print(dept[4] == dept[3])
#
#     # TODO : sort the items
#     emps = sorted(dept)
#     for emp in emps:
#         print(emp.fname)
#
#
# if __name__ == "__main__":
#     main()


#=======================================================================================================================


# list1 = [4,2,6,9]
# list2 = [6,7]
# print(list(set(list1) - set(list2)))


# numbr = [1,4,6,8,10]
# for i, numb in enumerate(numbr):
#     print(i+1,numb)

#=======================================================================================================================
# def second_max(list1,max1,count):
#
#
#     if count == len(list1):
#         return max1
#
#     else:
#         highest = list1[0]
#         for i in list1:
#             if i > highest and i != max1:
#                 highest = i
#         count = count+1
#
#
#         return  (second_max(list1,highest,count))
#
#
#
# list1 = [1, 2, 3, 4, 5, 6, 7]
# max1 =list1[0]
# count =0
#
# print(second_max(list1,max1,count))

import heapq
mylist1 = [1,2,3,4,5,6,7]
larg2=(heapq.nlargest(2,mylist1)[-1])
print(larg2)


#print the 2nd most values in a list

#print python statements