def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def check_num(*numbers):
    for n in numbers:
        if is_prime(n):
            print("Number {} is prime".format(n))
        else:
            print("Number {} not prime".format(n))

check_num(1, 2, 3, 4, 5)
