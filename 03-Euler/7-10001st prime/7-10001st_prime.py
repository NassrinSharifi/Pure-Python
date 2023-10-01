def IsPrime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

count_prime = 0
largest_prime_so_far = 1
x = 1
while count_prime < 10002:
    if IsPrime(x) is True:
        count_prime += 1
        largest_prime_so_far = x
    x += 1

print(largest_prime_so_far)
