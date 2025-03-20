import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors

# First time working with sympy, i need all the comments to memorize
# what my pastes from the docs actually do

# this script approximates a function with a polynomial, kind of like a taylor series

# Threshold for determining viewport (difference between original function and approximation)
threshold = 0.5

# Scale factor between x and y axis
scale_factor = 0.03

# x value for approximation
x_value = 4

# Number of approximation iterations/degree of polynomial
num_iterations = 30

# define symbol and original function
x = sp.symbols('x', real=True)
#f = sp.exp(x)
f = sp.sin(x) * sp.log(1/x) + sp.cos(x)  * 30


P = 0  # P = polynomial

polynomials = []

for i in range(num_iterations):
    """f_prime = sp.diff(f, x, i)
    # calculate i-th term of taylor series
    term = (f_prime.subs(x, x_value) / sp.factorial(i)) * (x - x_value) ** i
    P += term  # append term to the polynomial
    polynomials.append(P)"""
    f_prime = sp.diff(f, x, i)
    coefficient = sp.N(f_prime.subs(x, x_value) / sp.factorial(i))
    term = coefficient * (x - x_value) ** i
    P += term
    polynomials.append(P)

print(polynomials)

final_poly = polynomials[-1]


# evaluate the original function; approximation at a given x value
# access globally defined original and approximated function
def eval_at(x_val):
    orig = float(sp.N(f.subs(x, x_val)))
    approx = float(sp.N(final_poly.subs(x, x_val)))
    return orig, approx, abs(orig - approx)


# find viewport boundaries by tracing left and right from original x_value until difference threshold in y value between
# original and approximation is reached (functions visibly diverge at this point); used to obtain a nice coordinate system section
def find_boundary(direction):
    step_size = 0.01
    current_x = x_value

    while True:
        if direction > 0:
            current_x += step_size
        else:
            current_x -= step_size

        orig, approx, diff = eval_at(current_x)

        if diff > threshold:
            return abs(current_x - x_value)


left_bound = find_boundary(-1)
right_bound = find_boundary(1)
max_bound = max(left_bound, right_bound) * 1.5 #1.1 # add some padding; extend selection 10% to both sides

#viewport
x_min = x_value - max_bound
x_max = x_value + max_bound
#x_max = x_value + max_bound + 10
#x_min = x_value - max_bound - 10

x_vals = np.linspace(x_min, x_max, 400) # todo: make this dynamic based on the viewport

#f_vals = [sp.N(f.subs(x, val)) for val in x_vals]
#f_vals = [sp.N(f.subs(x, val).evalf(chop=True)) for val in x_vals]
f_vals = [float(sp.re(f.subs(x, val).evalf(chop=True))) for val in x_vals]

if scale_factor > 0:
    #after calculating x_min and x_max do y-axis limits
    # x-axis range
    x_range = x_max - x_min

    # get the y values for the original function and all approximations
    all_y_vals = [f_vals]
    for poly in polynomials:
        poly_vals = [float(sp.N(poly.subs(x, val))) for val in x_vals]
        all_y_vals.append(poly_vals)

    # find the minimum and maximum, i miss my java streams
    all_y_vals_flat = [y for sublist in all_y_vals for y in sublist]
    y_min = min(all_y_vals_flat)
    y_max = max(all_y_vals_flat)

    y_at_x_value = float(sp.N(f.subs(x, x_value)))

    desired_y_range = x_range / scale_factor

    # center the y-axis around the approximation point if possible
    # while maintaining the desired scale ratio
    # todo: change to fit y centering to fit most of the function
    y_center = y_at_x_value
    y_min_desired = y_center - desired_y_range / 2
    y_max_desired = y_center + desired_y_range / 2

    # Replace your plt.axis('equal') with:
    plt.xlim(x_min, x_max)
    plt.ylim(y_min_desired, y_max_desired)

    # Optional: Add these lines before plt.show() to add vertical and horizontal lines at the approximation point
    plt.axvline(x=x_value, color='gray', linestyle='--', alpha=0.5)
    plt.axhline(y=y_at_x_value, color='gray', linestyle='--', alpha=0.5)
else:
    print("\tScale factor is negative, skip adjusting y-axis limits")


plt.plot(x_vals, f_vals, label='Original function $e^x$', color='black')

# create a color spectrum
cmap = plt.cm.rainbow
colors = [cmap(i / (num_iterations - 1)) for i in range(num_iterations)]

for i, poly in enumerate(polynomials):
    poly_vals = [sp.N(poly.subs(x, val)) for val in x_vals]
    if i == num_iterations - 1:
        plt.plot(x_vals, poly_vals, label=f'Approximation {i + 1}', color=colors[i])
    else:
        # not the final approximation -> make plot line opaque
        plt.plot(x_vals, poly_vals, label=f'Approximation {i + 1}', color=colors[i], alpha=0.4)
#plt.axis('equal') # equal square; scaled
plt.xlabel('x')
plt.ylabel('y')
plt.title(f'Taylor Series Approximation of {sp.latex(f)} at x = {x_value}')
# plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.legend(fancybox=True, framealpha=0.5, fontsize='x-small')
plt.grid(True)
plt.axvline(x=x_value, color='gray', linestyle='--', alpha=0.5)  # vertical line at x_value (for testing)
plt.show()

"""print(f"Original function: {sp.latex(f)}")
print(f"Original function: {sp.pretty(f)}")
print(f"Original function: {sp.sstrrepr(f)}")
print(f"Original function: {sp.sstr(f)}")
print(f"Original function: {str(f)}")"""

print(f"Final approximation: {polynomials[-1]}")
print(f"in LaTeX: {sp.latex(polynomials[-1])}")
print(f"\tViewport range: [{x_min:.4f}, {x_max:.4f}]")
print(f"\tDivergence point (left): {x_value - left_bound:.4f}")
print(f"\tDivergence point (right): {x_value + right_bound:.4f}")