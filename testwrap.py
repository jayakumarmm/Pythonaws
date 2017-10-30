string = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
max_width = 5

def wrap(string, max_width):
    str1 = ""
    j = 0
    for i in range(len(string)):
        str1 = str1 + string[j:j+max_width] + '\n'
        j = j+ max_width
    print (str1)

wrap(string, max_width)







