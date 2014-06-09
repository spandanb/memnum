

DICTFILE = 'wordlist.txt' #Dictionary file
MINFILE = 'wordmin.txt'  #Minimized dictionary file
JSDICT = 'wordlist.js'   #Creates js function that returns dictionary object
char2num = {'a':2, 'b': 2, 'c':2, 'd':3, 'e':3, 'f': 3, "g":4, "h":4, "i":4, "j":5, "k":5, "l":1,
            "m":6, "n":6, "o":0, "p":7,"q":7, "r":7, "s":7,"t":8,"u":8, "v":9, "w":9, "x":9, "y":9,"z":9} 


#Creates a small subset of the dictionary word list to test on
def createMin(step=1000):
    count = 0
    with open(MINFILE, 'w') as minfile:
        for line in open(DICTFILE):
            if count%step == 0:
                minfile.write(line)    
            count+=1

#Turns dictionary list to JS array returning function
def dict2json(filename = MINFILE):    
    with open(JSDICT, 'w') as outfile:
        outfile.write("getdict = function(){\n")
        outfile.write("    dict=[\n")
        for line in open(MINFILE):
            outfile.write( "        '{}', \n".format(line.strip()))
        outfile.write( "    ]\n")
        outfile.write( "    return dict;\n")
        outfile.write( "}\n")

#Turns dictionary into a tree, i.e. embedded lists 
def dict2tree(minfile=MINFILE, maxlen=7, null=""):    
    child = lambda : [null]*11 
    root = child()
    ptr = root
    for line in open(minfile, 'r'):
        word = line.strip()
        if len(word) <= maxlen:
            for char in word.strip():
                idx = char2num[char]
                if ptr[idx] == null: ptr[idx] = child()
                ptr = ptr[idx]
            if ptr[-1] == null: ptr[-1] = []
            ptr[-1].append(word)
    return root

def word2num(word):
    return [char2num[char] for char in word]

if __name__ == '__main__':
    #createMin()
    print dict2tree(minfile="test.txt")
    #print dict2tree()