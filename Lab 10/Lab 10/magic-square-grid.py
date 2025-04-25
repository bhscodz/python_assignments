import numpy as np
import matplotlib.pyplot as plt

def is_magic_square(square):
    n = len(square)
    magic_sum = n * (n**2 + 1) // 2

    # Check rows and columns
    for i in range(n):
        if sum(square[i]) != magic_sum or sum(square[:, i]) != magic_sum:
            return False

    # Check diagonals
    if sum(square[i][i] for i in range(n)) != magic_sum or sum(square[i][n - 1 - i] for i in range(n)) != magic_sum:
        return False

    return True

def generate_magic_square(n):
    if n % 2 == 0:
        raise ValueError("Only odd-sized magic squares are supported.")

    magic_square = np.zeros((n, n), dtype=int)
    num = 1
    i, j = 0, n // 2

    while num <= n**2:
        magic_square[i][j] = num
        num += 1
        new_i, new_j = (i - 1) % n, (j + 1) % n

        if magic_square[new_i][new_j]:
            i += 1
        else:
            i, j = new_i, new_j

    return magic_square

def plot_magic_square(square):
    n = len(square)
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.matshow(np.ones((n, n)), cmap='gray', alpha=0.1)

    for i in range(n):
        for j in range(n):
            ax.text(j, i, str(square[i][j]), va='center', ha='center', fontsize=20)

    plt.xticks(range(n), [])
    plt.yticks(range(n), [])
    plt.title(f"{n}x{n} Magic Square")
    plt.show()

if __name__ == "__main__":
    n = int(input("Enter size of magic square: "))  # Size of the magic square (must be odd)
    magic_square = generate_magic_square(n)
    print("Generated Magic Square:")
    print(magic_square)

    if is_magic_square(magic_square):
        print("This is a valid magic square.")
    else:
        print("This is not a valid magic square.")

    plot_magic_square(magic_square)