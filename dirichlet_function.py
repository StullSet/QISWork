#!/usr/bin/env python3
# dirichlet_function.py

# Allows us to use values with much larger precision
# Really small and really big values
import mpmath

mpmath.mp.dps = 2000  # dps = decimal places

# mpmath immensely simplifies the calculation process
def dirichlet_function(x):
    # Defining our variables
    k = 100
    n = 1e10
    # Defining the Dirichlet Pathological function shown on slide 51
    f = mpmath.power(mpmath.cos(mpmath.factorial(k) * mpmath.pi * x), n)
    # mpmath.chop rounds values that have an even smaller level of precision than we require
    return mpmath.chop(f)


def main():
    # Printing the results for all desired values of x
    print(f"f(2) = {dirichlet_function(2)}")
    print(f"f(2.5) = {dirichlet_function(2.5)}")
    print(f"f(sqrt(2)) = {dirichlet_function(mpmath.sqrt(2))}")
    print(f"f(e) = {dirichlet_function(mpmath.e)}")


if __name__ == "__main__":
    main()
