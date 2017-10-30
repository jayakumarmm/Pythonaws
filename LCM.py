def LCM(num1,num2):
    if num1 > num2:
        num1,num2 = num2,num1
    for x in range(num2,num2*num1+1,num2):
        if  x % num1 == 0:
            return x
        
print (LCM(3,5))

lst = [3,2,16]
def LCM_lst(lst):
    lst.sort()
    worst = lst[0] * lst[1] * lst[2]
    for x in range(lst[2],worst+1,lst[2]):
        if  x % lst[0] == 0 and x % lst[1]  == 0:
            return x

print (LCM_lst(lst))
