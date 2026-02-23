import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

def train_neural_net(inputs, target, learning_rate=0.1, epochs=10000):
    w1, w2 = 0.5, 0.8 
    w3 = 0.7           
    
    print(f"Starting training to reach target: {target}")

    for epoch in range(epochs):

        h1 = sigmoid(inputs[0] * w1)
        h2 = sigmoid(inputs[1] * w2)
        
        output = sigmoid(h1 * w3 + h2 * w3)

        error = target - output

        d_output = error * sigmoid_derivative(output)

        d_w3 = (h1 * d_output) + (h2 * d_output)
        
        d_h1 = d_output * w3 * sigmoid_derivative(h1)
        d_h2 = d_output * w3 * sigmoid_derivative(h2)
        
        d_w1 = inputs[0] * d_h1
        d_w2 = inputs[1] * d_h2

        w1 += learning_rate * d_w1
        w2 += learning_rate * d_w2
        w3 += learning_rate * d_w3

        if epoch % 2000 == 0:
            print(f"Epoch {epoch}: Output = {output:.4f}, Error = {error:.4f}")

    return output

my_inputs = [1.0, 0.5]
my_target = 0.9  

final_output = train_neural_net(my_inputs, my_target)
print(f"\nFinal Result: {final_output:.4f} (Target: {my_target})")