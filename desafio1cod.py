import numpy as np

x = np.array([[0.52, 0.20, 0.25],
              [0.30, 0.50, 0.20],
              [0.18, 0.30, 0.55]])
y = np.array([4800, 5210, 5690])
z = np.linalg.solve(x, y)
print("Las cantidades de metros cubicos son:")
print(f"Cantera 1: {z[0]:.2f} m³")
print(f"Cantera 2: {z[1]:.2f} m³")
print(f"Cantera 3: {z[2]:.2f} m³")