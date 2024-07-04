def temperature_modeling(a, b, c, time):
  # Calculate temperature based on time using the quadratic equation
  temperature = a * time**2 + b * time + c
  return temperature

# Hard-coded Variables Section
a_hardcoded, b_hardcoded, c_hardcoded = 0.1, 2, 10
time_hardcoded = 5  # Example time value
print("Hard-coded Variables for Weather Modeling")
print("Temperature for hardcoded coefficients at time", time_hardcoded, "hours:", temperature_modeling(a_hardcoded, b_hardcoded, c_hardcoded, time_hardcoded))