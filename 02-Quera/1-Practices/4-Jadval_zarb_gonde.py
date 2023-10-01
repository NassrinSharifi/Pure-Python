n=int(input())
for i in range(1,n+1):
    line=[i*x for x in range(1,n+1)]
    string=""
    for num in line:
        string=string+" "+str(num)
    print(string.lstrip(' '))


