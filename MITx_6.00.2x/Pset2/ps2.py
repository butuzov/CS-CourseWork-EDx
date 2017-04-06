# 6.00.2x Problem Set 2: Simulating robots

import math
import random

import ps2_visualize
import pylab

##################
## Comment/uncomment the relevant lines, depending on which version of Python you have
##################

# === Provided class Position
class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: number representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        angle = float(angle)

        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))

        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

    def __str__(self):
        return "(%0.2f, %0.2f)" % (self.x, self.y)


# === Problem 1
class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        self.width = width
        self.height = height

        self.tiles = dict()


    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        Coordinates = ( int( pos.getX() ), int( pos.getY() ) )
        self.tiles.update({Coordinates: True })

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        return self.tiles.get( ( int(m), int(n) ), False );

    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        # width * height
        return self.width * self.height

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        return len( self.tiles );

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        x, y = random.uniform(0, self.width -1), random.uniform(0, self.height - 1);

        return Position( x, y )

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        return  0 <= pos.getY() < self.height \
            and 0 <= pos.getX() < self.width;

# === Problem 2
class Robot(object):
    direction = 0;
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        self.room  = room;
        self.speed = speed
        self.direction = random.randrange(360)
        self.setRobotPosition( self.room.getRandomPosition() )


    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self.pos;

    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.direction;

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        self.pos = position
        self.room.cleanTileAtPosition( self.pos );

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.direction = direction;
        return self.direction;

    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        raise NotImplementedError


# === Problem 3
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current
    direction; when it would hit a wall, it *instead* chooses a new direction
    randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """


        n = 0;
        while True:
            possible_new_position = self.getRobotPosition().getNewPosition(
                self.getRobotDirection(), self.speed)


            # print( possible_new_position );
            # print( 'In Room?', self.room.isPositionInRoom( possible_new_position ) )
            # print( 'Dirrection?', self.getRobotDirection() )

            if self.room.isPositionInRoom( possible_new_position ):
                break;

            # this is not valid robo direction.
            # trying to update direction
            self.setRobotDirection( random.randrange(360) )
            n += 1

        self.setRobotPosition(possible_new_position);

# Uncomment this line to see your implementation of StandardRobot in action!
# testRobotMovement(StandardRobot, RectangularRoom)

# Single Random Robot Visualized
# aminate( 1, 1, 10, 10, .5, StandardRobot)

# === Problem 4
def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. StandardRobot or
                RandomWalkRobot)
    """
    # import ps2_visualize
    # anim = ps2_visualize.RobotVisualization(num_robots, width, height)


    trials = []
    for _ in range( num_trials ):
        room = RectangularRoom( width, height );
        robots = [ robot_type(room, speed) for r in range(num_robots) ]

        curr_coverage = 0.0;
        num = 0
        while curr_coverage < min_coverage:
            [ robot.updatePositionAndClean() for robot in robots  ]
            curr_coverage = room.getNumCleanedTiles() / room.getNumTiles()
            num += 1;
            if num > 10000:
                print("fuck");
                break;

        trials.append(num)

    return sum(trials) / len(trials)


# === Optional: Visualizing Robots
# also additional code added to ps2_visualize.py
def aminate( num_robots, speed, width, height, min_coverage, robot_type):

    anim = ps2_visualize.RobotVisualization(num_robots, width, height)
    room = RectangularRoom( width, height );
    robots = [ robot_type(room, speed) for r in range(num_robots) ]

    curr_coverage = 0.0;
    num = 0
    while curr_coverage < min_coverage:
        [ robot.updatePositionAndClean() for robot in robots  ]

        anim.update(room, robots)

        curr_coverage = room.getNumCleanedTiles() / room.getNumTiles()
        num += 1;
        if num > 10000:
            # de inffinite loop protection.
            print("fuck");
            break;

    anim.done()




# === Problem 5
class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random at the end of each time-step.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        n = 0;

        # this is not valid robo direction.
        # trying to update direction
        self.setRobotDirection( random.randrange(360) )

        while True:
            possible_new_position = self.getRobotPosition().getNewPosition(
                self.getRobotDirection(), self.speed)

            if self.room.isPositionInRoom( possible_new_position ):
                break;

            self.setRobotDirection( random.randrange(360) )
            n += 1

        self.setRobotPosition(possible_new_position);

# Single Random Robot Visualized
# aminate( 1, 1, 10, 10, .5, RandomWalkRobot)

def showPlot1(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    """
    num_robot_range = range(1, 11)
    times1 = []
    times2 = []
    for num_robots in num_robot_range:
        print("Plotting", num_robots, "robots...")
        times1.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, StandardRobot))
        times2.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, RandomWalkRobot))
    pylab.plot(num_robot_range, times1)
    pylab.plot(num_robot_range, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()


# showPlot1("Robots", "Robots Number", "Tics Required to clean dirty room")

def showPlot2(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    """
    aspect_ratios = []
    times1 = []
    times2 = []
    for width in [10, 20, 25, 50]:
        height = 300//width
        print("Plotting cleaning time for a room of width:", width, "by height:", height)
        aspect_ratios.append(float(width) / height)
        times1.append(runSimulation(2, 1.0, width, height, 0.8, 200, StandardRobot))
        times2.append(runSimulation(2, 1.0, width, height, 0.8, 200, RandomWalkRobot))
    pylab.plot(aspect_ratios, times1)
    pylab.plot(aspect_ratios, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()

# showPlot2("Cleaning Speed to Shape of the Room Correlation", "Spect Ratio", "Teme/Moves")
