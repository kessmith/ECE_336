# Write a Python program to compute the sum of two given integer values. 
# If the two values are the same, then return triple their sum.

# a = 2
# b = 4

# if (a == b):
#     print(3 * (a + b))
# else:  
#     print(a + b)

# Write a Python program to find the sum of the 
# first 10 natural numbers.
#The first 10 natural number is: 1,2,3,4,5,6,7,8,9,10

# Set the value:
n = 10

# Initialize the sum to 0
total_sum_result = 0

for i in range(1, n+1):
    total_sum_result +=1

print(total_sum_result)

temp = int(input('Enter temperature value: '))
degrees = input('Enter degree aka. unit: ') # F or C

