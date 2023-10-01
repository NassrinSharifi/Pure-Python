import re
fname=input("Enter filename:")
if len(fname)<1:
    fname="regex_sum_1375311.txt"
total=0
fhandle=open(fname)
for line in fhandle:
    line.rstrip()
    numbers=re.findall('[0-9]+', line)
    for n in numbers:
        total+=int(n)

print(total)