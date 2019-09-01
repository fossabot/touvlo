from numpy import zeros, int64
from numpy.linalg import inv, LinAlgError

# model hypothesis


def h(X, theta):
    return X.dot(theta)


def cost_function(X, y, theta):

    m = len(y)  # number of training examples
    J = (1 / (2 * m)) * ((X.dot(theta) - y).T).dot(X.dot(theta) - y)
    return J


def grad(X, y, theta):

    m = len(y)
    grad = (1 / m) * (X.T).dot(h(X, theta) - y)
    return grad


def predict(X, theta):
    return X.dot(theta)


def normal_eqn(X, y):
    n = X.shape[1]  # number of columns
    theta = zeros((n + 1, 1), dtype=int64)

    try:
        X_T = X.T
        theta = inv(X_T.dot(X)).dot(X_T).dot(y)

    except LinAlgError:
        pass

    return theta
