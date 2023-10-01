n=int(input())
wds=input().split()
rev_str=""
for i in range(n-1,-1,-1):
    rev_str=rev_str+" "+wds[i]
print(rev_str.lstrip())
