import pylab, numpy

def loadFile():
    inFile = open('julytemps.txt')
    high = []
    low = []
    for line in inFile:
        fields = line.split()
        if len(fields) < 3 or not fields[0].isdigit():
            continue
        else:
            high.append(int(fields[1]))
            low.append(int(fields[2]))
    return (low, high)

highTemps, lowTemps = loadFile()
diffTemps = list(numpy.array(highTemps) - numpy.array(lowTemps))

pylab.plot(range(1,32), diffTemps)
