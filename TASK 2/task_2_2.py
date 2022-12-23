rpc = {"rock": 1, "paper": 2, "scissors": 3}
elf = {"A": "rock", "B": "paper", "C": "scissors"}
man = {"X": 0, "Y": 3, "Z": 6}

with open("text_2.txt", "r") as file:
    games = file.read().split("\n")

tally = 0
for _ in games:
    if _:
        if _[2] == "X":
            points = rpc[(list(rpc.keys())[((rpc[elf[_[0]]] - 1) % 3) - 1])]
        elif _[2] == "Y":
            points = rpc[(elf[_[0]])]
        else:
            points = rpc[(list(rpc.keys())[((rpc[elf[_[0]]] + 1) % 3) - 1])]
        print(_[0], _[2])
        current_game = points + man[_[2]]
        tally += current_game
print(tally)
