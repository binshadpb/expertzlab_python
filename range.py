#program to check prime number or not using for loop

# num=int(input("Enter your number"))
# a=1
# for i in range(2,num):
#     if(num%i==0):
#         a=0
# if a==0:
#     print("not a prime number")
# else:
#     print("its a prime number")

#break statement demo

# n=[1,2,3,4,5,10,45]
#
# for i in n:
#     if i==4:
#         break
#     else:
#         print(i)

#continue demo
# n=[1,2,3,4,5,10,45]
#
# for i in n:
#     if i==4:
#         continue
#     print(i)

# braek using prime number

# num=int(input("Enter your number"))
# # a=1
# for i in range(2,num):
#     if(num%i==0):
#         print("its not a prime number")
#         break
# else:
#     print("its a prime number")

a="hello World"
b=" welcome"

print(a)
print(a[6])
print(a[:])
print(a[1:4])
print(a[1:4:2])

print(a[-1])
print(a[-3:-1])
print(a[::-1]) #reverse a string

a=a+b  #concatenate 2 strings
print(a)

for i in a:
    print(i)

print("i" in  a)  #membership operator