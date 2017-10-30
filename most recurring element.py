str1 = '1235677'
num_list = list(map(int,str1))
print (num_list)
counts = {}
for i in num_list:
    counts[i] = counts.get(i,0)+1
lst = sorted([(k,v) for k,v in counts.items()])
print (lst[0])

