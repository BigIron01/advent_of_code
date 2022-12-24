rpc = {"rock": 1, "paper": 2, "scissors": 3}
elf = {"A": "rock", "B": "paper", "C": "scissors"}
man = {"X": "rock", "Y": "paper", "Z": "scissors"}

with open("text_2.txt", "r") as file:
    games = file.read().split("\n")

tally = 0
for _ in games:
    if _:
        current = ((((rpc[man[_[2]]]) - 1 - rpc[elf[_[0]]] - 1) % 3) * 3 + rpc[man[_[2]]])
        tally += current

print(tally)  # 11666
