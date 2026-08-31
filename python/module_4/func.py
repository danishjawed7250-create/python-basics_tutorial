#write a function that prints hello world

# def printHello():
#     #body of the function
#     print("Hello world!!")
# printHello()


#function which takes 2 numbers as input and return their sum
# def add(n1,n2):
#     print("n1:", n1)
#     print("n2:", n2)
#     sum = n1+n2 
#     return sum
# #positional argument
# print("the sum is", add(3,4))

#default argument
# print("The sum is", add())

#arbitary argument
def addAllNumbers(*args):
    sum = 0
    for i in args:
        sum+=i
    return sum
output = addAllNumbers(1,2,3,4,5)
print("The sum is", output)