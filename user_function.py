#####functions#######
# def sample():
#     """just print something"""  #this is doc string
#     print("Hello World")
# print("outside")
# sample()
# print(sample.__doc__)  #print doc string
#
# print(len.__doc__)

# def add():
#    """adding two numbers"""
#     a=2
#     b=3
#     sum=a+b
#     # print(sum)
#     return sum
#
# print("The sum is :",add())

# del add()                  #deleting function
# print(add())

####calculate average of numbers
#
# def aver(x,y):
#     """function with arguments"""
#     print((x+y)/2)
#     print("average of",x,"and",y,"is",(x+y)/2)
#
# aver(3,4)


#####passing a list ang printing the elements

#
# def printlist(a):
#     for i in a:
#         print(i)
#
# printlist([1,2,3])


##########problem sum of square of 2 and 3 (a+b)^2

# x=int(input("Enter the 1 number"))
# # print(x)
# y=int(input("Enter the 2 number"))
#
# def sum_square(a,b):
#     square=(a*a)+2*a*b    +(b*b)
#     return square
# print(sum_square(x,y))


##############arguments in user defined functions#####

# def man(name,abc,msg="good morning"): #default arguments
#     print(name)
#     print(abc)
#     print(msg)
# man("binu","boy")
# man("binu","boy","good")

#####keyword arguments#######

# def display(a,b):
#     print(a)
#     print(b)
#
# display(b=10,a=5)


############variable length arguments#########
# def emp(*args):
#     print("hello",args)
#     print("good morning all")
# emp("binu","anu","ansu")  #output in tuples

#
# def emp1(*args):
#     for i in args:
#         print("hello",i)
#     print("good morning all")
# emp1("binu","anu","ansu")


######problem sum of numbers##

# def sum(*args):
#     total = 0
#     for i in args:
#         total=total+i
#     print("sum of numbers",total)
#
# sum(10,20,30,40,50)

#####variable length keyword arguments#######
# def man(**args):
#     print(args)
#
# man(name="binu",msg1="welcome",msg2="good morning",msg3=100)
# ##output in dict

# Example
# def man1(**args):
#     print(args["msg3"])
#     print(args["msg2"])
#     print(args["msg1"])
#
# man1(name="binu",msg1="welcome",msg2="good morning",msg3=100)
# def man1(**args):
#     for i,n in args.items():
#         print(i,n)
#
# man1(name="binu",msg1="welcome",msg2="good morning",msg3=100)

####################################problem
# x=int(input("Enter the 1 number"))
# y=int(input("enter the 2 number"))
# z=input("enter the operator")
#
# def add(a,b):
#     return (a+b)
#
# def sub(a,b):
#     return (a-b)

#conditions
# total=0
#
# if z=="+":
#     total=add(x,y)
#     print("sum is ",total)
# elif z=="-":
#     total=sub(x,y)
#     print("difference is",total)
# else:print("invalid operator")

##########recursion##########

###example 1
# def greet():
#     print("hello")
#     greet()
# greet()
##example 2
# import sys
# sys.setrecursionlimit(50) ##limit recursive module
# i=0
# def greet():
#     global i
#     i+=1
#     print("hello",i)
#     greet()
# greet()

#####factorial of a number#####

# def fact(num):
#     if num==0: #boundary condition
#         return 1
#     else:
#         return (num*fact(num-1))
# print("factorial is",fact(3))
#


###########