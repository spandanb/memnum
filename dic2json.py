

DICFILE = 'wordlist.txt'
MINFILE = 'wordmin.txt'

#Creates a small subset to test on
def createMin():
    count = 0
    with open(MINFILE, 'w') as minfile:
        for line in open(filename):
            if count%100 == 0:
                minfile.write(line)    
            count+=1


def dic22json():
    from __future__ import print_function
    filename = "wordmin.txt"
    f = open("wordlist.js", "w") #Output file
    print( "getdict = function(){", file=f)
    print( "    dict=[", file=f)
    for line in open(filename):
        print( "        '{}', ".format(line.strip()), file=f)
    print( "    ]", file=f)
    print( "    return dict;", file=f)
    print( "}", file=f)
    f.close()



if __name__ == '__main__':
    pass