import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# Parameter
n = 6
p = 0.4

# Wahrscheinlichkeitsverteilung
x = np.arange(0, n+1)
pmf = binom.pmf(x, n, p)

# Kumulative Verteilungsfunktion
cdf = binom.cdf(x, n, p)

# Wertetabelle der Wahrscheinlichkeitsverteilung
print("Wertetabelle der Wahrscheinlichkeitsverteilung:")
for i in range(len(x)):
    print(f"P(X = {x[i]}) = {pmf[i]:.4f}")

# Wertetabelle der Kumulativen Verteilungsfunktion
print("\nWertetabelle der Wahrscheinlichkeitsverteilung:")
for i in range(len(x)):
    print(f"P(X = {x[i]}) = {cdf[i]:.4f}")

# Säulendiagramm
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.bar(x, pmf, color='blue', alpha=0.7)
plt.xlabel('x')
plt.ylabel('P(X = x)')
plt.title('Wahrscheinlichkeitsverteilung der Binomialverteilung')

# Graph
plt.subplot(1, 2, 2)
plt.step(x, cdf, where='post', marker='o', linestyle='-', color='red')
plt.xlabel('x')
plt.ylabel('P(X ≤ x)')
plt.title('Kumulative Verteilungsfunktion der Binomialverteilung')

plt.tight_layout()
plt.show()