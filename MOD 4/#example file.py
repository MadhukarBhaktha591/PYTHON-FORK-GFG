#example file.py
#xor and or ..perceptron
def xor(a,b):
    return (a|b)&(not(a&b))
def andof(a,b):
    return a&b 
def orof(a,b):
    return a|b
n = 4
while n != 0:
    A, B = map(int,input("Enter A and B space separated either 1 or 0 : ").split())
    print("XOR of A and B is : " + str(xor(A,B)))
    print("AND of A and B is : " + str(andof(A,B)))
    print("OR of A and B is : " + str(orof(A,B)))
    n -= 1

import math
import numpy as np
def sigmoid(x):
    return 1 / (1 + np.exp(-x)) 

def neuron_output(weights,inputs):
    return sigmoid(np.dot(weights,inputs))

def feed_forward(neural_network, input_vector):
    outputs = []
    for layer in neural_network:
        input_with_bias = np.append(input_vector,1)
        output = [neuron_output(neuron, input_with_bias)
                  for neuron in layer]
        outputs.append(output)

        input_vector = output

    return outputs

xor_networks = [
    [[20,20,-30],
    [20,20,-10]],

    [[-60,60,-30]]]

for x in [0, 1]:
    for y in [0, 1]:
        print(x,y,feed_forward(xor_networks,[x,y])[-1])