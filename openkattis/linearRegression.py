# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
import numpy as np

def feature_normalize(X):
    '''
    Returns a normalized version of X where
    the mean value of each feature is 0 and the standard deviation
    is 1. This is often a good preprocessing step to do when
    working with learning algorithms.
    '''
    mean_r = []
    std_r = []

    X_norm = X

    n_c = X.shape[1]
    for i in range(n_c):
        m = mean(X[:, i])
        s = std(X[:, i])
        mean_r.append(m)
        std_r.append(s)
        X_norm[:, i] = (X_norm[:, i] - m) / s

    return X_norm, mean_r, std_r
def compute_cost(X, y, theta):
    '''
    Comput cost for linear regression
    '''
    #Number of training samples
    m = y.size

    predictions = X.dot(theta)

    sqErrors = (predictions - y)

    J = (1.0 / (2 * m)) * sqErrors.T.dot(sqErrors)

    return J

def gradient_descent(X, y, theta, alpha, num_iters):
    '''
    Performs gradient descent to learn theta
    by taking num_items gradient steps with learning
    rate alpha
    '''
    m = y.size
    J_history = zeros(shape=(num_iters, 1))

    for i in range(num_iters):

        predictions = X.dot(theta)

        theta_size = theta.size

        for it in range(theta_size):

            temp = X[:, it]
            temp.shape = (m, 1)

            errors_x1 = (predictions - y) * temp

            theta[it][0] = theta[it][0] - alpha * (1.0 / m) * errors_x1.sum()

        J_history[i, 0] = compute_cost(X, y, theta)

    return theta, J_history


F,N = map(int,raw_input().split(" "))
print F,N
x = []
y = []
for n in range(N):
    features = np.array(map(float,re.findall("\d+\.\d+", raw_input())))
    predictors = np.array(features[:F])
    target = features[F:][0]
    x.append(predictors)
    y.append(target)
cov = np.cov(x,rowvar = 0)
print cov



X = data[:, :2]
y = data[:, 2]


#number of training samples
m = y.size

y.shape = (m, 1)

#Scale features and set them to zero mean
x, mean_r, std_r = feature_normalize(X)

#Add a column of ones to X (interception data)
it = ones(shape=(m, 3))
it[:, 1:3] = x

#Some gradient descent settings
iterations = 100
alpha = 0.01

#Init Theta and Run Gradient Descent
theta = zeros(shape=(3, 1))

theta, J_history = gradient_descent(it, y, theta, alpha, iterations)
print theta, J_history
plot(arange(iterations), J_history)
xlabel('Iterations')
ylabel('Cost Function')
show()

#Predict price of a 1650 sq-ft 3 br house
price = array([1.0,   ((1650.0 - mean_r[0]) / std_r[0]), ((3 - mean_r[1]) / std_r[1])]).dot(theta)
print 'Predicted price of a 1650 sq-ft, 3 br house: %f' % (price)


    