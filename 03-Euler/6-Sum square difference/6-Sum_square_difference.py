n = 100
sum_of_spuares = 0
total = 0
for i in range(n + 1):
    square = i ** 2
    sum_of_spuares += square
    total += i
square_of_total = total ** 2
print(sum_of_spuares)
print(square_of_total)
print(square_of_total - sum_of_spuares)
