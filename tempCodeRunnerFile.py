num = int(input("enter a numberr: "))

# if num <=1:
#     print("prime number")
# else:
#     if num == 2:
#         print(" a prime number")
#     else:
#         i = 2
#         while num>i:
#             if num % i ==0:
#                 y = 1
#                 break
#             else:
#                 y = 0
#             i = i+1

#         if y ==0:
#             print("prime number")
#         else:
#             print("not a prime")                    



# #-----------------------------------------------------------------------------------

# num = int(input("enter a number: "))
# fact = 1

# if num<=1:
#     print(num)


# while num>0:
#     fact = fact * num
#     num = num-1
# print(f"factorial is {fact}")    


# #-----------------------------------------------------------------------------
# num = int(input("enter a number: "))

# fact = 1

# for i in range(1,num+1):
#     fact = fact * i
# print(fact)    


# #-----------------------------------------------------------------------------
# #sum of a number of a digit

# num = int(input("enter a number: "))
# digit = 0
# sum = 0
# if num < 10:
#     print(num)
# else:
#     while num>0:
#         digit = num % 10                             
#         sum = sum + digit
#         num = num//10
#     print(sum)    
    
# #---------------------------------------------------------------------------------
# # armstrong number

# num = int(input("enter a number: "))
# check = num
# l = len(str(num))
# digit = 0
# sum = 0

# if num<10:
#     print(num)
# else:
#     while num>0:
#         digit = num%10
#         sum = sum + digit **int(l) 
#         num = num // 10
#     if sum == check:
#         print("armstrong number")
#     else:
#         print(" not a armstrong number")           


# #--------------------------------------------------------------------------------------------
# # reverse of a number a palindrome number

# num = int(input("enter a number"))

# reverse =""

# for i in str(num):
#     reverse = i + reverse
# print(int(reverse))    


# #-----------------------------------------------------------------------------------------

# year = int(input("enter a year: "))

# if (year % 4==0 and year % 400 == 0) or year % 100!=0:
#     print("leap year")
# else:
#     print("not a leap year")
