import numpy as np
import matplotlib.pyplot as plt

# Define the quadratic model
def quadratic_model(x, a, b, c):
    return a * x**2 + b * x + c

# # Generate weather data
a, b, c = 0.5, -5, 20
x = np.linspace(0, 10, 100)
y = quadratic_model(x, a, b, c)

# Plot weather data
plt.scatter(x, y, label='Weather Data')
plt.title('Agile Model: Initial Weather Data')
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.legend()
plt.show()

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Generate and plot weather data
x = np.linspace(0, 10, 100)
y = quadratic_model(x, a, b, c)
plt.scatter(x, y, label='Weather Data')
plt.title('Agile Model: Weather Data with User Input')
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.legend()
plt.show()

# Adding file input for coefficients
with open('weather.txt', 'r') as file:
    lines = file.readlines()
    a, b, c = map(float, lines[0].split())

# Generate and plot weather data
x = np.linspace(0, 10, 100)
y = quadratic_model(x, a, b, c)
plt.scatter(x, y, label='Weather Data')
plt.title('Agile Model: Weather Data with File Input')
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.legend()
plt.show()


#Generate weather data with noise
def generate_weather_data(start, end, num_points, a, b, c, noise_factor=10):
    x = np.linspace(start, end, num_points)
    y = quadratic_model(x, a, b, c) + np.random.normal(0, noise_factor, num_points)
    return x, y

# Example parameters for the quadratic model
a, b, c = 0.5, -5, 20

# Generate weather data
start_time = 0
end_time = 10
num_points = 100
x_data, y_data = generate_weather_data(start_time, end_time, num_points, a, b, c)

# Plot the data
plt.scatter(x_data, y_data, label='Weather Data')
plt.title('Agile Model: Weather Data with Noise')
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.legend()
plt.show()


