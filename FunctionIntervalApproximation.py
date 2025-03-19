import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors

# First time working with sympy, i need all the comments to memorize
# what my pastes from the docs actually do

# this script approximates a function with a polynomial, kind of like a taylor series

# x value for approximation
x_value = 0

# define symbol and original function
x = sp.symbols('x')
f = sp.exp(x)

# Number of approximation iterations/degree of polynomial
num_iterations = 10

P = 0 # P = polynomial

polynomials = []

for i in range(num_iterations):
    f_prime = sp.diff(f, x, i)
    # calculate i-th term of taylor series
    term = (f_prime.subs(x, x_value) / sp.factorial(i)) * (x - x_value)**i
    P += term # append term to the polynomial
    polynomials.append(P)

print(polynomials)

# plots
x_vals = np.linspace(-2, 2, 400)
f_vals = [sp.N(f.subs(x, val)) for val in x_vals]

plt.plot(x_vals, f_vals, label='Original function $e^x$', color='black')

# create a color spectrum
cmap = plt.cm.rainbow
colors = [cmap(i / (num_iterations - 1)) for i in range(num_iterations)]

for i, poly in enumerate(polynomials):
    poly_vals = [sp.N(poly.subs(x, val)) for val in x_vals]
    if i == num_iterations - 1:
        plt.plot(x_vals, poly_vals, label=f'Approximation {i+1}', color=colors[i])
    else:
        # not the final approximation -> make plot line opaque
        plt.plot(x_vals, poly_vals, label=f'Approximation {i+1}', color=colors[i], alpha=0.4)

plt.xlabel('x')
plt.ylabel('y')
plt.title(f'Taylor Series Approximation of {sp.latex(f)} at x = {x_value}')
#plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.legend(fancybox=True, framealpha=0.5, fontsize='x-small')
plt.grid(True)
plt.show()


"""print(f"Original function: {sp.latex(f)}")
print(f"Original function: {sp.pretty(f)}")
print(f"Original function: {sp.sstrrepr(f)}")
print(f"Original function: {sp.sstr(f)}")
print(f"Original function: {str(f)}")"""

print(f"Final approximation: {polynomials[-1]}")
print(f"in LaTeX: {sp.latex(polynomials[-1])}")