# By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
# find the sum of the even-valued terms.

total = 2

num1 = 1
num2 = 2
num3 = 0

#find fibonacci sequence below 4,000,000
while True:
    num3 = num1 + num2
    num1 = num2
    num2 = num3
    if num3 >= 4000000:
        break
    if num3 % 2 == 0:
        total = total + num3

print(total)