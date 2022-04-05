def isprime(num):
    if num> 1:
        for n in range(2,num):
            if (num % n) == 0:
                return False
        return True
    else:
        return False


def get_primes(integers):
    for num in integers:
        if isprime(num):
            yield num


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))