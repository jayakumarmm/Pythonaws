a = '1 2 3 4 5 6 7 8 9'
b = '10 1 2 3 11 21 55 6 8'

eng = set([int(x) for x in a.strip().split()])
fre = set([int(x) for x in b.strip().split()])

print (eng)
print(fre)

print (len(eng |fre))










