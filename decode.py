#by baric

#this is a basic shift chipher the password is shifted +7
#shift -7 to get the password

counter = 0
vals = list('tfzbwlyzljylawhzzdvyk')

###################################################
asciiVals = []
for chars in vals:
    asciiVals.append(ord(chars)-7)

#print(asciiVals)

newVal = []
for c in asciiVals:
    newVal.append(chr(c))

print("".join(newVal))    
