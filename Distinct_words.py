sen = 'This is a hello house of hello'
def distinct_words(sen):
    line = sen.split()
    line = set(line)
    count = 0
    for i in range(len(line)):
        count +=1
    print(count)

distinct_words(sen)