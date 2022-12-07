accumulator = 0
max_amount = 0
max_amount2 = 0
max_amount3 = 0
for line in open('input.txt','r'):
    if line == '\n':
        if accumulator >= max_amount:
            max_amount3 = max_amount2
            max_amount2 = max_amount
            max_amount = accumulator
        elif accumulator >= max_amount2:
            max_amount3 = max_amount2
            max_amount2 = accumulator
        elif accumulator >= max_amount3:
            max_amount3 = accumulator
        accumulator = 0
    else:
        accumulator += int(line)

print(max_amount + max_amount2 + max_amount3)
