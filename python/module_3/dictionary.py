#create a dictionary phones
phones = {
    "John" : 9845644,
    "Ria"  : 4536974,
    "Joy"  : 5842135
}
#printing the dictionary
# print(phones)

#checking types of dictionary
# print(type(phones))

#checking length of dictionary
# print(len(phones))

#access items of dict
# print(phones["John"])
# print(phones.get("John"))
# print(phones.keys())

#update value in dict
# phones["John"] = 3486485
# print(phones)

#add elements in dict
# phones["Kia"] = 4578904
# print(phones)

# phones.clear() #this will empty the dict
# print(phones)

#printing values of a dict
# for x in phones:
#     print(phones[x])

#nested dict
phones = {
    "Area1" : {
        "x" : 0,
        "y" : 1,
        "z" : 2
    },
      "Area2" : {
            "a" : 3,
            "b" : 4,
            "c" : 5
        }
}         
print(phones["Area1"]["y"])



