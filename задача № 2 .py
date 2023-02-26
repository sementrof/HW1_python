x1= int(input())
y1= int(input())
x2= int(input())
y2 =int(input())
#если они лежат в одной четверти, значит отличные от нуля(x1 * x2 и y1 * y2)  
if (x1 * x2 > 0) and (y1 * y2 > 0):
    print('YES')
else:
    print('NO')