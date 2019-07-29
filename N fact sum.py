n=int(input())
fact=1
for i in range(1,n+1):
    fact=fact*i
sum=n*(n+1)*(2*n+1)//6
if fact%sum==0:
    print("yes")
else:
    print("no")
