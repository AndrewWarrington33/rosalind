#Given: A positive integer n≤25.

#Return: The value of Fn.

with open('fibonacci/rosalind_fibo.txt', 'r') as input:
    number = int(input.read())

def fibonacci(n):
    a = 0
    b = 1
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n+1):
            c = a + b
            a = b
            b = c
        return b

print(fibonacci(number))