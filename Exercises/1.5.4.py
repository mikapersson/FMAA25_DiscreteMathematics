
# PART 1)

mod = 37
# base = 3
# order = -1  # initial value

for base in range(1, mod):
    order = 0
    for exponent in range(1, mod):
        remainder = (base**exponent-1) % mod
        if remainder == 0:
            order = exponent
            break
    print("order of " + str(base) + ": " + str(order))

  
