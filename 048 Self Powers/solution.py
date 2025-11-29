total = 0

for i in range(1, 1001):
    term = i ** i
    total = total + term

total = str(total)
total = total[-10:]
print(total)