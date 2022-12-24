with open("text_3.txt", "r") as file:
    rucksacks = file.read().split()

lowercase = {chr(value + 96): value for value in range(1, 27)}
uppercase = {chr(value + 64): value + 26 for value in range(1, 27)}
lookup_table = {**lowercase, **uppercase}
prio_total = 0

for elf in rucksacks:
    compartment_div = len(elf) // 2
    compartment_first = elf[:compartment_div]
    compartment_second = elf[compartment_div:]
    item_share = set(compartment_first).intersection(set(compartment_second)).pop()
    prio_total += (lookup_table[item_share])

print(prio_total)
