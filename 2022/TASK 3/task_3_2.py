with open("text_3.txt", "r") as file:
    rucksacks = file.read().split()

lowercase = {chr(value + 96): value for value in range(1, 27)}
uppercase = {chr(value + 64): value + 26 for value in range(1, 27)}
lookup_table = {**lowercase, **uppercase}

badge_value = 0

for _ in range(100):
    elf_1 = set(rucksacks[0 + _ * 3])
    elf_2 = set(rucksacks[1 + _ * 3])
    elf_3 = set(rucksacks[2 + _ * 3])

    id_badge = elf_1.intersection(elf_2).intersection(elf_3).pop()
    badge_value += lookup_table[id_badge]

print(badge_value)
