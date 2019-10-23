"""Collection of tools for finding roots
"""

import cmath

def quad_roots(a=1.0, b=2.0, c=0.0):
    """Returns the roots of a quadratic equation ax^2 + bx + x = 0
    
    Args:
        a (float, optional): Coefficient on quadratic term. Defaults to 1.0.
        b (float, optional): Coefficient on the linear term. Defaults to 2.0.
        c (float, optional): Constant term. Defaults to 0.0.
    
    Raises:
        ValueError: Quadratic coefficient is zero
    
    Returns:
        tuple: Both roots of the equation

    Examples:
        >>> quad_roots(1.0, 1.0, -12.0)
        ((3 + 0j), (-4 + 0j))
    """

    if a == 0:
        raise ValueError("The quadratic coefficient is zero.  This is not a quadratic equation.")
    else:
        sqrt_disc = cmath.sqrt(b * b - 4.0 * a * c)
        r1 = -b + sqrt_disc
        r2 = -b - sqrt_disc
        two_a = 2.0 * a
        return (r1 / two_a, r2 / two_a)

def linear_roots(a=1.0, b=0.0):
    """Return the root of a linear equation ax + b = 0
    
    Args:
        a (float, optional): Coefficient on the linear term. Defaults to 1.0.
        b (float, optional): Constant. Defaults to 0.0.
    
    Raises:
        ValueError: Linear coefficient is zero
    
    Returns:
        float: Root

    Examples:
        >>> linear_roots(1.0, 2.0)
        -2.0
    """

    if a == 0:
        raise ValueError("The linear coefficient is zero.  This is not a linear equation.")
    else:
        return ((-b / a))

if __name__ == '__main__':
    print(quad_roots(1.0, 1.0, -12.0))
    print(linear_roots(1.0, 2.0))