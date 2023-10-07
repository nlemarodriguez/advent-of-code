with open("day1/data.txt") as f:
    lines = f.readlines()

calories_by_elf = []

total = 0

for i, calory in enumerate(lines):
    total += int(calory) if calory != "\n" else 0
    if calory == "\n" or i == len(lines) - 1:
        calories_by_elf.append(total)
        total = 0

# part one
print(max(calories_by_elf))
# part two
print(sum(sorted(calories_by_elf)[-3:]))
