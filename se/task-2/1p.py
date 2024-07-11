import numpy as np
import matplotlib.pyplot as plt

# Step 1: Define the quadratic model
def quadratic_model(x, a, b, c):
    return a * x**2 + b * x + c

# Step 2: Generate weather data
def generate_weather_data(start, end, num_points, a, b, c, noise_factor=10):
    x = np.linspace(start, end, num_points)
    y = quadratic_model(x, a, b, c) + np.random.normal(0, noise_factor, num_points)
    return x, y

# Step 3: Plot weather data
def plot_weather_data(x, y, title):
    plt.scatter(x, y, label='Weather Data')
    plt.title(title)
    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.legend()
    plt.show()

# Example parameters for the quadratic model
a, b, c = 0.5, -5, 20

# Generate weather data
start_time = 0
end_time = 10
num_points = 100
x_data, y_data = generate_weather_data(start_time, end_time, num_points, a, b, c)

# Plot the data
plot_weather_data(x_data, y_data, 'Waterfall Model: Weather Data')
