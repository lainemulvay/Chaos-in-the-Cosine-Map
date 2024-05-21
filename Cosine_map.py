import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, FloatSlider, IntSlider


def draw_cobweb(map_func, x_n, n_iterations):
    x = np.zeros(n_iterations)
    y = np.zeros(n_iterations)
    x_vals = np.linspace(0, 1, 100)
    x[0] = x_n



    # Plot the map and identity
    plt.plot(x_vals, x_vals, color='black', linestyle='--')
    y_vals = map_func(x_vals)
    plt.plot(x_vals, y_vals, color='black', label='Map Function')
    plt.xlabel('x_n')
    plt.ylabel('x_n+1')
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    # Plot the cobweb diagram
    plt.title('Cobweb Diagram')

    # Apply the map iteratively
    for i in range(n_iterations - 1):
        y[i] = map_func(x[i])
        x[i+1] = y[i]
        plt.plot([x[i], y[i]], [y[i], y[i]], color='red')
        plt.plot([y[i-1], y[i-1]], [y[i-1], y[i]], color='red')

    plt.plot([x[0], x[0]], [0, x[1]], color='red')
    plt.show()

# Test the cobweb plot with a simple map
def cosine_map(x):
    return np.cos(x)

# Create sliders
x_n_slider = FloatSlider(min=0, max=1, step=0.01, value=0.1, description='x_n:')
n_iterations_slider = IntSlider(min=1, max=100, step=1, value=10, description='Iterations:')

# Use interact to create the interactive plot
interact(draw_cobweb, map_func=cosine_map, x_n=x_n_slider, n_iterations=n_iterations_slider)
draw_cobweb(cosine_map, 0.1, 10)