import numpy as np

n = int(input("Enter number of points: "))
while n < 10:
    n = int(input("Number of points should be greater than 9: "))
    
cartesian_points = np.random.randint(1, 101, size=(n, 2))

def cartesian_to_polar(cartesian_points):
    x, y = cartesian_points[:, 0], cartesian_points[:, 1]
    r = np.sqrt(x**2 + y**2)
    theta = np.arctan2(y, x)
    return np.column_stack((r, theta * 180 / 3.14159))

polar_points = cartesian_to_polar(cartesian_points)

print("Cartesian Coordinates (x, y):\n", cartesian_points)
print("\nPolar Coordinates (r, theta in degree):\n", polar_points)
