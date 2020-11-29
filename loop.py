#prim number program using whilw loop

# number=int(input("enter the number"))
# i=2
# a=1
# while i<number:
#     if number%i==0:
#         a=0
#     i+=1
#
#
# if a==0:
#     print("Its not a prime number")
# else:
#     print("its a prime number")

#program numbers divisible by 5 or 7 below 100 using while lopp
# n=100
# i=1
# a=1
# while i<n:
#     if ((i%5==0) or (i%7==0)):
#         a=0
#
#         print(i)
#     i+=1

#for lopp programs(for loop executed only in collection (indexing))

# l=[10,50,"hello",20,"world",100]
#
# for i in l:
#     print(i)
#     print("*****")

#for loop program to count odd numbers and even numbers in a list

# l=[1,2,3,4,5,6,7,8,9,10,11,12,13]
# odd=0
# even=0
# for i in l:
#     # print(i)
#     if i%2==0:
#         even+=1
#     else:
#
#         odd+=1
#
# print("odd numbers",odd)
# print("even numbers",even)

#range function implementation

print(list(range(10)))

for i in range(10,50,5):
    print(i)