# What is the smallest positive number that is **evenly divisible divisible with no remainder** by all of the numbers from $1$ to $20$ ?

num = 20
done = False

while True:
    for x in range(20, 0, -1):
        if x == 1:
            print(num)
            done = True
            break
        if num % x == 0:
            continue
        else:
            break
    if done:
        break
    num += 1