#example4.py
#backpropagation algorithm
import numpy as np

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivative of the sigmoid function
def sigmoid_derivative(x):
    return x * (1 - x)

# XOR inputs and outputs
inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
outputs = np.array([[0], [1], [1], [0]])

# Set random seed for reproducibility
np.random.seed(42)

# Initialize network parameters
input_layer_neurons = 2  # Two input neurons
hidden_layer_neurons = 2  # Two neurons in the hidden layer
output_neurons = 1  # Single output neuron

# Initialize weights and biases with random values
weights_input_hidden = np.random.uniform(low=-1.0, high=1.0, size=(input_layer_neurons, hidden_layer_neurons))
weights_hidden_output = np.random.uniform(low=-1.0, high=1.0, size=(hidden_layer_neurons, output_neurons))

# Bias terms
bias_hidden = np.random.uniform(low=-1.0, high=1.0, size=(1, hidden_layer_neurons))
bias_output = np.random.uniform(low=-1.0, high=1.0, size=(1, output_neurons))

# Learning rate
learning_rate = 0.5

# Training the network
epochs = 10000  # Number of training iterations

for epoch in range(epochs):
    # Forward propagation
    hidden_layer_activation = np.dot(inputs, weights_input_hidden) + bias_hidden
    hidden_layer_output = sigmoid(hidden_layer_activation)

    final_layer_activation = np.dot(hidden_layer_output, weights_hidden_output) + bias_output
    predicted_output = sigmoid(final_layer_activation)

    # Calculate the error
    error = outputs - predicted_output
    mse = np.mean(np.square(error))  # Mean Squared Error

    # Backpropagation
    d_predicted_output = error * sigmoid_derivative(predicted_output)
    error_hidden_layer = d_predicted_output.dot(weights_hidden_output.T)
    d_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_layer_output)

    # Update weights and biases
    weights_hidden_output += hidden_layer_output.T.dot(d_predicted_output) * learning_rate
    bias_output += np.sum(d_predicted_output, axis=0, keepdims=True) * learning_rate

    weights_input_hidden += inputs.T.dot(d_hidden_layer) * learning_rate
    bias_hidden += np.sum(d_hidden_layer, axis=0, keepdims=True) * learning_rate

    # Print error at every 1000th epoch
    if epoch % 1000 == 0:
        print(f"Epoch {epoch}, MSE: {mse}")

# Print the final output
print("Final output after training:")
print(predicted_output)

# Testing the XOR network
print("\nTesting the trained network:")
for x in [0, 1]:
    for y in [0, 1]:
        hidden_layer_activation = np.dot([x, y], weights_input_hidden) + bias_hidden
        hidden_layer_output = sigmoid(hidden_layer_activation)

        final_layer_activation = np.dot(hidden_layer_output, weights_hidden_output) + bias_output
        predicted_output = sigmoid(final_layer_activation)

        print(f"Input: {x, y}, Output: {predicted_output}")
