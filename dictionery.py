#####dict####
# d={"name":"binu","age":22}
# print(d)
# print(type(d))
#
# print(d["name"])
# print(d.get("name")) #displaying key values
#
# d["name"]="binshad"  #mutable
# print(d)
#
# d["place"]="chenam"  #adding key and values
# print(d)
# d.pop("place")  #removing key and values
# print(d)
#
# d.popitem()
# print(d)       #random removing items
# #
# # del d
# # print(d)
# d.clear()
# print(d)

####################################################
#problem:1
# sampledict={
#     "name": "kelly",
#     "age":25,
#     "salary":8000,
#     "city":"new york"
# }
# print(sampledict)
#
# ret=sampledict.pop("city")
# sampledict["location"]=ret
# print(sampledict)
#

###################################
# d={"a":10,"b":20,"c":30}
# print(d)
# d.update({"place":"chenam","name":"binu"})  #update multiple items
# print(d)


# s={}.fromkeys(["maths","chem","eng"],0)  #giving keys same value
# print(s)
#
# s={}.fromkeys(["maths","chem","eng"],[1,2,3])
# print(s)
#
#
# s={}.fromkeys(("maths","chem","eng"),("hello"))
# print(s)

# s={}.fromkeys("hello",0)
# print(s)

#############functions############
# s={"a":10,"b":20,"c":30}
# print(s)
#
# print(s.items())
# a=s.items()
# print(type(a))
#
# print(s.keys())
# print(s.values())



# s={"a":10,"b":20,"c":30}
#
# for items in s.items():  #iteration
#     print(items)
#
# for i in s.values():
#     print(i)
#
# for i in s.keys():
#     print(i)
#

# l=[(1,2,3),(4,5,6)]
# for a,b,c in l:
#     print(a)
#     print(b)
#
#
# s={"a":10,"b":20,"c":30}
# for k,v in s.items():
#     # print(k)
#     # print(v)
#     print("key is ",k,"value is ",v)
#

#################problem#############
#sum of marks
# d={"maths":10,"chem":50,"english":40}
#
# print(d)
# total=0
# for i,n in d.items():
#     total=total+n
#
# print("toal mark is :",total)


#greatest mark in dic
# large=d["maths"]
#
# for i in d.values():
#     if i>large:
#         large=i
# print("graetest mark is :",large)


#problem(values geater than 2)
#
# d={"a":1,"b":3,"c":5}
# print(d)
# print("new dict")
# #
# for i,n in d.items():
#     if n>2:
#         new[i]=n
# print(new)
#

# new=[k:v for k,v in d.items() if v>2]
# print(new)

###################################### nested dict
# d={101:{"name":"binu","mark":99},
#    102:{"name":"anu","mark":100}}
# print(d)
# print(d[101])
# print(d[101]["name"])
# print(d[101]["mark"])

##########################problem to change varsha's salary to 7000
# sampleDict = {
#      'emp1': {'name': 'John', 'salary': 7500},
#      'emp2': {'name': 'Emma', 'salary': 8000},
#      'emp3': {'name': 'Varsha', 'salary': 6500}
# }
# print("before",sampleDict)
# sampleDict['emp3']['salary']=70000
# print("after",sampleDict)

# for k,v in sampleDict.items():
#     for k1,v1 in v.items():
#         if v1=="varsha":
#             sampleDict[k]["salary"]==70000
# print(sampleDict)

###### problem sum of marks

# studentinfo= {
#    "name" : "anil",
#    "email" : "anil@ddd.com",
#    "marks" : {"sem1" : 100, "sem2" : 200,"sem3" : 300}
# }
#
# print(studentinfo)
# sum=0
# for k,v in studentinfo.items():
#     if k=="marks":
#         for j in v.values():
#             sum=sum+j
# print(sum)
# print(studentinfo["name"],"got",sum,"marks")

###################problem displau name id and total mark

data = {
   "100" : {
       "name" : "anil",
       "email" : "anil@ddd.com",
       "marks" : {"sem1" : 100,"sem2" : 200,"sem3" : 300}
            },
   "101" :{
       "name" : "binil",
       "email" : "binil@ddd.com",
       "marks" : {"sem1" : 200,"sem2" : 200,"sem3" : 300}
            }
        }

# print(data)

#my code

#
# for k1,v1 in data.items():
#     s=0
#     #print(v1)
#     for k2,v2 in v1.items():
#         #print(k2)
#         if k2=="marks":
#             #print(v2)
#
#             for j in v2.values():
#                 s=s+j
#             # print(s)
#     print(k1,v1["name"],v1["email"],s)

########################problem calculat

stud_data={
    "111":{
        "name":"tom",
        "email":"tom@gmail.com",
        "sem":{"sem1":{"sub1":2,"sub2":5,"sub3":8},
               "sem2":{"sub1":7,"sub2":6}}
    },
    "222":{
        "name":"ramu",
        "email":"ramu@gmail.com",
        "sem":{"sem1":{"sub1":8,"sub2":2,"sub3":9},
               "sem2":{"sub1":7,"sub2":6}}
    }
}
#print(stud_data)


#### my code#####
# for id,info in stud_data.items():
#     # print(info)
#     s1=0
#     s2=0
#     for k1,k2 in info.items():
#         # print(k2)
#         if k1=="sem":
#             for i1,i2 in k2.items():
#                 # print(i2)
#                 if i1=="sem1":
#                     for i in i2.values():
#                         s1=s1+i
#                 if i1=="sem2":
#                     for j in i2.values():
#                         s2=s2+j
#
#     print(id,info["name"],info["email"],"sem1 :",s1,"sem2 :",s2)
#


####mentors code

for rollNo, studentInfo in studentData.items():
   # print (studentInfo)
   totalMark= 0
   for key, value in studentInfo.items() :
       if (key == "sem"):
           # print (value)
           for sem, subjects in value.items() :
               # print (sem , subjects)
               for subName, mark in subjects.items():
#                    #print (subName, mark)
                   totalMark=totalMark+mark
   print (rollNo, studentInfo["name"],  studentInfo["email"] , totalMark)

















