import random as rd
import string

def genPassword(x):
    chars=string.ascii_letters + string.digits + string.punctuation
    return ''.join(rd.sample(chars, x))

ps = int(input("Enter the length of password: "))
print(genPassword(ps))