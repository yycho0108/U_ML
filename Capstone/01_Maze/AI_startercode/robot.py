import numpy as np
import random as random
from collections import defaultdict

valid_move = range(-3,3+1)
valid_rot = [-90,0,90]
valid_heading = ['up','right','down','left']


class Robot(object):

    def __init__(self, maze_dim):
        '''
        Use the initialization function to set up attributes that your robot
        will use to learn and navigate the maze. Some initial attributes are
        provided based on common information, including the size of the maze
        the robot is placed in.
        '''

        self.location = [0, 0]
        self.heading = 'up'
        self.maze_dim = maze_dim
        #self.qtable = defaultdict(lambda:[[0.0 for _ in valid_move] for _ in valid_rot])
        self.qtable = defaultdict(lambda:np.full((len(valid_rot),len(valid_move)),1.0))
        
        #q-val = self.qtable[state][rot][move]
        #action = (rot,mov), rot = [-90,0,90], mov = [-3...3]

    def build_input(self,sensors):
        #TODO : determine if location is critical
        return tuple(sensors + [self.heading] + self.location)

    def update(self,rot,mov):
        if rot == -90:
            self.heading = CCW[self.heading]
            pass
        elif rot == 90:
            self.heading = CW[self.heading]

    def next_move(self, sensors):
        '''
        Use this function to determine the next move the robot should make,
        based on the input from the sensors after its previous move. Sensor
        inputs are a list of three distances from the robot's left, front, and
        right-facing sensors, in that order.

        Outputs should be a tuple of two values. The first value indicates
        robot rotation (if any), as a number: 0 for no rotation, +90 for a
        90-degree rotation clockwise, and -90 for a 90-degree rotation
        counterclockwise. Other values will result in no rotation. The second
        value indicates robot movement, and the robot will attempt to move the
        number of indicated squares: a positive number indicates forwards
        movement, while a negative number indicates backwards movement. The
        robot may move a maximum of three units per turn. Any excess movement
        is ignored.

        If the robot wants to end a run (e.g. during the first training run in
        the maze) then returing the tuple ('Reset', 'Reset') will indicate to
        the tester to end the run and return the robot to the start.
        '''
        print self.qtable[self.build_input(sensors)]
        rotation = random.choice(valid_rot)
        movement = random.choice(valid_move)
        self.update(rotation,movement)

        return rotation, movement
