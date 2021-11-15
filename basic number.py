n=int(input())
e=0
m=0
c=0
while n:
    c+=1
    d=n%10
    n=n//10
    if d%2==0:
        
        e=e+1
    
    else :
        
        m=m+1
if e==c:
    print("even")
elif m==c:
    print("odd")
else:
    print("mixed")

