import numpy as np
import matplotlib.pyplot as plt

class Perceptron():
    def __init__(self, train_input, train_output, epochs = 10000, learning_rate = 0.1):
        self.train_input = train_input
        self.train_output = train_output
        self.epochs = epochs
        self.learning_rate = learning_rate
        self.weights = 2 * np.random.random((len(self.train_input[0]),1)) - 1
        self.b = np.random.randn()
        self.error = [0]*epochs
        self.was_trained = False

    def sigmoid(self,x):
        return 1/(1+np.exp(-x))

    def sigmoid_derivative(self,x):
        return self.sigmoid(x)*(1-self.sigmoid(x))

    def train(self):
        for i in range(self.epochs):
            curr_outputs = self.sigmoid(np.dot(self.train_input, self.weights)+self.b)
            cost = self.train_output - curr_outputs
            self.error[i] = sum(cost)
            correction = cost*self.sigmoid_derivative(np.dot(self.train_input, self.weights))
            self.weights += self.learning_rate*np.dot(self.train_input.T, correction)
            for x in correction:
                self.b += self.learning_rate*x
        
    def visualize_training(self):
        if not self.was_trained:
            self.train()
    
        fig, ax = plt.subplots()
        ax.plot(np.arange(self.epochs), [1/sum(x) for x in self.error])
        ax.set(xlabel='Epoch', ylabel='Sum Error',
               title='Perceptron Convergence')
        plt.show()

    def visualize_data(self):
        minimum = np.amin(self.train_input) - 1
        maximum = np.amax(self.train_input) + 1
        fig, ax = plt.subplots()
        ax.axis([minimum, maximum, minimum, maximum])
        ax.grid()
        for i in range(len(self.train_input)):
            if self.train_output[i] == 0:
                color = 'g'
            else:
                color = 'b'
            plt.scatter(self.train_input[i][0],self.train_input[i][1],c=color)
        x = np.linspace(minimum, maximum, 100)
        y = [(xi*self.weights[0]+self.b)/(-self.weights[0]) for xi in x]
        ax.plot(x,y)
        plt.show()

    def check(self, inputs ):
        return self.sigmoid(np.dot(inputs, self.weights)+self.b)

def check_correctness(inputs, outputs, perceptron):
    for i in range(len(inputs)):
        if outputs[i] == np.round(perceptron.check(inputs[i])):
            print('SUCCESS')
        else:
            print('FAILURE')

#Training data for AND gate
AND_inputs = np.array([[0,0],[0,1],[1,0],[1,1]])
AND_outputs = np.array([[0,0,0,1]]).T

#Perceptron object for AND gate
AND = Perceptron(AND_inputs, AND_outputs)
AND.train()

#Training data for AND gate
OR_inputs = np.array([[0,0],[0,1],[1,0],[1,1]])
OR_outputs = np.array([[0,1,1,1]]).T

#Perceptron object for OR gate
OR = Perceptron(OR_inputs, OR_outputs)
OR.train()

check_correctness(AND_inputs, AND_outputs, AND)
check_correctness(OR_inputs, OR_outputs, OR)

AND.visualize_data()
OR.visualize_data()

