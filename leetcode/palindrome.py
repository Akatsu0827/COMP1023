def palindrome(n: int) -> bool:
    if n < 0:
        return False
    digits = 0
    temp = n
    while temp >= 10:
        temp //= 10
        digits += 1
    n -= temp * 10 ** digits + temp
    if not digits:
        return n + temp == 0
    return n // 10 == n / 10 and palindrome(int(n // 10))


