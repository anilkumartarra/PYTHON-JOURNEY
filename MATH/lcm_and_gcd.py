def gcd(a,b):
    if a==0:
        return int(b)
    else:
        return int(gcd(b%a,a))
def lcm(a,b):
    return int((a/gcd(a,b))*b)
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    print(lcm(a,b))  
    print(gcd(a,b))
