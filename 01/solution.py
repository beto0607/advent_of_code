accumulator = 0
max_amount = 0
max_elf = 0
elf = 0
for line in open('input.txt','r'):
    if line == '\n':
        elf+=1
        if accumulator > max_amount:
            max_elf = elf
            max_amount = accumulator
        accumulator = 0
    else:
        accumulator += int(line)
print(max_elf)
print(max_amount)


