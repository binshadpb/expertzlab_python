#string functions
#
# a="HELLO WORLD"
# print(a.lower())
# b="hello world"
# print(b.upper())
#
# print(a.split()) #split the string to list
# x=a.split()
# print(x)

# b="hello,world"
# print(b.split(",")) #split string using criteria

# b="hello/world"
# print(b.split("o")) #split string using criteria

# print(",".join(["hello","world"]))  #join of two strings
# a=["welcome","all","thrissur"]
# print(",".join(a))

#reversing of string
# a="thrissur"
# print(reversed(a))
# s=list(reversed(a))
# print(s)


#sorting of string list
# a=["welcome","all","thrissur"]
# print(sorted(a))  #tempory sorted sort() for permenant
# print(a)

#find matching position on first occur find function
# b="hello world"
# print(b.find("w"))
# print(b.find("llo"))
#
# #replace function
#
# print("how are you".replace("how","where"))
# print("how are you honey".replace("h","H"))

#capitalize first character
b = "hello world"
# print(b.capitalize())
# #align a string
# print(b.center(50,"*"))
# #count chara in a string
# print(b.count("l"))
#
# #starts with
# print(b.startswith("h"))
# print(b.endswith("d"))
# print(b.endswith("h"))


# str="Hi world how are you"
#
# low_case=str.lower()
# words=low_case.split()
# new_str=sorted(words)
# print(new_str)
# for i in new_str:
#     print(i)

#strip function

# str=" Hi world how are you "
# print(str, len(str))
#
# s=str.strip()
# print(s,len(s))

mystr="Madam"
low_case=mystr.lower()
rev_str=low_case[::-1]
# print(rev_str)
if low_case==rev_str:
    print("palindrome")