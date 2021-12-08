enter = input("Type exit to quit")
while enter != "quit":
    p1 = int(input("Player 1: \nEnter Rock Paper or Scissors [1, 2, 3 respectively]: "))
    p2 = int(input("Player 2: \nEnter Rock Paper or Scissors [1, 2, 3 respectively]: "))
    if p1 == p2:
        print("Tie try again")
    elif (p1 == 1 and p2 == 3) or (p1 == 3 and p2 == 2) or (p1 == 2 and p2 == 1):
        print("Player 1 wins")
    else:
        print("Player 2 wins")