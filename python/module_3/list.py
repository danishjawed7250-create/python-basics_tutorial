fruits = ["apple","banana","kiwi","coconut","cherry"] #create a list
print(fruits) #print a list
# print(type(fruits)) #check type of list
# print(len(fruits)) #check length of list

# #checking if an item is present in the list
# if "banana" in fruits:
#     print("banana is part of the list")
    
# #checking if an item not present in list
# if "cherry" not in fruits:
#     print("cherry is not part of the list")


#indexing the list
# print(fruits[1]) #banana
# print()

#negative indexing
# print(fruits[-3])
# print()
# print(fruits[1:2])

#adding elemnets to a list
# fruits.append("strwbarry")
# print(fruits)

#inserting elemnets to a list
# fruits.insert(1,"mango")
# print(fruits)

#extending elemnts to a list
# fruits2=["grapes","coconut"]
# fruits.extend(fruits2)
# print(fruits)

#removing elemnets from the list
# fruits.remove("apple")
# print(fruits)

# fruits.pop(2)
# print(fruits)

#ssorting the elemnets ina list
# fruits.sort()   #in ascending order 
# print(fruits)

#in descending order
# fruits.sort(reverse=True)
# print(fruits)

#list comprehension
# new_fruits = [fruit for fruit in fruits if "a" in fruit]
# print(new_fruits)

#copy alist
# new_fruits = fruits.copy()
# print(new_fruits)

# nested list
fruits.insert(2, ["kiwi","papaya"])
print(fruits)
print(fruits[2][0])