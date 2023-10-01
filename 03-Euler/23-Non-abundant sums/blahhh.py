# def sum_of_divisors(n):
#     sum=0
#     for i in range(1,n):
#         if n%i == 0:
#             sum+=i
#     return sum
#
# abundants=[]
# def is_abundant(n):
#     if n< sum_of_divisors(n):
#         abundants.append(n)
#
#
#
# all_numbers=[i for i in range(12,28123)]
# for n in all_numbers:
#     is_abundant(n)
#
# for i in abundants:
#     for j in abundants:
#         if j>= i:
#             sum_of_2_abundants = i+j
#             if sum_of_2_abundants in all_numbers:
#                 all_numbers.remove(sum_of_2_abundants)
#
#
#
# print(sum(all_numbers))

l=[1,2,3]
for i in l :
 for j in l:
    if j>=i:
        print(i+j)