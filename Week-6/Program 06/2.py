def get_factors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

print(get_factors(10)) #output: [1, 2, 5, 10]