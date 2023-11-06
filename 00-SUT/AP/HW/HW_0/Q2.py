n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
# print(numbers)
if n % 2 == 0:
    max_sum = sum(numbers[n // 2:]) - sum(numbers[0:n // 2])
else:
    numbers.pop(n//2)
    # print(numbers)
    n=n-1
    max_sum = sum(numbers[n // 2:]) - sum(numbers[0:n // 2])

print(max_sum)