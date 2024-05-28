import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

class Neuron:
    def __init__(self, n_inputs, bias = 0., weights = None):
        self.b = bias
        if weights: self.ws = np.array(weights)
        else: self.ws = np.random.rand(n_inputs)

    def _f(self, x): #activation function (here: leaky_relu)
        return max(x*.1, x)

    def __call__(self, xs): #calculate the neuron's output: multiply the inputs with the weights and sum the values together, add the bias value,
                            # then transform the value via an activation function
        return self._f(xs @ self.ws + self.b)

class Layer:
    def __init__(self, n_inputs, n_neurons):
        self.neurons = [Neuron(n_inputs) for _ in range(n_neurons)]

    def __call__(self, xs):
        return np.array([neuron(xs) for neuron in self.neurons])

class ANN:
    def __init__(self, n_inputs, hidden_layers, n_outputs):
        layers = [Layer(n_inputs, hidden_layers[0])]
        layers += [Layer(hidden_layers[i-1], hidden_layers[i]) for i in range(1, len(hidden_layers))]
        layers.append(Layer(hidden_layers[-1], n_outputs))
        self.layers = layers

    def __call__(self, xs):
        for layer in self.layers:
            xs = layer(xs)
        return xs

ann = ANN(n_inputs=3, hidden_layers=[4, 4], n_outputs=1)
inputs = np.array([1.0, 0.5, -1.0])

output = ann(inputs)
print(output)

def draw_ann(ann):
    G = nx.DiGraph()
    pos = {}
    colors = []
    n_inputs = len(ann.layers[0].neurons[0].ws)
    for i in range(n_inputs):
        G.add_node(('Input', i))
        pos[('Input', i)] = (-1, -i + 0.5 * (n_inputs - 1))
        colors.append('red')
    for i, layer in enumerate(ann.layers):
        for j, neuron in enumerate(layer.neurons):
            G.add_node((i, j))
            pos[(i, j)] = (i, -j + 0.5 * (len(layer.neurons) - 1))
            if i == 0:
                for k in range(n_inputs):
                    G.add_edge(('Input', k), (i, j))
            else:
                for k in range(len(ann.layers[i - 1].neurons)):
                    G.add_edge((i - 1, k), (i, j))

            if i < len(ann.layers) - 1:
                colors.append('blue')
            else:
                colors.append('green')

    nx.draw(G, pos, with_labels=False, node_color=colors, node_size=1000)


    plt.text(-1, -1.8, 'Input Layer', fontsize=12, ha='center')
    for i in range(len(ann.layers) - 1):
        plt.text(i, -1.8, f'Hidden Layer {i+1}', fontsize=12, ha='center')
    plt.text(len(ann.layers) - 1, -1.8, 'Output Layer', fontsize=12, ha='center')

    plt.show()

ann = ANN(n_inputs=3, hidden_layers=[4, 4], n_outputs=1)
draw_ann(ann)
