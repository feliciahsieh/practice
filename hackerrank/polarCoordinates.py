import math
import cmath

a = input()
phi = cmath.phase(complex(a))
r = abs(complex(a))

print("{}\n{}".format(r, phi))
