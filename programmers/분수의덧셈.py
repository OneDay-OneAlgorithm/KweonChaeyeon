# def gcd(a, b):
#     if b == 0:
#         return a
#     else:
#         return gcd(b, a % b)

# def solution(numer1, denom1, numer2, denom2):
#     lcm = denom1 * denom2 // gcd(denom1, denom2)
#     numer = (lcm // denom1 * numer1) + (lcm // denom2 * numer2)
    
#     total_gcd = gcd(numer, lcm)
#     numer //= total_gcd
#     lcm //= total_gcd
#     solution = [numer, lcm]
#     return solution

import math

def solution(numer1, denom1, numer2, denom2):
    numer = numer1 * denom2 + numer2 * denom1
    denom = denom1 * denom2
    
    gcd = math.gcd(numer, denom)
    numer //= gcd
    denom //= gcd
    solution = [numer, denom]
    return solution

print(solution(1, 2, 3, 4))
print(solution(9, 2, 1, 3))
    