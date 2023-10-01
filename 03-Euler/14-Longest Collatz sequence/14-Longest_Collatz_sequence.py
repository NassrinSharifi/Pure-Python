import time
start_time = time.time()
def Rule(n):
    chain_length = 0
    while True:
        if n == 1:
            break
        elif n % 2 == 0:
            n = n / 2
            chain_length += 1
        else:
            n = 3 * n + 1
            chain_length += 1
    return chain_length + 1

n = 1
longest_chain = 1
starting_num = 1
while n < 1000000:
    if Rule(n) > longest_chain:
        longest_chain = Rule(n)
        starting_num = n
    n += 1
print(starting_num)
print("--- %s seconds ---" % (time.time() - start_time))