# Write a program (function!) that takes a list and returns a new list
# that contains all the elements of the first list minus all the duplicates.
def removeDuplicates(x):
    # y = []
    # [y.append(i) for i in x if i not in y]
    # return y
    return list(set(x))

list1 = [1, 1, 2, 2, 3, 4, 5, 5, 6, 6, 6, 7, 7]
print(removeDuplicates(list1))
