#!/usr/bin/env python
# coding: utf-8

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix 
from sklearn.datasets import load_iris

def fit_NeuralNetwork(X_train,y_train,alpha,hidden_layer_sizes,epochs):
    weights = []
    err = []
    shuffler = np.arange(len(y_train)).tolist()
    X_train = np.hstack((     np.ones((len(y_train),1))    ,   X_train     ))

    # set of weights connecting input layer to first hidden layer
    a = np.zeros((len(X_train[0]),hidden_layer_sizes[0]))
    b = np.full_like(a,0.1,dtype=float)
    weights.append(b.tolist())

    # set of weights connecting each hidden layer nodes
    # hidden_layer_sizes[i]+1 is used to account for bias node
    for i in range(len(hidden_layer_sizes)-1):
        a = np.zeros((hidden_layer_sizes[i]+1,hidden_layer_sizes[i+1]))
        b = np.full_like(a,0.1,dtype=float)
        weights.append(b.tolist())

    # set of weights connecting last hidden layer to the single node in the output layer
    a = np.zeros((hidden_layer_sizes[-1]+1,1))
    b = np.full_like(a,0.1,dtype=float)
    weights.append(b.tolist())

    # print('the initial weights are: ', weights)
    # print()
    for i in range(epochs):
        # print('EPOCH NUMBER: ', i)
        # print()
        # selects a random training point
        np.random.shuffle(shuffler)
        # print('current weights are: ', weights)
        # print()
        # the forward pass
        x,s = forwardPropagation(X_train[shuffler[0]],weights)

        # the backwards pass
        g=backPropagation(x,y_train[shuffler[0]],s,weights)
        # print('gradients are: ', g)
        # print()
        # update the weights
        weights=updateWeights(weights,g,alpha)
        # print('new weights are: ', weights)
        # print()
        # record the error at each epoch
        err.append(errorf(x[-1][0][0],y_train[shuffler[0]]))

    return err,weights
# this function wasn't originally here
def forwardPropagation(X, weights):
    # x is the output at all nodes in all layers
    x = []
    x.append(X)
    # s is the input of all nodes in all layers
    s = []

    # number of elements in weights[L] represents the number of nodes in layer L
    # number of elements in weights[L][i] represents the number of nodes in layer L+1
    # number of elements in weights represents the number of layers minus 1
    for i in range(len(weights)): 
        outputs = []
        inputs = []
        # elements in 'a' are arrays of incoming edge weights going into a single node in layer L+1
        a = np.transpose(weights[i]) 

        # finds the inputs/outputs in each node of layer L+1, starting at the input layer
        # each 'j' in 'a' has dimension d^(L) + 1, where d is numOfNodes(L)
        # the first given input in x is X, which has dimension d + 1       
        if i<len(weights)-1:
            outputs.append(1)
            for j in a:
                b = np.dot(j,x[i]) 
                inputs.append(b)
                outputs.append(activation(b))
        # this is the last layer (output layer), containing a single node
        else:
            b = np.dot(a,x[i])
            inputs.append(b)
            outputs.append(outputf(b))

        # s will now have the inputs for the next layer
        x.append(outputs)
        s.append(inputs)
    return x,s

def errorPerSample(X,y_n):  
    return errorf(X[-1][0], y_n)

def backPropagation(X, y_n, s, weights):
    g=[] #vector full of gradients for each weight
    backward_message=[]

    lastVectorinX = X[-1]
    lastVectorinS = s[-1]
    
    delta_L=derivativeError(lastVectorinX[0], y_n) * derivativeOutput(lastVectorinS[0])
    backward_message.insert(0,delta_L)
    
    for num in range(len(weights)-1):
        backward_message.insert(0,0)
    
    for layer in range(len(weights)-2,-1,-1):
        
        backpropagation_vector=backward_message[layer+1] #could be integer,float, double or array
        #print("backpropagation_vector for this layer is: ",backpropagation_vector)
        V=[]#backward message vector for this layer
        
        for nodei in range(1,len(weights[layer+1])):
            current_activation_derivative=derivativeActivation(s[layer][nodei-1])
            current_weight_vector=weights[layer+1][nodei]
        
            width=0
            if type(current_weight_vector)==int or type(current_weight_vector)==float:
                width=1
            else: #if the current weight vector is actually a vector
                width=len(current_weight_vector)
                       
            if width==1: #if there is only one node where the weights go (ie. on the last iteration)
                #print("number we're looking for for this node is: ",backpropagation_vector*current_activation_derivative*current_weight_vector)
                V.insert(2,backpropagation_vector*current_activation_derivative*current_weight_vector)
            else:#if there is more than one node in the next layer (besides bias)
                V.insert(width+1,current_activation_derivative*np.dot(current_weight_vector,backward_message[layer+1]))

            backward_message[layer]=V
   
    for k in range(len(backward_message)):
            if type(backward_message[k])!=list:
                backward_message[k]=[k]
                # print("flag2")
                
    for asdf in backward_message:
            if type(asdf)!=list:
                # print("flag1")
                None
    backward_message[-1]=[delta_L]
                  
    for i in range(len(backward_message)): #take care of scenarios where there might be only one node
        current_matrix=[]
        for abc in range(len(X[i])):
            current_row=[]
            for defg in range(len(backward_message[i])):
                current_row.append(float(X[i][abc]*backward_message[i][defg]))
            current_matrix.append(current_row)
        g.append(current_matrix)
            
    return g
def updateWeights(weights,g,alpha):
    for i in range(len(weights)):
        b=np.full_like(g[i],alpha,dtype=float)
        c=np.multiply(g[i],b)
        weights[i]=np.subtract(weights[i],c).tolist()
    return weights

def activation(s):
    # ReLU function, ReLU(x) = max(0,x)
    if s<0:
        return 0
    return s

def derivativeActivation(s):
    # ReLU'(x) = {0, x<0}
    #            {1, x>0}
    # shouldnt it be undefined at 0? because RelU'(0-) != ReLU'(0+)
    if s>0:
        return 1
    return 0

def outputf(s):
    # sigmoid function f(x) = 1/(1+e^-x)
    return 1/(1+np.exp(-s))

def derivativeOutput(s):
    # derivative of sigmoid f'(x) = e^-x/(1+e^-x)^2
    return np.exp(-s)/(1+np.exp(-s))**2
    
def errorf(x_L,y):
    # the log loss error function

    # a = (y==1) ? np.log(x_L) : 0
    a = np.log(x_L) if y==1 else 0
    # b = (y==-1) ? np.log(1-x_L) : 0
    b = np.log(1-x_L) if y==-1 else 0
    return -a-b
def derivativeError(x_L,y):

    a = 1/x_L if y==1 else 0
    b = -1/(1-x_L) if y==-1 else 0
    return -a-b

def pred(x_n,weights):
    # run through forwardPropagation once and check its result
    if forwardPropagation(np.hstack((1, x_n)),weights)[0][-1][0] >= 0.5:
        return 1
    return -1

def confMatrix(X_train,y_train,w):
    # confusion matrix is defined as:
    # [true -1, false -1]
    # [false 1, true   1]
    confMatrix = np.zeros((2, 2),dtype=int)

    for x,y in zip(X_train,y_train):
        # true -1
        if pred(x, w) == -1 and y == -1:
            confMatrix[0][0] += 1
        # false -1
        elif pred(x, w) == -1 and y == 1:
            confMatrix[0][1] += 1
        # false 1
        elif pred(x, w) == 1 and y == -1:
            confMatrix[1][0] += 1
        # true 1
        if pred(x, w) == 1 and y == 1:
            confMatrix[1][1] += 1
    
    return confMatrix


def plotErr(e,epochs):
    plt.plot(np.arange(epochs),e)
    plt.show()
    return 1
    
def test_SciKit(X_train, X_test, Y_train, Y_test):
    m = MLPClassifier(solver='sgd', alpha=0.00001, hidden_layer_sizes=(300, 100), random_state=1)
    m.fit(X_train, Y_train) #fitting training data to NN
    y_hat = m.predict(X_test) #y_hat prediction based on X_test
    
    cM = confusion_matrix(Y_test, y_hat) #confusion matrix from prediction value and test values

    return cM
def test():
    #----------------my test(fit neural network initializes correct weights)---------------------------------
    # X_train, y_train = load_iris(return_X_y=True)
    # print(len(fit_NeuralNetwork(X_train,y_train,1e-2,[3, 2],100)[0])/3)
    #--------------------------------------------------------------------------------------------------------
    #----------------test forwardProp, backprop, update weights----------------------------------------------
    # x=[1,0.2,-0.5,0.3] # a 4x1 vector

    # w0=[[1,-1],[3,4],[1,-2],[-2,3]]
    # w1=[[1,0.4,-2],[0.3,1,1],[-1,0.5,-1]]
    # w2=[-0.2,3,1,0.5]
    # weights=[w0,w1,w2]

    # y_n=1

    # xout,sout=forwardPropagation(x, weights)

    # g=backPropagation(xout, y_n, sout, weights)
    # alpha=0.1
    # print(g)
    # print(updateWeights(weights,g,alpha))
    #--------------------------------------------------------------------------------------------------------
    #-------------------------test fitneuralnetwork----------------------------------------------------------
    # X_train, y_train = load_iris(return_X_y=True)
    # X_train, X_test, y_train, y_test = train_test_split(X_train[50:],y_train[50:],test_size=0.2)
    # for i in range(80):
    #     if y_train[i]==1:
    #         y_train[i]=-1
    #     else:
    #         y_train[i]=1
    # for j in range(20):
    #     if y_test[j]==1:
    #         y_test[j]=-1
    #     else:
    #         y_test[j]=1
    # err,w=fit_NeuralNetwork(X_train,y_train,1e-2,[3, 4],2)
    #--------------------------------------------------------------------------------------------------------
    X_train, y_train = load_iris(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(X_train[50:],y_train[50:],test_size=0.2)
    for i in range(80):
        if y_train[i]==1:
            y_train[i]=-1
        else:
            y_train[i]=1
    for j in range(20):
        if y_test[j]==1:
            y_test[j]=-1
        else:
            y_test[j]=1
    err,w=fit_NeuralNetwork(X_train,y_train,1e-2,[30, 10],100)
    
    plotErr(err,100)
    
    cM=confMatrix(X_test,y_test,w)
    
    sciKit=test_SciKit(X_train, X_test, y_train, y_test)
    
    print("Confusion Matrix is from Part 1a is: ",cM)
    print("Confusion Matrix from Part 1b is:",sciKit)

test()

