import random
from functions import *

class Perceptron:
    def __init__(self):
        self.weights = [random.uniform(-1, 1), random.uniform(-1, 1)]
        self.learning_rate = 0.000001

    def predict(self, inputs):
        sum = 0
        #first and second step of the perceptron algorithm
        for i in range(0, len(self.weights)):
            sum += inputs[i] * self.weights[i]

        #third step: passes throught the activation function
        output = Activate(sum)
        return output

    def train(self, inputs, target):
        #supervised learning process
        guess = self.predict(inputs)
        error = target - guess

        for i in range(0, len(self.weights)):
            self.weights[i] +=  error * inputs[i] * self.learning_rate
