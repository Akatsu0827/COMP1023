import time
import sys
from math import floor, ceil
from typing import Callable, Any

sys.set_int_max_str_digits(114514)

def memoize(f: Callable[[int], Any]) -> Callable[[int], Any]:
    memo: list[Any] = [None]
    limit: int = sys.getrecursionlimit()
    limit = floor(limit/2 - 3)
    limit_list: list[Any] = [None] * limit

    def handler(x: int) -> int:
        reps: int = ceil((x - max(limit, len(memo) - 1)) / limit)
        for i in range(reps):
            if memo[len(memo) - 1] is not None or len(memo) - 1 == 0:
                memo.extend(limit_list)
            x_i = len(memo) - 1
            handler(x_i)
        if x - (len(memo) - 1) > 0:
            memo.extend(limit_list)
        if memo[x] is None:
            memo[x] = f(x)
        return memo[x]
    return handler

def timing(f) -> Callable[..., int]:
    def wrap(*args) -> int:
        start = time.time()
        res = f(*args)
        end = time.time()
        print(end - start)
        return res
    return wrap

@memoize
def fibonacci_sequence(n: int) -> int:
    match n:
        case 1 | 2:
            return 1
        case _:
            return fibonacci_sequence(n-1) + fibonacci_sequence(n-2)
    
@timing
def main():
    print(fibonacci_sequence(114514))

if __name__ == "__main__":
    main()