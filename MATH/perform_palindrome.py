given an input number
add the reversed number to the input number and check palindrome or not 
if not add that number to previous number and perform same
def palindrome(n):
    k=str(n)
    l=k[::-1] 
    m=int(l)+int(k)
    s=str(m)
    if(s==s[::-1]):
        return s 
    else:
        return palindrome(s)
n=int(input())
print(palindrome(n))

(or)

def reverse(n):
    k=str(n)
    l=k[::-1] 
    m=int(l)+int(k)
    check=palindrome(m)
    return check
def palindrome(n):
    temp=n
    rev=0
    while n>0:
        p=n%10
        rev=rev*10+p 
        n=n//10
    if temp==rev:
        return rev
    else:
        return reverse(temp)
n=int(input())
print(reverse(n))
