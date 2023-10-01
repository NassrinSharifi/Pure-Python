import time
start_time = time.time()
def n_of_divisors(n):
    count=0
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            count+=2
    if n**0.5 == int(n**0.5):
        count-=1
    return count
def triangle_num_generator(n):
    re=n*(n+1)/2
    return int(re)
i=1
num_of_divisors=0
while num_of_divisors <=500:
    triangle_num=triangle_num_generator(i)
    num_of_divisors=n_of_divisors(triangle_num)
    i+=1
print(triangle_num)
print("--- %s seconds ---" % (time.time() - start_time))



