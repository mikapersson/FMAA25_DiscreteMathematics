
# PART 1)

mod = 36
# base = 3
# order = -1  # initial value

for base in range(1, 36):
    order = 0
    for exponent in range(1, 36):
        diff = (base**exponent-1)/mod
        if diff == 0:
            order = exponent
            break
    print("order of " + str(base) + ": " + str(order))


