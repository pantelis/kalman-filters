import helper

# test 1
world = [['G', 'G', 'G'],
         ['G', 'R', 'G'],
         ['G', 'G', 'G']]
measurements = ['R']
motions = [[0, 0]]
sensor_right = 1.0
p_move = 1.0

p = helper.localize(world, measurements, motions, sensor_right, p_move)

correct_answer = (
    [[0.0, 0.0, 0.0],
     [0.0, 1.0, 0.0],
     [0.0, 0.0, 0.0]])

if p == correct_answer:
    print('Test 1 Passed')

# test 2
world = [['G', 'G', 'G'],
         ['G', 'R', 'R'],
         ['G', 'G', 'G']]
measurements = ['R']
motions = [[0, 0]]
sensor_right = 1.0
p_move = 1.0

p = helper.localize(world, measurements, motions, sensor_right, p_move)

correct_answer = (
    [[0.0, 0.0, 0.0],
     [0.0, 0.5, 0.5],
     [0.0, 0.0, 0.0]])

if p == correct_answer:
    print('Test 2 Passed')
# test 3
world = [['G', 'G', 'G'],
         ['G', 'R', 'R'],
         ['G', 'G', 'G']]
measurements = ['R']
motions = [[0,0]]
sensor_right = 0.8
p_move = 1.0
p = helper.localize(world, measurements, motions, sensor_right, p_move)

correct_answer = (
    [[0.06666666666, 0.06666666666, 0.06666666666],
     [0.06666666666, 0.26666666666, 0.26666666666],
     [0.06666666666, 0.06666666666, 0.06666666666]])

if p == correct_answer:
    print('Test 3 Passed')

# test 4
world = [['G', 'G', 'G'],
         ['G', 'R', 'R'],
         ['G', 'G', 'G']]
measurements = ['R', 'R']
motions = [[0,0], [0,1]]
sensor_right = 0.8
p_move = 1.0

p = helper.localize(world, measurements, motions, sensor_right, p_move)

correct_answer = (
    [[0.03333333333, 0.03333333333, 0.03333333333],
     [0.13333333333, 0.13333333333, 0.53333333333],
     [0.03333333333, 0.03333333333, 0.03333333333]])

if p == correct_answer:
    print('Test 4 Passed')

# test 5
world = [['G', 'G', 'G'],
         ['G', 'R', 'R'],
         ['G', 'G', 'G']]
measurements = ['R', 'R']
motions = [[0,0], [0,1]]
sensor_right = 1.0
p_move = 1.0
p = helper.localize(world, measurements, motions, sensor_right, p_move)
correct_answer = (
    [[0.0, 0.0, 0.0],
     [0.0, 0.0, 1.0],
     [0.0, 0.0, 0.0]])

if p == correct_answer:
    print('Test 5 Passed')

# test 6
world = [['G', 'G', 'G'],
         ['G', 'R', 'R'],
         ['G', 'G', 'G']]
measurements = ['R', 'R']
motions = [[0,0], [0,1]]
sensor_right = 0.8
p_move = 0.5
p = helper.localize(world, measurements, motions, sensor_right, p_move)
correct_answer = (
    [[0.0289855072, 0.0289855072, 0.0289855072],
     [0.0724637681, 0.2898550724, 0.4637681159],
     [0.0289855072, 0.0289855072, 0.0289855072]])

if p == correct_answer:
    print('Test 6 Passed')

# test 7
world = [['G', 'G', 'G'],
         ['G', 'R', 'R'],
         ['G', 'G', 'G']]
measurements = ['R', 'R']
motions = [[0,0], [0,1]]
sensor_right = 1.0
p_move = 0.5
p = helper.localize(world, measurements, motions, sensor_right, p_move)
correct_answer = (
    [[0.0, 0.0, 0.0],
     [0.0, 0.33333333, 0.66666666],
     [0.0, 0.0, 0.0]])

if p == correct_answer:
    print('Test 7 Passed')

#############################################################
# For the following test case, your output should be
# [[0.01105, 0.02464, 0.06799, 0.04472, 0.02465],
#  [0.00715, 0.01017, 0.08696, 0.07988, 0.00935],
#  [0.00739, 0.00894, 0.11272, 0.35350, 0.04065],
#  [0.00910, 0.00715, 0.01434, 0.04313, 0.03642]]
# (within a tolerance of +/- 0.001 for each entry)

colors = [['R', 'G', 'G', 'R', 'R'],
          ['R', 'R', 'G', 'R', 'R'],
          ['R', 'R', 'G', 'G', 'R'],
          ['R', 'R', 'R', 'R', 'R']]
measurements = ['G', 'G', 'G', 'G', 'G']
motions = [[0, 0], [0, 1], [1, 0], [1, 0], [0, 1]]
p = helper.localize(colors, measurements, motions, sensor_right=0.7, p_move=0.8)
helper.show(p)  # displays your answer
