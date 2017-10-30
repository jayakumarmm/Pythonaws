sen = 'This is a hello house of hello'
def count_words(sen):
    line = sen.split()
    counts={}
    print (line)
    for i in line:
        counts[i] = counts.get(i,0)+1
    print(counts)

count_words(sen)