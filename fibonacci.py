# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
# Take this opportunity to think about how you can use functions.
# Make sure to ask the user to enter the number of numbers in the sequence to generate.
def fibonacci(n):
    fib = []
    if n == 0 or n == 1:
        fib.append(1)
    if n == 2:
        fib = [1,1]
    if n > 2:
        fib = [1,1]
        for i in range(1,n-1):
            fib.append(fib[i] + fib[i-1])
    return fib

num = int(input("Enter a number: "))
print(fibonacci(num))