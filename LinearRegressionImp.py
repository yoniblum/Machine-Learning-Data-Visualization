import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_diabetes
from sklearn import linear_model
from sklearn.metrics import mean_squared_error



def fit_LinRegr(X_train, y_train):

    X = np.array(X_train)  # making a copy of input matrix which has the dimensions Nxd
    col_of_ones = np.ones((X.shape[0], 1))  # making an Nx1 matrix filled with ones
    X_with_ones = np.hstack((col_of_ones, X))  #inserting column of ones into array
    X_transposed = np.transpose(X_with_ones)

    P = np.dot(X_transposed, X_with_ones) # d+1xN x Nxd+1 = d+1xd+1

    Pinv = np.linalg.inv(P) # d+1xd+1 (SAME DIMENSIONS)

    Q = np.dot(Pinv, X_transposed)  # d+1xd+1 x d+1xN = d+1xN (I hope)

    Y = np.array(y_train) # Nxd+1


    w = np.dot(Q, Y) #final weight vector

    return w

def mse(X_train,y_train,w):
    #w is a d+1 x 1 matrix
    #X_train is an Nxd+1 matrix

    #Filling up x with a column of ones

    X = np.array(X_train)  # making a copy of input matrix which has the dimensions Nxd
    col_of_ones = np.ones((X.shape[0], 1))  # making an Nx1 matrix
    X_with_ones = np.hstack((col_of_ones, X))
    N=y_train.shape[0]

    #putting y_train in array form

    Y=[]
    for i in range(N):
        Y.append(y_train.item(i))

    #creating the prediction function, while simultaneously calculating the mean squared error

    yhat = []
    current_num = 0
    sum = 0

    for i in range(N): #from 0 to N-1
        #yhat.append(np.dot(X_with_ones[i],w)) This line does the same thing as the next line
        yhat.append(pred(X_with_ones[i],w))
        current_num=(yhat[i]-Y[i])*(yhat[i]-Y[i])
        sum+=current_num


    return sum/N





def pred(X_train,w):


    #prediction function is w^T * Xi
    #Both Xi and w are vectors of length d+1


   return np.dot(np.transpose(w),X_train)



def test_SciKit(X_train, X_test, Y_train, Y_test):

   #scikit implementation of linear regression

    regression = linear_model.LinearRegression()
    regression.fit(X_train, Y_train)  # training the algorithm

    y_prediction = regression.predict(X_test)


    return mean_squared_error(Y_test, y_prediction)


def testFn_Part2():


    X_train, y_train = load_diabetes(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(X_train,y_train,test_size=0.2)

    #Testing Part 2a

    w=fit_LinRegr(X_train, y_train)
    e=mse(X_test,y_test,w)

    #Testing Part 2b
    scikit=test_SciKit(X_train, X_test, y_train, y_test)

    print("Mean squared error from Part 2a is ", e)
    print("Mean squared error from Part 2b is ", scikit)

testFn_Part2()

