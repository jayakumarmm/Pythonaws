stud = {}
line = 'Malika 52 56 60'
line = line.split()
name,scores = line[0],line[1:]
scores = list(map(float,scores))
print (scores)
stud[name] = scores
stud[name] = sum(scores)/len(scores)
print (stud[name])











