#lists
#
# a=[]
# b=list()
# print(type(a),type(b))
# str="hello world"
# a=list(str)
# print(a)
# print(a[:5])
# print(a[:5:2])
# print(a[1:15:2])
# print(a[::2])
# l=[1,4,5,8,2,[4,9,6]]
# print(l[5])
# print(l[5][0])  #indexing of 5th element list 0th index

# a=[1,2,3,4]
# b=["one","two"]
# c=a+b
# print(c)
# a[3]="four"
# print(a)
# a.append("five")   #appending elements in list
# print(a)
# a.insert(2,"two")  #adding elements by index
# print(a)
# print(a.index("two"))

# del a   #deleting a list
# print(a)

# a.remove(1) delete first element in the list

#
# del a[2]  # delete element using indexing of list
# print(a)
#
# x=a.pop(2) #DLETE element and return element
# print(x)
# print(a)
#
# a=[1,2,3,4,5]
# b=[6,7,8]
# a.append(b)  #add as a last element
# print(a)
# a.extend(b) #add as list items
# print(a)
# print(a.count(6))  #count the occurence of 6
#
# x=a
# print(x)   #copy or assign

# if 6 in a:
#     print("6 is there in a")   #memebership operator in the list

# v=sorted(a,reverse=true)
# print(v)

# for i in a:
#     print(i)

#
# t=[0,1,2,3,4,5,6,7,8,9,10]
# s=[]
#
# for i in t:
#     s.append(i*i)
# # print(s)
# li=[-10,-20,10,20,-15,30]
# s=[]
#
# for i in li:
#     if i>0:
#         s.append(i)
# print(s)

# li=[45,8,6,89,7,15,35,100]
# li.sort()
# print(li)
# print(li[-1])

# l=["xyz","aba","abcd","1231","sdhbks"]
# count=0
# for i in l:
#     if i[0]==i[-1]:
#         count+=1
# print(count)

#



# l=[10,20,30,20,10,50,10]
# s=[]
# m=[]
# for i in l:
#     if (l.count(i)>1):
#         print("more than 1")
#     else:
#         s.append(i)
#
#
#
# print(s)



#
# l=[10,20,30,20,10,50,10]
# s=[]
# i=0
# for i in l:
#     if i not in s:
#         s.append(i)
# print(s)

####################################################

#aggregate functions
# l=[10,20,30,5,15]
# print(max(l))
# print(sum(l))


###########################
#comprehensive function
# l=[10,-20,9,45,-33]
#
# new=[i for i in l if i>0]
#
# print(new)
#
# eve=[i for i in range(20) if i%2==0]
# print(eve)
#

##############################
#transose of a matrix
m=[[1,2,3,4],
   [5,6,7,8,],
   [9,10,11,12]]
print(m)

a=[]
for j in range(4):
    k=[]
    for i in m:
        k.append(i[j])

    print(k)
    a.append(k)
print(a)

