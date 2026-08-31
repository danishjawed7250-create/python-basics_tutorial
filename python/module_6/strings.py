#creating strings
name1 = 'college wallah'

name2 = "physics wallah"

name3 = '''MBA wallah'''

# print(name1, name2, name3)
# print(type(name1))
# print(type(name2))
# print(type(name3))

#indexing in a string 
# print(name1[5])
# print(name2[4])
# print(name3[-5])

#traversing a string
#using for loop
# for i in name1:
#     print(i)
    
#using list comprehension
# list = [char for char in name1]
# for i in list:
#     print(i)
    
#find length of a string
# print(len(name1))
    
#find a char/substring in a string
# print(name1.find('z'))

#slicing in string
# C O L L E G E   W A L L A H
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13

print(name1[8:])
print(name1[8:11])
print(name1[1:6])
print(name1[-10:])
print(name1[-5:-1])