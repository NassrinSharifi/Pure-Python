num=600851475143
def Is_Prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
largest_prime_so_far=2
for j in range(2,int(num**0.5)+1):
    is_prime=Is_Prime(j)
    if is_prime is True and num%j==0 and j>largest_prime_so_far:
        largest_prime_so_far=j

print(Is_Prime(num))
print(largest_prime_so_far)



