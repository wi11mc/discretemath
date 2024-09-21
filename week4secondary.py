def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

#to get the user input i will add a input option
num = int(input("what number do you want to factorial"))

#print the answer
result = factorial(num)
print(f"the factorial of {num} is {result}")