with open("test_1.txt", "r") as file:
    content = file.read().split("\n")

calories = 0
elves = []
top_elves = []
for _ in content:
    if _:
        calories += int(_)
    else:
        elves.append(calories)
        calories = 0

print(max(elves))  # task 1: 69,912 calories, nice
for _ in range(3):
    top_elves.append(elves.pop(elves.index(max(elves))))

print(sum(top_elves))  # task 2: 208,180 calories
