# def cals(a , b):
#     sum = a + b
#     print(sum)
    
# cals(2, 4)

# def cals(a , b):
#     return a + b

# sum = cals(2, 1)
# print(sum)

# def cals():
#     return "hello"

# sum = cals()
# print(sum)

# def avg(a, b, c):
#     average = (a+b+c)/3
#     print(average)
#     return average

# avg( 3, 3, 9)

# color = ["red", "black", "orange", "purple"]

# def printlen(list):
#     print(list)
    
# printlen(color)

# def fact(a):
#     i = 1
#     n = 1
#     while i < a:
#         p = i + 1
#         n = n * p
#         i += 1
#     print(n)
#     return n
        
# fact(5)
# fact(7)

# def usdinr(a):
#     val = 82 * a
#     print("usd:", a,"inr", val)
#     return val

# usdinr(10)

# def oddoreven(a):
#     if(a%2 == 0):
#         print("EVEN")
#     else:
#         print("ODD")
        
# oddoreven(0)

def fact(a):
    i = 0
    n = 1
    while i < a:
        if(a-1 == 0):
            return
        p = i + 1
        n = n * p
        i += 1
        fact(a-1)    
    print(n)
    
       
    

fact(3)
        
    