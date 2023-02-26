n =int(input())
a=n%60
if a >=40:
    a2=(n//60)+1
    n=0
    a1=0
else:
    a2=n//60
if (a%10)>=9:
    n =(a//10)+1
    a1=0
else:
    n=a//10
    a1=a%10
print(a1, n ,a2)
