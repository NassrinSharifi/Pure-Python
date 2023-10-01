def IsPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
tot=0
n=2
while n <2000000:
    if IsPrime(n) is True:
        tot+=n
    n=n+1

print(tot)

