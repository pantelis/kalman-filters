def update(mean1, var1, mean2, var2):
    new_mean = (var2 * mean1 + var1 * mean2)/(var1 + var2)
    new_var = 1./((1./var1) + (1./var2))
    return [new_mean, new_var]


def predict(mean1, var1, mean2, var2):
    new_mean = mean1 + mean2
    new_var = var1 + var2
    return [new_mean, new_var]

def kalman(belief_stats, data, measurement_var, motion_var):

    for d in data:
        # Prediction
        belief_stats = predict(belief_stats[0], belief_stats[1],
                               d[1], motion_var)

        print('Prediction Step = ', belief_stats)

        # Measurement Update
        belief_stats = update(belief_stats[0], belief_stats[1],
                               d[0], measurement_var)
        print('Measurement Update = ', belief_stats)

    return(belief_stats)

# data
measurements = [5., 6., 7., 9., 10.]
motion = [1., 1., 2., 1., 1.]

# variance of measurements and motion
measurement_var = 4.
motion_var = 2.

# Initial measurements
mu = 0.
var = 10000.

data = zip(measurements, motion)
init_belief_stats = [mu, var]

belief_stats = kalman(init_belief_stats, data, measurement_var=measurement_var, motion_var=motion_var)

print(belief_stats)
