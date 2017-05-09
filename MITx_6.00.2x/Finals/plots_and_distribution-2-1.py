import random, pylab

xVals = []
yVals = []
wVals = []

for i in range(1000):
    xVals.append(random.random())
    yVals.append(random.random())
    wVals.append(random.random())

xVals = pylab.array(xVals)
yVals = pylab.array(yVals)
wVals = pylab.array(wVals)

xVals = xVals + xVals
zVals = xVals + yVals
tVals = xVals + yVals + wVals


pylab.plot(sorted(xVals), sorted(yVals), 'r')
pylab.show()

pylab.plot(zVals, 'r');
pylab.show()

pylab.plot(tVals, 'r');
pylab.show()
