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
plt.title('Iterative Model: Initial Weather Data')
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.legend()
plt.show()

# # Adding user input for coefficients
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Generate and plot weather data
x = np.linspace(0, 10, 100)
y = quadratic_model(x, a, b, c)
plt.scatter(x, y, label='Weather Data')
plt.title('Iterative Model: Weather Data with User Input')
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
plt.title('Iterative Model: Weather Data with File Input')
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.legend()
plt.show()

