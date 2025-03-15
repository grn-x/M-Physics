# ill tell you what though folks, thats bloody nice, that is really ... that is bloody lovely
# https://youtu.be/tnPG-kOTrls?t=454
import sympy as sp
# First time working with sympy, i need all the comments to memorize
# what my pastes from the docs actually do

# this script approximates a function with a polynomial, kind of like a taylor series

# x value for approximation
x_value = 0

# define symbol and original function
x = sp.symbols('x')
f = sp.exp(x)

# Derive the function twice
f_prime = sp.diff(f, x)
f_double_prime = sp.diff(f_prime, x)


# Define the polynomial to approximate the original function
# P(x) = a0 + a1*x + a2*x**2
a0, a1, a2 = sp.symbols('a0 a1 a2')
P = a0 + a1 * x + a2 * x**2

#calculate polynomial params
# P(x_value) should be equal to f(x_value)
eq1 = sp.Eq(P.subs(x, x_value), f.subs(x, x_value))
# P'(x_value) should be equal to f'(x_value)
eq2 = sp.Eq(sp.diff(P, x).subs(x, x_value), f_prime.subs(x, x_value))
# P''(x_value) should be equal to f''(x_value)
eq3 = sp.Eq(sp.diff(P, x, x).subs(x, x_value), f_double_prime.subs(x, x_value))

# Solve for the parameters a0, a1, a2
solution = sp.solve((eq1, eq2, eq3), (a0, a1, a2))

# Substitute the solutions into the polynomial
P_approx = P.subs(solution)

print(f"Original function: {f}")
print(f"First derivative: {f_prime}")
print(f"Second derivative: {f_double_prime}")
print(f"Approximating polynomial: {P_approx}")
print(f"Solution for parameters: {solution}")