def sum_1to_N(n):
    
    #base case 
    if n==1:
        return 1
    
    #recursive case
    ans = n + sum_1to_N(n-1)
    return ans 

n = int(input("enter n:"))
print(sum_1to_N(n))