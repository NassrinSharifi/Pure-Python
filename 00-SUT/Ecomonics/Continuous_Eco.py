from math import exp


def p_f(r: float, n: int, f: float = None) -> float:
    """produce p from f"""
    if f:
        return f * exp(-r * n)
    else:
        return exp(-r * n)


def f_p(r: float, n: int, p: float = None) -> float:
    """produce f from p"""
    if p:
        return p * exp(r * n)
    else:
        return exp(r * n)


def f_a(r: float, n: int, a: float = None) -> float:
    """produce f from a"""
    if a:
        return a * ((exp(r * n) - 1) / (exp(r) - 1))
    else:
        return (exp(r * n) - 1) / (exp(r) - 1)


def a_f(r: float, n: int, f: float = None) -> float:
    """produce a from f"""
    if f:
        return f * ((exp(r) - 1) / (exp(r * n) - 1))
    else:
        return (exp(r) - 1) / (exp(r * n) - 1)


def p_a(r: float, n: int, a: float = None) -> float:
    """produce p from a"""
    if a:
        return a * ((exp(r * n) - 1) / (exp(r * n) * (exp(r) - 1)))
    else:
        return (exp(r * n) - 1) / (exp(r * n) * (exp(r) - 1))


def a_p(r: float, n: int, p: float = None) -> float:
    """produce a from p"""
    if p:
        return p * ((exp(r * n) * (exp(r) - 1)) / (exp(r * n) - 1))
    else:
        return (exp(r * n) * (exp(r) - 1)) / (exp(r * n) - 1)


def p_g(r: float, n: int, g: float = None) -> float:
    """produce p from g"""
    if g:
        return g * ((exp(r * n) - 1 - n * (exp(r) - 1)) / (exp(r * n) * ((exp(r) - 1) ** 2)))
    else:
        return (exp(r * n) - 1 - n * (exp(r) - 1)) / (exp(r * n) * ((exp(r) - 1) ** 2))


def a_g(r: float, n: int, g: float = None) -> float:
    """produce a from g"""
    if g:
        return g * ((1 / (exp(r) - 1)) - (n / (exp(r * n) - 1)))
    else:
        return (1 / (exp(r) - 1)) - (n / (exp(r * n) - 1))


def ie(r: float) -> float:
    """produce effective interest rate"""
    return exp(r) - 1
