def gcf(num1,num2):
    if num1 > num2:
        num1,num2 = num2,num1
    for x in range(num1,0,-1):
        print (x)
        if num1 % x == 0 and num2 % x ==0:
            return x

print (gcf(18,27))
