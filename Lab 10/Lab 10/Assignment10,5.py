import numpy as np

def format_strings(array):
    formatted_centered = np.array([f"{s:^15}".replace(" ", "_") for s in array])
    formatted_left = np.array([f"{s:<15}".replace(" ", "_") for s in array])
    formatted_right = np.array([f"{s:>15}".replace(" ", "_") for s in array])
    
    return formatted_centered, formatted_left, formatted_right

array = []
n = int(input("Enter number of strings: "))
while n < 0:
    n = int(input("Please enter a positive integer: "))

for i in range(n):
    string = str(input(f"Enter string {i+1}: "))
    array.append(string)

array = np.array(array)
centered, left_justified, right_justified = format_strings(array)

print("Original Array:")
print(array)
print("\nCentered Strings:")
print(centered)
print("\nLeft Justified Strings:")
print(left_justified)
print("\nRight Justified Strings:")
print(right_justified)
