######SET####
# s=set()   #create set only by this method
# print(type(s))
# s={1,2,"hello"}
# print(s)
# a=set([1,2,3])  #coverting list to set
# print(a)
########################
# a={1,2,3,2,1,5,4}
# print(a)  #dulication of data not allowed
#
# a.add("str")
# print(a)
# a.add(0)   #adding elements
# print(a)
#
# a.update("h","a")   #adding multiple elemenets in a list
# print(a)
#
# a.discard("str")   #removing elements in a set
# print(a)
# a.remove(5)
# print(a)    #removing element in a set(error if element is not in the set
#
# a.pop()
# print(a)   #remove element as random)
#
# # a.clear()
# # print(a)

###########set operations

s1={1,2,3,4}
s2={1,5,3,6}
print(s1 | s2)
print(s1.union(s2))  #union of set

print(s1.intersection(s2))
print(s1 & s2)   #intersection

print(s1-s2) #difference b/w sets

print(s1^s2)  #symmetric difference



