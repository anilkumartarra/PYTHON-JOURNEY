#print(ord('1')-ord('0'))
def factorial(n):
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)
#factorial=[1,1,2,6,24,120,720,5040,40320,362880]
def isstrongnumber(n):
    s=str(n)
    sum=0
    for i in range(len(s)):
        sum+=factorial(ord(s[i])-ord('0'))
    if sum==n:
        return 1
    else:
        return 0
def strongnumbers(n):
            if i in range(1,n+1):
                if(isstrongnumber(i)):
                    print(i,end=" ")
n=int(input())
for i in range(n):
    strongnumbers(i)


