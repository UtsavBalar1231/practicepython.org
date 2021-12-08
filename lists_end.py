# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and
# makes a new list of only the first and last elements of the given list.
# For practice, write this code inside a function.

def lists_end(x):
    y = []
    y.extend((x[0], x[-1]))
    return y


a = [5, 10, 15, 20, 25]
print(lists_end(a))
