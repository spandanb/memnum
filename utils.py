

DICTFILE = 'wordlist.txt' #Dictionary file
MINFILE = 'wordmin.txt'  #Minimized dictionary file
JSDICT = 'wordlist.js'   #Creates js function that returns dictionary object


#Creates a small subset of the dictionary word list to test on
def createMin():
    count = 0
    with open(MINFILE, 'w') as minfile:
        for line in open(DICTFILE):
            if count%100 == 0:
                minfile.write(line)    
            count+=1

#Turns dictionary list to JS array returning function
def dic22json(filename = MINFILE):    
    with open(JSDICT, 'w') as outfile:
        outfile.write("getdict = function(){\n")
        outfile.write("    dict=[\n")
        for line in open(MINFILE):
            outfile.write( "        '{}', \n".format(line.strip()))
        outfile.write( "    ]\n")
        outfile.write( "    return dict;\n")
        outfile.write( "}\n")


if __name__ == '__main__':
    dic22json()