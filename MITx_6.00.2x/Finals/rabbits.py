import random
import pylab

# Global Variables

MAXRABBITPOP = 1000

# CURRENTRABBITPOP = 50
# CURRENTFOXPOP = 300

CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30


numSteps = 200

def rabbitGrowth():
    """
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up,
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    RabbitReprProbab = 1 - ( CURRENTRABBITPOP / MAXRABBITPOP );
    ReproductedRabbits = CURRENTRABBITPOP
    for _ in range(ReproductedRabbits):
        if RabbitReprProbab >=  random.random() and 10 < CURRENTRABBITPOP < 1000:
                ReproductedRabbits += 1;
    CURRENTRABBITPOP = ReproductedRabbits
    return


def foxGrowth():
    """
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    FoxEatsProbability = ( CURRENTRABBITPOP / MAXRABBITPOP );
    FoxesSurvived = CURRENTFOXPOP;

    for _ in range(CURRENTFOXPOP):
        if FoxEatsProbability >=  random.random() and CURRENTRABBITPOP > 10:
            CURRENTRABBITPOP -= 1;

            # fox reproduction
            if random.random() <= 1/3 and 10 < CURRENTFOXPOP < CURRENTRABBITPOP:
                FoxesSurvived += 1;

        elif random.random() <= 1/10 and 10 < CURRENTFOXPOP:
            FoxesSurvived -= 1;

    CURRENTFOXPOP = FoxesSurvived


def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """

    Foxes = [];
    Rabbits = [];
    for _ in range(numSteps):
        rabbitGrowth()
        foxGrowth();
        Foxes.append(CURRENTFOXPOP);

        Rabbits.append(CURRENTRABBITPOP);

    return Rabbits, Foxes

# Ploting

rabbits, foxes = runSimulation(numSteps)
pylab.figure(1)

xVals = pylab.array( range( numSteps ) )

pylab.plot(rabbits, 'b', label='Rabbits' )
ar, br, cr = pylab.polyfit( range( numSteps ), rabbits, 2)
est_yvals_f = ar * xVals**2 + br*xVals + cr
pylab.plot( est_yvals_f, 'b.', label='Rabbits - Polyfit Curve' )

pylab.plot(foxes, 'r', label='Foxes' )

af, bf, cf = pylab.polyfit( range( numSteps ), foxes, 2)
est_yvals_f = af*xVals**2 + bf*xVals + cf
pylab.plot( est_yvals_f , 'r.', label='Foxes - Polyfit Curve' )


pylab.legend(loc='best')
pylab.show()
