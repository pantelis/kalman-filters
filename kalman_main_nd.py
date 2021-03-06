from matrix import matrix


# Kalman filter function
def kalman_filter(x, P, u, measurements, F, R, H):
    for n in range(len(measurements)):

        # measurement update
        y = matrix([[measurements[n]]]) - H * x
        S = H * P * matrix.transpose(H) + R
        K = P * matrix.transpose(H) * matrix.inverse(S)

        P = (I - (K * H)) * P
        x = x + (K * y)

        # prediction
        x = (F * x) + u
        P = F * P * matrix.transpose(F)
        
    return x, P

measurements = [1., 2., 3.]

x = matrix([[0.], [0.]])  # initial state (location and velocity)
P = matrix([[1000., 0.], [0., 1000.]])  # initial uncertainty
u = matrix([[0.], [0.]])  # external motion
F = matrix([[1., 1.], [0, 1.]])  # next state function
H = matrix([[1., 0.]])  # measurement function
R = matrix([[1.]])  # measurement uncertainty
I = matrix([[1., 0.], [0., 1.]])  # identity matrix

x, P = kalman_filter(x, P, u, measurements, F, R, H)

matrix.show(x)
matrix.show(P)

# output should be:
# x: [[3.9996664447958645], [0.9999998335552873]]
# P: [[2.3318904241194827, 0.9991676099921091], [0.9991676099921067, 0.49950058263974184]]
