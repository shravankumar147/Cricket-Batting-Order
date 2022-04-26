from random import shuffle

# select number of players
n = int(input("Enter Number of Players(Example: 10)\n : "))

players = list(range(1, n + 1))

shuffle(players)

# print(players)

while players:
    text = input("Next Player")  # or raw_input in python2
    if text == "":
        print(f"your batting order: {players.pop(0)}")
    else:
        print("you typed some text before pressing enter")
