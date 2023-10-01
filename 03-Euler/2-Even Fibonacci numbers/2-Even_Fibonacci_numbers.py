# this code consumes a lot of time...
# def Fibo_until(n):
#     if n==1:
#         num=1
#     if n==2:
#         num=2
#     if n >= 3:
#         num=Fibo_until(n-1)+Fibo_until(n-2)
#     return num
# tot=0
# n=1
# fib_n=Fibo_until(n)
# while n< 4000000:
#     if fib_n%2 != 0:
#         continue
#     else:
#         tot+=fib_n
#     n+=1
# print(tot)
# .................* right code *....................
# fibo: 1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597
#even nums of fibo: 2,8,34,144,610,2584 --> a(n)= 4a(n-1)+a(n-2)
def Even_Fibo(n):
    if n==1:
        num=2
    elif n==2:
        num=8
    else:
        num=Even_Fibo(n-2)+4*Even_Fibo(n-1)
    return num

n=1
tot=0
while Even_Fibo(n)< 4000000:
    tot+=Even_Fibo(n)
    n+=1

print(tot)