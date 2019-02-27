#=============================================================
#Truth value testing
#strings and bytes are not directly interchnageble
#strings contain unicod, bytes are raw 8-bit values

# def main():
#     b = bytes([0x41,0x42,0x43,0x44])
#     print(b)
#
#
#     s = "this is a string"
#     print(s)
#
#     #try to combine
#     s2 = b.decode('utf-8')
#     print(s+s2)
#     b1 = s.encode('utf-8')
#     print(b+b1)
#
#     #utf-32
#     b2 = s.encode('utf-32')
#     print(b2)
#
# if __name__ == '__main__':
#     main()

#=============================================================
#string vs bytes
# demo template string functions
#types of string formatting

# from string import Template
#
# def main():
#     my_str = "you are watching {0} with {1}".format('Ai probably','parth sharma')
#     print(my_str)
#
#     #TODO : create a template with place holder
#
#     templ = Template("You are watching ${title} by ${author}")
#
#
#     #TODO :use the substitute method with keyword arguments
#     str2 = templ.substitute(title = 'Ai probably', author='parth sharma') #template strings
#     print(str2)
#
#     #TODO : use the substitute method with dictionary
#     data = {
#         "title":"ai probably",
#         "author":"parth sharma"
#     }
#     str3 = templ.substitute(data)
#     print(str3)
#      print('it is {}'.format(str3)
#
# if __name__ == '__main__':
#     main()

#=============================================================

#template strings
#python built in funtions
# any() , all(), min(),max(),sum()

# def main():
#     #use any() and all() to test sequences for boolean values
#     list1 = [1, 2, 3, 4, 5, 6]
#
#     #TODO : any will return true if any of the sequences values are true
#     print(any(list1))
#
#     #TODO : all will return true if all values are true
#     print(all(list1)) #false because 0
#
#     #TODO : min an max will return minimum and max values in a sequence
#     print(min(list1))
#     print(max(list1))
#
#     #TODO : use sum() to sum all up in a sequence
#     print(sum(list1))
#
#
# if __name__ == "__main__":
#     main()

#=============================================================

# utilities
# use iterator functions like enumerate, zip, iter, next

# def main():
#     days = ["sun","mon","tue","wed","thu","fri","sat"]
#     daysFr = ["dim","lun","mar","mer","jeu","ven","sam"]
#
#     #TODO : use iter to create an iterator over a collection
#     i = iter(days)
#     print(next(i))
#     print(next(i))
#     print(next(i))
#
#     #TODO : iterate using a function and a sentinel
#     with open("testfile.txt","r") as fp:
#         for line in iter(fp.readline,''):  #' ' is called sentinal value
#             print(line)                    # when ' ' is seen stop
#
#
#
#     #TODO : use regular interation over a days
#     # for m in days:
#     #     print(m)
#     # for m in range(len(days)):
#     #     print(m+1,days[m]) #try m
#
#
#
#     #TODO : using enumerate reduces code and provides a counter
#     for i,m in enumerate(days, start=1):
#         print(i,m)
#
#     #TODO : using zip to combine sequences
#     # for m in zip(days,daysFr):
#     #     print(m)
#     for i,m in enumerate(zip(days,daysFr),start=1):
#         print(i,m[0], '=', m[1], 'in french')
#
#
#
#
# if __name__ == "__main__":
#         main()

#=============================================================

#python iterators
# use transform functions like sorted , filter ,map
def filterFunc(x):
    if x % 2 == 0:
        return False
    return True

def filterFunc2(x):
    if x.isupper():
        return False
    return True

def squarefunc(x):
    return x**2

def toGrade(x):
    if (x>=90):
        return "A"
    elif (x>= 80 and x<90):
        return "B"
    elif (x>= 70 and x<80):
        return "C"
    elif (x>= 65 and x<80):
        return "D"
    else:
        return "F"


def main():
    #some sample sequence
    nums = (1, 8, 4, 5, 13, 26, 381, 410, 58, 47)
    chars = "abcdeFghIJklmnopQrsTuvWxyz"
    grades = (81, 89, 94, 78, 61, 66, 99, 74)

    #TODO : use filter to remove items from a list
    odds = list(filter(filterFunc,nums))
    print(odds)

    #TODO: use filter on non-numeric sequence
    lowers = list(filter(filterFunc2,chars))
    print(lowers)

    #TODO : use map to create a new sequence of values
    sqaures = list(map(squarefunc,nums))
    print(sqaures)

    #TODO : use sorted and map to change numbers to grades
    grades = sorted(grades)
    letters = list(map(toGrade,grades))
    print(letters)


if __name__ == '__main__':
    main()


















































