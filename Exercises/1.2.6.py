import math

"""Wilhelm Threschows 'solution', doesn't work"""

mod = 209
RHS = 21

M = RHS**(1/3)

while M != math.floor(M):
    RHS = RHS + mod
    M = RHS**(1 / 3)
    print(M)


print(M)