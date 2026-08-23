#take 3 positive interger input and print the greatest of them
n1 = int(input("enter number1:"))
n2 = int(input("enter number 2:"))
n3 = int(input("enter number 3:"))

# # if n1 is greatest 
# if n1 > n2 and n1 > n3:
#     print(n1, "is the greatest number")
# # if n2 is the greatest 
# elif n2 > n1 and n2 > n3:
#     print(n2, "is the greatest number")
# # if n3 is the greatest
# else:
#     print(n3, "is the greatest")

#using nested if else
#comparing n1 and n2
if n1 > n2:
    #either n1 or n3 is greatest
    if n1>n3:
        print(n1, "is the greatesr element")
    else:
        print(n3, "is the greatest elemnent")
else:
    #either n2 or n3 is greatest
    if n2>n3:
        print(n2, "is the greatest elemnet")
    else:
        print(n3, "is the greatest element1")