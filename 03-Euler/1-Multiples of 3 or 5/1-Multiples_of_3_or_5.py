i=0
total=0
while i <1000:
    if i %3==0:
        total+=i
    elif i%5==0:
        total+=i
    i+=1
print(total)
# attention: since there is elif and not if, there's no need to eliminate 15s !!
