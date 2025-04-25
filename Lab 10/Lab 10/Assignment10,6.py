import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**10 - 4*x**2 + 6*x - 24

def bisection_method(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) > 0:
        raise ValueError("The function must have opposite signs at a and b (f(a)*f(b) < 0).")
    
    updates = []
    for _ in range(max_iter):
        c = (a + b) / 2
        updates.append([a, b, c, f(c)])
        if abs(f(c)) < tol or (b - a) / 2 < tol:
            break
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
    return np.array(updates)

np.random.seed(42)
x_probe = np.linspace(-10, 10, 1000)
for i in range(len(x_probe) - 1):
    a, b = x_probe[i], x_probe[i + 1]
    if f(a) * f(b) < 0:
        break

updates = bisection_method(f, a, b)

iterations = np.arange(1, len(updates) + 1)
root_approximations = updates[:, 2]

plt.figure(figsize=(10, 6))
plt.plot(iterations, root_approximations, marker='o', label='Root Approximation')
plt.axhline(0, color='gray', linestyle='--', label='Exact Root Line')
plt.title('Bisection Method Root-Finding Process')
plt.xlabel('Iteration')
plt.ylabel('Root Approximation (x)')
plt.grid()
plt.legend()
plt.show()

print("Updates (a, b, midpoint, f(midpoint)):")
print(updates)
