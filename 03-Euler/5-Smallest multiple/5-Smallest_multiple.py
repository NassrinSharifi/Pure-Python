def becharkh(num, lst):
    for i in lst:
        if num%i==0:
            num=num/i
    return num
number_serie = [x for x in range(2,21)]
to_be_multipled = [2]
for num in number_serie:
    num_to_multi=becharkh(num,to_be_multipled)
    to_be_multipled.append(num_to_multi)
print(to_be_multipled)
result=1
for i in to_be_multipled:
    result*=i
print(result)