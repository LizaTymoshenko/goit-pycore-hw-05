from typing import Callable

def caching_fibonacci() -> Callable[[int], int]:
    """Caching function for fibonacci numbers"""
    cache = {}
    # fibonacci func
    def fibonacci(n: int) -> int:
        """Function to calculate fibonacci numbers. Previously calculated numbers are cached."""
        # check if the number is in allowed range
        if n > 1004:
            print('Maximum recursion depth exceeded. Please try smaller number. Up to 1004-th fibonacci number allowed.')
            return 0
        # check if number is cached
        elif not cache.get(n):
            if n <= 0:
                cache[n] = 0
            elif n == 1:
                cache[n] = 1
            else:
                # calc fibonacci number if not cached yet
                cache[n] = fibonacci(n-1) + fibonacci(n-2)
        return cache[n]
    return fibonacci

if __name__ == "__main__":

    fib = caching_fibonacci()
    
    print(fib(1))
    print(fib(4))
    print([fib(n) for n in range(1,11)])
    print(fib(11))
    print(fib(1005))

    print(fib(10))  # Виведе 55
    print(fib(15))  # Виведе 610
