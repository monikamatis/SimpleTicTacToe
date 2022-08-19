prime_numbers = [x for x in range(2, 1001) if all(x % n > 0 for n in range(2, x - 1))]
