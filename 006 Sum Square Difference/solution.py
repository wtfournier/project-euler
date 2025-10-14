def sum_of_the_squares(beginning, end):
    x = 0
    for i in range(beginning, end):
        x = x + (i * i)
    return x

def sum_of_numbers_squared(beginning, end):
    x = 0
    for i in range(beginning, end):
        x = x + i
    x = x * x    
    return x

solution = sum_of_numbers_squared(1, 101) - sum_of_the_squares(1, 101)
print(solution)
