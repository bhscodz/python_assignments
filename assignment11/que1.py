import pandas as pd
a = pd.to_datetime("Jan 15 2012")
print(f"a) {a}")
b = pd.to_datetime("2023/08/23 9:20 pm")
print(f"b) {b}")
c = pd.Timestamp.now()
print(f"c) {c}")
d = pd.to_datetime("January 12 2009").date()
print(f"d) {d}")
e = pd.Timestamp.now().date()
print(f"e) {e}")
f = pd.to_datetime("March 2 2026 8:30 pm").time()
print(f"f) {f}")
g = pd.Timestamp.now().time()
print(f"g) {g}")