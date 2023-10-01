#permutation with repeated items
#we have n "right"s and n "down"s & we want to calculate the permutation
def Facctorial(n):
    n_factorial=1
    for i in range(1,n+1):
        n_factorial *= i
    return n_factorial
n=20
numarator=Facctorial(n*2)
denomirator=(Facctorial(n))**2
num_of_paths=numarator/denomirator
print(num_of_paths)

