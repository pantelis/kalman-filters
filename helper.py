import numpy as np


def sense(world, p, Z, pHit):
    pMiss = 1.0 - pHit

    # Posterior
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))

    # Normalization
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s

    return q


def sense2d(world, p, Z, pHit):

    pMiss = 1.0 - pHit
    world = np.array(world)

    # Posterior
    num_cells_x, num_cells_y = np.shape(world)
    q = p
    for i in range(num_cells_x):
        for j in range(num_cells_y):
            hit = (Z == world[i, j])
            q[i, j] = p[i, j] * (hit * pHit + (1-hit) * pMiss)

    # Normalization
    s = np.sum(q)
    for i in range(num_cells_x):
        for j in range(num_cells_y):
            q[i, j] = q[i, j] / s

    return q

def move(p, U, pExact, pOvershoot, pUndershoot):

    # U = U % len(p)
    # q = p[-U:] + p[:-U]

    q = []
    for i in range(len(p)):
        s = pExact * p[(i-U) % len(p)]
        s = s + pOvershoot * p[(i-U-1) % len(p)]
        s = s + pUndershoot * p[(i-U+1) % len(p)]
        q.append(s)
    return q

def move2d(p, U, pExact, pOvershoot, pUndershoot):

    # U = U % len(p)
    # q = p[-U:] + p[:-U]

    # Posterior
    num_cells_x, num_cells_y = np.shape(p)
    q = p
    s = np.zeros_like(q)
    for i in range(num_cells_x):
        for j in range(num_cells_y):
            s[i, j] = (pExact * p[(j-U[1]) % num_cells_x], pExact * p[(i-U[0]) % num_cells_y])
            s[i, j] = [s[i, j] + pOvershoot * p[(i-U[1]-1) % num_cells_y],
                       s[i, j] + pOvershoot * p[(i - U[0] - 1) % num_cells_x]]
            s[i, j] = [s[i, j] + pUndershoot * p[(i-U[1]+1) % num_cells_y],
                       s[i, j] + pUndershoot * p[(i-U[0]+1) % num_cells_x]]
            q[i, j] = s[i, j]
    return q


# The function localize takes the following arguments:
#
# colors:
#        2D list, each entry either 'R' (for red cell) or 'G' (for green cell)
#
# measurements:
#        list of measurements taken by the robot, each entry either 'R' or 'G'
#
# motions:
#        list of actions taken by the robot, each entry of the form [dy,dx],
#        where dx refers to the change in the x-direction (positive meaning
#        movement to the right) and dy refers to the change in the y-direction
#        (positive meaning movement downward)
#        NOTE: the *first* coordinate is change in y; the *second* coordinate is
#              change in x
#
# sensor_right:
#        float between 0 and 1, giving the probability that any given
#        measurement is correct; the probability that the measurement is
#        incorrect is 1-sensor_right
#
# p_move:
#        float between 0 and 1, giving the probability that any given movement
#        command takes place; the probability that the movement command fails
#        (and the robot remains still) is 1-p_move; the robot will NOT overshoot
#        its destination in this exercise
#
# The function should RETURN (not just show or print) a 2D list (of the same
# dimensions as colors) that gives the probabilities that the robot occupies
# each cell in the world.
#
# Compute the probabilities by assuming the robot initially has a uniform
# probability of being in any cell.
#
# Also assume that at each step, the robot:
# 1) first makes a movement,
# 2) then takes a measurement.
#
# Motion:
#  [0,0] - stay
#  [0,1] - right
#  [0,-1] - left
#  [1,0] - down
#  [-1,0] - up

# def localize(colors, measurements, motions, sensor_right, p_move):
#     # initializes p to a uniform distribution over a grid of the same dimensions as colors
#     pinit = 1.0 / float(len(colors)) / float(len(colors[0]))
#     p = [[pinit for row in range(len(colors[0]))] for col in range(len(colors))]
#
#     # >>> Insert your code here <<<
#
#     return p


def show(p):
    rows = ['[' + ','.join(map(lambda x: '{0:.5f}'.format(x), r)) + ']' for r in p]
    print
    '[' + ',\n '.join(rows) + ']'


def localize(world, measurements, motions, sensor_right, p_move):
    num_cells_x, num_cells_y = np.shape(world)
    p = (1./(num_cells_x * num_cells_y)) * np.ones([num_cells_x, num_cells_y])

    # We assume that the size of measurements and motions vectors
    # are identical
    for k in range(len(measurements)):
        p = sense2d(world, p, measurements[k], sensor_right)
        p = move2d(p, motions[k], p_move, 0., 0.)

    return p
