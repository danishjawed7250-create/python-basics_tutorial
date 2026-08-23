#creating a set 
names = {"sia", "Mai", "Tia"}
# print(names)

#check length of the set
# print(len(names))

#check data type of set 
# print(type(names))

#accsesing items of set
# for x in names:
#     print(x)
    
# check if an item exists in a set
# if "Sia" in names:
#     print("Sia is in the set")

#add elements in set
# names.add("Ria")
# print(names)

#removing element from a set
# names.remove("Ria") #this function will not throw an error if the value is not present in the set 
# print(names)

#joining two sets
s1 = {'a', 'b', 'c'}
s2 = {'d', 'e', 'f'}
print(s1,s2)

# s3 = s1.union(s2)
# print(s3)

s1.update(s2)
print(s1)