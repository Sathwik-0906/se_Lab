def temperature_modeling(a, b, c, time):
  # Calculate temperature based on time using the quadratic equation
  temperature = a * time**2 + b * time + c
  return temperature

print("Keyboard Input for Weather Modeling")
try:
  a_keyboard = float(input("Enter coefficient a: "))
  b_keyboard = float(input("Enter coefficient b: "))
  c_keyboard = float(input("Enter coefficient c: "))
  time_keyboard = float(input("Enter time in hours: "))
  print("Temperature for keyboard input coefficients at time", time_keyboard, "hours:", 
  temperature_modeling(a_keyboard, b_keyboard, c_keyboard, time_keyboard))
  print("\n")
except ValueError:
  print("Error: Please enter valid numeric coefficients and time.")
  exit(1)