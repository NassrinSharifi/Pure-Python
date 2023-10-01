num_1=input()
num_2=input()
num_1_reverse=int(num_1[2]+num_1[1]+num_1[0])
num_2_reverse=int(num_2[2]+num_2[1]+num_2[0])
numbers=[num_1_reverse,num_2_reverse]
if num_1==num_2:print(num_1,"=",num_2)
else:
    if num_1_reverse < num_2_reverse:
        print(num_1+" < "+num_2)
    else:
        print(num_2+" < "+num_1)

