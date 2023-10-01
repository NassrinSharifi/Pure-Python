def sum_till(n):
    return n * (n + 1) / 2


sum_of_all_numbers = sum_till(28123)


def IsPrime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def sum_of_divisors(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum


def is_abundant(n):
    if n < sum_of_divisors(n):
        return True


# primes are surely NOT  abundants
abundants = []

for i in range(12, 28123):
    if IsPrime(i) == False:
        if is_abundant(i) == True:
            abundants.append(i)

# print(sum_of_all_numbers)
# print(abundants)
l = []
for i in range(len(abundants)):
    for j in range(i, len(abundants)):
        sum_of_2_abundants = abundants[i] + abundants[j]
        if sum_of_2_abundants <= 28123:
            l.append(sum_of_2_abundants)

l = set(l)
f = sum(list(set(range(1, 28124)) - l))
print(f)
