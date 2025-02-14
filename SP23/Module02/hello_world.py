
#fname = 'Keshawn' 

# lname = 'Smith'
# full_name = fname + " " + lname
# print('Two separate string: ', fname, lname)
# print('One single string: ', full_name)

# print('Enter name of best friend: ', end=' ')
# best_friend = input()
# print('My best friend is: ', best_friend)

# print("Hello World with Double Quotes") # Double Quotes
# print('Hello World with Single Quotes') # Single Quotes

# my_string = '123' 
# my_int = ('123.0000') 
# print(my_string) 
# # print(my_int)
# A = 10
# B = A + 10
# present = 'Here'
# attendance = 1

# if (present == 'Here ' and attendance == 1):
#     print('Hurray')
# else:
#     print('\----/')

print('Enter between celsius or Fahr: ')
temp_name = input()
if (temp_name == 'F' or temp_name == 'f'):
    print('Enter your value for Fahr: ')
    fahr = int(input())
    fahr_to_cel = (5/9) * (fahr - 32)
    print(fahr_to_cel)
elif (temp_name == 'C' or temp_name == 'c'):
    print('Enter your value for Celsius: ')
    celsius = int(input())
    cel_to_fahr = ((9/5) * celsius) + 32
    print(cel_to_fahr)
else:
    print('Your in the wrong place')