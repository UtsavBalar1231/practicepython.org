# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number,
# then tell them whether they guessed too low, too high, or exactly right.
import random as rd

num = rd.randint(1, 9)
choice = int(input("Guess the number: "))
guesses = 1
while (num != choice):
    guesses += 1
    if (choice < num):
        choice = int(input("Enter higher number: "))
    else:
        choice = int(input("Enter lower number: "))

print("Congrats you found the number which was {}".format(num))
print("Number of guesses taken were {}".format(guesses))
