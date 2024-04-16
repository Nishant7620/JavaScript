# num = int(input("enter a numberr: "))

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


#------------------------------------------------------------------------------------------

# for i in range(1,5):
#     for j in range(i):
#         print("*",end="")
#     print()        

#-----------------------------------------------------------------------------------
# Greater Number:

# n1 = 10
# n2 = 30
# n3 = 5

# if n1 > n2 and n1> n3:
#     print("n1 is greater")

# elif n2> n1 and n2> n3:
#     print("n2 is greater")
# else:
#     print("n3 is greater")    

#----------------------------------------------------------------------------------
#write a program to print even number between 100 and 200 using while loop   

# num = 100

# while num<=200:
#     if num % 2 ==0:
#         print(num,end=" ")
#     num +=1    

#-------------------------------------------------------------------------------------------
#string questions

#Write a Python program that prints the length of a string s.

# string = "Hello World"

# length = len(string)
# print(length)
#--------------------------------------------------------------------------------------------
#iterating string  using for loop

# string = "Hello World"

# for i in string:
#     print(i)

#------------------------------------------------------------------------------------------

##Write a Python program that prints the character at index i in the string s. 
#If the index is out of range, the program should print "i is out of range".
#If the string is empty, the program should print "Empty String".

# string = input("enter a string: ")
# indexx = int(input("enter index"))
# if len(string)==0:
#     print("Empty string")
# else:
#     if indexx>len(string):
#         print("out of range")
#     else:
#         print(string[indexx])    

#------------------------------------------------------------------------------------------
#Write a Python Program that prints the reversed version of a string. 
#The program must preserve uppercase and lowercase letters. If the string is empty, print it intact.

# string = "Hello World"
# reverse =""
# if len(string) == 0:
#     print("empty string")
# else:
#     for char in string:
#         reverse = char + reverse
#     print(reverse)

#-----------------------------------------------------------------------------------------------
#Write a Python program that prints the first and last three characters of the string s as a single string. 
#If the string has less than six characters, print an empty string (blank output)

# string = "Hello World"

# if len(string)<=6:
#     print(" ")
# else:
#     first = string[:3]
#     last = string[-3:]

#     print(first)
#     print(last)    


#Write a Python program that prints the string s without the characters located at even indices.
#If the string is empty or only has one character, print it intact

# string = "Hello World"

# if len(string) ==0:
#     print("empty string")
# else:
#     print(string[1::2])    


# string = "Hello World"
# new_char = input("enter new a char: ")

# curr_char =input("current char: ") 

# if curr_char in string:
#     new_string  = string.replace(curr_char,new_char)
#     print(new_string)    
# else:
#     print("no match found")        

#-----------------------------------------------------------------------------------

# string = input("Enter a string: ")

# if string.isnumeric():
#     print("True")
# else:
#     print("False")    


# string = "Hello.World"

# new_string=string.replace(".",",")
# print(new_string)


#----------------------------------------------------------------------------------------


#write a Python program that prints a copy of the string s without any spaces using for loop.
#Words should be connected in the final string.
#If the string doesn't contain spaces, print it intact.


# string = "Hello World"

# for char in string:
#     print(char.replace(" ",""),end="")   


# str = input("enter a string")
# for char in str.replace(" ",""):
#     print(char, end="")


#Write a Python program that checks if the string s starts with the sequence of characters denoted by the variable prefix.

# string =input("enter a string: ")

# sufix = input("enter a sufix: ")
# if len(sufix)> len(string):
#     print("false")

# else:
#     if string.endswith(sufix):
#         print('true')
#     else:
#         print('false')    

#Write a Python program that reverses the individual words in the string s and changes their capitalization.
#Uppercase letters should be printed in lowercase and vice versa.4

# string = input("enter a string: ")

# result = string.swapcase()
# print(result[::-1])

# num = 5

# def recursive(num):

#     if num<=1:
#         return num
#     else:
#         return  num * recursive(num -1)     
       
# print(recursive(num))


#dictionary

# dictionary = {'x':1,'y':'Hello','z':0.9}

# print(dictionary['x'])
# print(dictionary['y'])

# dictionary.clear()

# print(dict(dictionary))

# keys = ['a','b','c']

# default_values = 100

# my_dict = dict.fromkeys(keys,default_values)
# print(my_dict)


# keys = ['a','b','c']

# values = (100,200)

# new_dict = dict.fromkeys(keys,values)
# print(new_dict)

#get()

# my_dict = {'x':1,'y':'Hello','z':0.9}

# result = my_dict.get('x')
# print(result)

# result2 = my_dict.get('a')
# print(result2)

# result3 = my_dict.get('d',0)
# print(result3)


#items 

# my_dict = {'x':1,'y':'Hello','z':0.9}

# items = my_dict.items()
# print(items)

# key = my_dict.keys()

# print(key)

# values = my_dict.values()
# print(values)

# pop = my_dict.popitem()
# print(pop)


# dict1 = {'a':1,'b':2,'c':3}
# dict2 = {'d':4,'e':5}

# dict1.update(dict2)
# print(dict1)


# list1 = [1,2,3,4,5,6]

# print(list1[-2])

#string methods

# string = 'Hello world'

# string1 = 'Hello world'

# print(string+string1)

# print(string *5)

# print(len(string))


#strip method

string = 'Hello world'

# print(string.strip())

# print(string.lstrip())

# print(string.startswith('H'))

# print(string.endswith('d'))

# print('x' in string)


# print(string.upper())
# print(string.casefold())
# print(string.lower())

# print(string.capitalize())

# print(string.title())

# print(string.count("H"))

# print(string.count("x"))


# print(string.find('H'))
# print(string.index('H'))

# print(string[0])

# #split method 

# string2 = "Hello World"

# new_string = string2.split(' ',3)
# print(new_string)


# result = "*".join(string2)
# print(result)



# string2 ="23243222343vddvdfvf"

# print(string2.isdigit())
# print(string2.isnumeric())

# print(string2.isalnum())


# string3 = "Hello World"
# reverse = string3[::-1]

# print(reverse.swapcase())



# string = "Hello World"

# print(string[1])

# print(string[:3])
# print(string[-3:-1])


# list1 = [1,2,3,4,5]
# list1.append(6)

# print(list1)

# list1 = [1,2,3,4,5]

# list2 = [6,7,8,9,10]

# list1.extend(list2)

# print(list1)


# string = "HEllo World"

# new_list = list(string)
# print(new_list)



# list2.insert(2,4)
# print(list2)

# list2.insert(3,5)
# print(list2)

# list2.remove(10)
# print(list2)

# pop=list2.pop()
# print(list2)

# print(pop)

# list2.pop(1)

# print(list2)

# list2 = [6,7,8,9,10]

# index = list2.index(6)
# print(index)


# print(list2[0])

# print(list2.count(3))

# print(len(list2))


# list2.sort()
# print(list2)

# list2.reverse()
# print(list2)


# copy_list = list2.copy()

# print(copy_list)

# list2.pop(2)
# print(list2)
# print(copy_list)

# copy_list.append(100)
# print(copy_list)

# print(list2)

# import copy
# original_list = [1, [2, 3], 4]

# deep_copy = copy.deepcopy(original_list)

# original_list[1][0] = 'X'
# deep_copy[1][1] = 'Y'

# print(original_list)
# print(deep_copy)


# list1 = [3, 1, 2, 5, 6, 2, 7, 9]

# # Iterate over the indices of the list
# for i in range(len(list1)):
#     # Check if the index is odd
    
#     if i % 2 != 0:
#         print(list1[i])


# num = 5

# n1 = 0
# n2 = 1
# n3 = 0

# print(n1,n2,end=' ')

# while num>0:
#     n3 = n1+n2
#     n1 = n2
#     n2 = n3
#     num = num -1
#     print(n3,end=' ')


# for i in range(5,0,-1):
#     for j in range(i):
#             print("*",end="")
#     print()    

# n = 5

# for i in range(1,n+1):
#     print(' ' *(n-i),end='')
#     print('*' * (2* i-1)) 


# list2 = [1,3,6,5,7,2,7,4,2,7,10,43]

# list2.sort()

# print(list2[-2])

# list2 = [1,3,6,5,7,2,7,4,2,7,10,43]

# for i in range(len(list2)):
#     if i % 2==0:
#         print(list2[i])



# dictionary = {'name':"Nishant",'age':24,'city':"Panvel"}


# print(dictionary['name'])
# print(dictionary['age'])


# print(dictionary.items())

# print(dictionary.get('Location','Navimumbai'))

# for key,value in dictionary.items():
#     print(f"{key} : {value}")


# print(dictionary.keys())    

# print(dictionary.values())


# key = {'a','b','c'}

# value = 100

# dic = dict.fromkeys(key,value)

# dic.pop('a')
# dic.popitem()
# print(dic)

# dictionary = {'name':"nishant",'age':24,'city':"Panvel"}

# value_name = dictionary.setdefault('name','Manish')
# print(value_name)

# print(dictionary)


# dict2 = {'location':'NaviMumbai'}

# dictionary.update(dict2)
# print(dictionary)




# dict1 = {'name':'Nishant','age':24,'city':'Panvel'}


# new_key = 'Location'

# value = dict1.pop('city')
# print(value)

# dict1[new_key] = value
# print(dict1)


# dict1 = {'name':'Nishant','age':24,'city':'Panvel'}


# new_value ='NaviMumbai'

# dict1['city'] = new_value
# print(dict1)


# dict1 = {'name':'Nishant','age':24,'city':'Panvel'}


# new_key = 'location'

# value = dict1.pop('city')

# dict1[new_key] = value

# print(dict1)

# dict1 = {'name':'Nishant','age':24,'city':'Panvel'}



# new_value ='Navimumbai'

# dict1['city'] = new_value
# print(dict1)


n = 5
for i in range(1,n+1):
    print(' ' * (n-i), end ='')
    print("*" *(2 * i-1))


# n = 5

# for i in range(1,n+1):
#     print(' ' *(n-i),end='')
#     print('*' * (2* i-1))    


# my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# value_a = my_dict.setdefault('a', 100)
# print(value_a)  # Output: 1 (existing value for key 'a')
# print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}


# value_d = my_dict.setdefault('d',100)
# print(value_d)  # Output: 0 (default value for key 'd')
# print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 0}






my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}


new_key = 'new'

value = my_dict.pop('c')

my_dict[new_key] = value

print(my_dict)


new_value = 5

my_dict['d'] = 5
print(my_dict)