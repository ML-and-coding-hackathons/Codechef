import math
def lcm(a, b):
    return abs(a*b) // math.gcd(a,b)

t=lcm(4,6)
s=lcm(t,8)
print(s)