from Myro import *
init("com9")
notes = { 0 : "e", 1 : "f", 2 : "f#", 3 : "g",
        4 : "g#", 5 : "a", 6 : "a#", 7 : "b",
        8: "c", 9 : "c#", 10 : "d", 11 : "d#" }
base_key = 2
capo = 0
note_time = 0.25
lowest_note = False
txt = "payphone2.txt" #0.25 F2
#txt = "canon.txt" #0.25 False2
#txt = "call_me_maybe.txt" #0.15 F2
#txt = "mario.txt" #0.15 F2
#txt = ".txt" #.



def isInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def process(ra):
    sequence = ""
    minlen = min(len(s) for s in ra)
    for i in xrange(minlen):
        j = 5
        t = ""
        count = 0
        for r in ra:
            if isInt(r[i]):
                if i + 1 < len(r):
                    if isInt(r[i+1]):
                        w = int(r[i:i+1])
                    else:
                        w = int(r[i])
                if count <= 1:
                    #print(j, w)
                    t = t + trans(j, w)
                    l = len(trans(j, w))
                    count = count + 1
                elif count == 2 and lowest_note:
                    t = t[:-l] + trans(j, w)
                    l = len(trans(j, w))
            j = j - 1
        if(count >= 1):
            sequence = sequence + t + str(note_time) + "; "
    return sequence

def trans(j, w):
    if j > 3:
        total = w + j*5 - 1 + capo
    else:
        total = w + j*5 + capo
    b = str(int(round(total/7, 1))+base_key) + " "
    a = notes[total%12]
    #print(total)
    return(a + b)



## Open the file with read only permit
f = open(txt, "r")

## Read the first line
line = f.readline()#.strip()

## If the file is not empty keep reading line one at a time
## till the file is empty
song = ""
while line:
    #line = line.strip()
    if len(line) > 0:
        if line[0] == 'E' or line[0] == 'e'or line[0] == '|' or line[0] == '-':
            ra = []
            ra.append(line.strip())
            for i in xrange(5):
                ra.append(f.readline().strip())
            song = song + process(ra)
            #print(song)
            #print()
            #f.readline()
            #print(line)
    line = f.readline()
f.close()
#print(song)
s = makeSong(song)
playSong(s)
