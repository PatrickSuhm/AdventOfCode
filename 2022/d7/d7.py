
#--- Part 1
lines = open("data.txt", "r").readlines()
cur = []
sizeDict = {}
for l in lines:                                 # build absolute path to every directory
    if "$" in l:
        if "cd /" in l:                         # got to home
            cur = ["/"]
        elif "cd .." in l:                      # move out
            cur.pop(-1)
        elif "cd " in l:                        # move in
            name = l.split()[2]
            cur.append("/"+name)      
    else:
        if l.split()[0] != "dir":               # only care about files
            size = int(l.split()[0])            # file
            for i,c in enumerate(cur):          # add size to every dir in path
                path = "".join(cur[0:i+1])
                if path in sizeDict:
                    sizeDict[path] = sizeDict[path] + size
                else:
                    sizeDict[path] = size
endSum = 0
for k,v in sizeDict.items():
    if v <= 100000:
        endSum += v
print("Part 1:", endSum)

#--- Part 2
usableDiscSpace = 40000000
occupiedDiscSpace = sizeDict["/"]
toBeFreed = occupiedDiscSpace - usableDiscSpace
size = 0
errMin = 1e9
for k,v in sizeDict.items():
    err = v-toBeFreed
    if err > 0 and err < errMin:
        errMin = err
        size = v
print("Part 2:", size)


