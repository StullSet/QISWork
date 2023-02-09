#!/usr/bin/env python3
# binomial_sqrt.py

import sympy


def printM(expr, num_digits):
    return expr.xreplace(
        {
            n.evalf(): n if type(n) == int else sympy.Float(n, num_digits)
            for n in expr.atoms(sympy.Number)
        }
    )


# Calculating the coefficients using Newton's method
def calc_coeff(a, b, r, n):
    i = 1
    for m in range(n):
        i = i * (r - m) / (m + 1)
    i = i * pow(a, r - n)
    i = i * pow(b, n)
    return i


def binomial_expand(a, b, c, r, max_t):
    # Using sympy to treat x as an element and not a variable
    x = sympy.symbols("x")
    poly = 0
    for t in range(max_t):
        # Calling helper function to generate polynomial
        poly += calc_coeff(a, b, r, t) * x ** (c * t)
    # Making it so that we can then use poly as a function within the source code
    # So that we can call it elsewhere
    return poly, sympy.lambdify(x, poly.as_expr(), modules="numpy")


def heron(s):
    x = s / 2
    t = 1
    while x**2 - s > 1e-14:
        x = (s / x + x) / 2
        t += 1
    return t, x


def main():
    print(f"{'Terms':>5}{'Estimate':>18}{'Binomial Expansion':>21}")
    # Expanding for 20 terms
    for t in range(1, 21):
        eqn = binomial_expand(1, -1, 1, 1 / 2, t)
        print(f"{t:>5}  {3 * eqn[1](2/9):.14f}", end="")
        # Only printing out the first 7 polynomials
        if t < 8:
            print(f" = {printM(eqn[0], 5)}", end=" ")
        print()

    # Comparing the Heron's method
    t, x = heron(7)
    print("Heron's Method")
    print(f"{t:>5}  {x:.14f}", end="")


if __name__ == "__main__":
    main()
