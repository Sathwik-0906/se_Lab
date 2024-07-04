def temperature_modeling(a, b, c, time):
  # Calculate temperature based on time using the quadratic equation
  temperature = a * time**2 + b * time + c
  return temperature

# File Input Section
try:
  with open('weather.txt', 'r') as file:
      lines = file.readlines()
      if lines:
          print("Read from a File for Weather Modeling\n")
          for line in lines:
              try:
                  a_file, b_file, c_file, time_file = map(float, line.split())
                  print(f"Temperature for file input coefficients (a={a_file}, b={b_file}, c={c_file}) at time {time_file} hours: {temperature_modeling(a_file, b_file, c_file, time_file)}")
              except ValueError:
                  print("Error: Incorrect format in line. Please ensure the line contains numeric values.")
          print("\n")
      else:
          print("Error: File is empty.")
          exit(1)
except FileNotFoundError:
  print("Error: File 'weather.txt' not found.")
  exit(1)
