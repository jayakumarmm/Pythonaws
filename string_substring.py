str1 = 'ABCDCEDCDC0'
str2 = 'CDC'
def string_substring(str1,str2):
    count = 0
    for i in range(len(str1)):
        if str1[i:i+len(str2)] == str2:
            count +=1
    return count

print (string_substring(str1,str2))

