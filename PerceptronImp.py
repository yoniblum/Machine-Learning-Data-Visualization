import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron
from sklearn.metrics import confusion_matrix


def fit_perceptron(X_train, y_train):
    # Add implementation here
    # weight is the weight coefficients at each run
    weight = np.zeros(X_train[0].size + 1)

    # w holds the coefficients with lowest error
    w = np.zeros(X_train[0].size + 1)

    # keeps track of smallest error
    error = -1

    # add the 1s column in X_train
    ones = np.ones((X_train.shape[0], 1))
    x_train = np.hstack((ones, X_train))

    # pocket algorithm
    for j in range(1000):
        for i in range(x_train.shape[0]):
            # if dot product is positive when it should be negative
            if np.dot(weight, x_train[i]) >= 0 and y_train[i] == -1:
                weight = np.subtract(weight, x_train[i])

            # if dot product is negative when it should be positive
            elif np.dot(weight, x_train[i]) <= 0 and y_train[i] == 1:
                weight = np.add(weight, x_train[i])

        # update w to have the lowest error
        currErr = errorPer(X_train, y_train, weight)
        if currErr < error:
            w = weight
            error = currErr
        elif error == -1:
            w = weight
            error = currErr

    return w


def errorPer(X_train, y_train, w):
    # Add implementation here

    # add the 1s column in X_train
    ones = np.ones((X_train.shape[0], 1))
    x_train = np.hstack((ones, X_train))

    avgError = 0
    for i in range(x_train.shape[0]):
        if pred(x_train[i], w) != y_train[i]:
            avgError += 1
    return avgError


def confMatrix(X_train, y_train, w):
    # Add implementation here

    # add the 1s column in X_train
    ones = np.ones((X_train.shape[0], 1))
    x_train = np.hstack((ones, X_train))

    # confusion matrix is defined as:
    # [true -1, false -1]
    # [false 1, true   1]
    confMatrix = np.zeros((2, 2))

    for i in range(x_train.shape[0]):
        # true -1
        if pred(x_train[i], w) == -1 and y_train[i] == -1:
            confMatrix[0][0] += 1
        # false -1
        elif pred(x_train[i], w) == -1 and y_train[i] == 1:
            confMatrix[0][1] += 1
        # false 1
        elif pred(x_train[i], w) == 1 and y_train[i] == -1:
            confMatrix[1][0] += 1
        # true 1
        if pred(x_train[i], w) == 1 and y_train[i] == 1:
            confMatrix[1][1] += 1
    return confMatrix


def pred(X_train, w):
    # Add implementation here
    pred = np.dot(w, X_train)
    if pred >= 0:
        return 1
    return -1


def test_SciKit(X_train, X_test, Y_train, Y_test):
    # Add implementation here
    clf = Perceptron()
    clf.fit(X_train, Y_train)
    return confusion_matrix(Y_test, clf.predict(X_test))


def test_Part1():
    from sklearn.datasets import load_iris
    X_train, y_train = load_iris(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(X_train[50:], y_train[50:], test_size=0.2)
    for i in range(80):
        if y_train[i] == 1:
            y_train[i] = -1
        else:
            y_train[i] = 1
    for j in range(20):
        if y_test[j] == 1:
            y_test[j] = -1
        else:
            y_test[j] = 1
    # -----------------------------TEST--------------------------------
    # xData = np.array([[1,1],[2,2],[3,3],[4,4],[5,5],[6,6]])
    # yData = np.array([[-1],[-1],[-1],[1],[1],[1]])
    # print(fit_perceptron(xData,yData))
    # -----------------------------------------------------------------
    # Testing Part 1a
    w = fit_perceptron(X_train, y_train)
    cM = confMatrix(X_test, y_test, w)

    # Testing Part 1b
    sciKit = test_SciKit(X_train, X_test, y_train, y_test)

    print("Confusion Matrix is from Part 1a is: ", cM)
    print("Confusion Matrix from Part 1b is:", sciKit)


test_Part1()