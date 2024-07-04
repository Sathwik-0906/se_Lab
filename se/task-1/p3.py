def temperature_modeling(a, b, c, time):
  # Calculate temperature based on time using the quadratic equation
  temperature = a * time**2 + b * time + c
  return temperature
# File Input Section
try:
  with open('weather.txt', 'r') as file:
      lines = file.readlines()
      if lines:
          a_file, b_file, c_file, time_file = map(float, lines[0].split())
          print("Read from a File for Weather Modeling")
          print("Temperature for file input coefficients at time", time_file, "hours:", 
          temperature_modeling(a_file, b_file, c_file, time_file))
          print("\n")
      else:
          print("Error: File is empty.")
          exit(1)
except FileNotFoundError:
  print("Error: File 'weather.txt' not found.")
  exit(1)
except ValueError:
  print("Error: Incorrect format in file. Please ensure the first line contains numeric values.")
  exit(1)