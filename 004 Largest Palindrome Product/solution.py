# Find the largest palindrome made from the product of two $3$ -digit numbers.

palindrome_list = set()

for x in range(1, 1000):
    for y in range(1,1000):
        product = str(x * y)
        if product == product[::-1]:
            palindrome_list.add(int(product))

palindrome_list = sorted(palindrome_list)

print(palindrome_list[-1])