# def isFactor(dividend: int, factor: int) -> bool:
#     # finding the quotient
#     quotient = dividend / factor
#     # determine whether the quotient is integer, if yes then return true or otherwise.
#     return quotient == int(quotient)

# def gcd(m: int, n: int):
#     factor_m: list = []
#     factor_n: list = []
#     for i in range(1, max(abs(m), abs(n))+1):
#         if isFactor(m, i):
#             factor_m.append(i)
#         if isFactor(n, i):
#             factor_n.append(i)
#     return max(set(factor_m).intersection(set(factor_n)))

# print(gcd(75, 360)) # Output: 15

# solving problems by recursion
def gcd(m: int, n: int):
    return m if n == 0 else gcd(n, m % n)

print(gcd(75, 360))