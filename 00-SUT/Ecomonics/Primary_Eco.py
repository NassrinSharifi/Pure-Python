def f_p(i: float, n: int, p: float = None) -> float:
    """produce f from p"""
    if p:
        return p * ((1 + i) ** n)
    else:
        return (1 + i) ** n


def p_f(i: float, n: int, f: float = None) -> float:
    """produce p from f"""
    if f:
        return f * (1 / (1 + i) ** n)
    else:
        return 1 / (1 + i) ** n


def p_a(i: float, n: int, a: float = None) -> float:
    """produce p from a"""
    if a:
        return a * (((1 + i) ** n - 1) / ((1 + i) ** n * i))
    else:
        return ((1 + i) ** n - 1) / ((1 + i) ** n * i)


def a_p(i: float, n: int, p: float = None) -> float:
    """produce a from p"""
    if p:
        return p * (((1 + i) ** n * i) / ((1 + i) ** n - 1))
    else:
        return ((1 + i) ** n * i) / ((1 + i) ** n - 1)


def f_a(i: float, n: int, a: float = None) -> float:
    """produce f from a"""
    if a:
        return a * (((1 + i) ** n - 1) / i)
    else:
        return ((1 + i) ** n - 1) / i


def a_f(i: float, n: int, f: float = None) -> float:
    """produce a from f"""
    if f:
        return f * (i / ((1 + i) ** n - 1))
    else:
        return i / ((1 + i) ** n - 1)


def p_g(i: float, n: int, g: float = None) -> float:
    """produce p from g"""
    if g:
        return g * ((1 / i) * ((((1 + i) ** n - 1) / (i * (1 + i) ** n)) - (n / (1 + i) ** n)))
    else:
        return (1 / i) * ((((1 + i) ** n - 1) / (i * (1 + i) ** n)) - (n / (1 + i) ** n))


def a_g(i: float, n: int, g: float = None) -> float:
    """produce a from g"""
    if g:
        return g * ((1 / i) - (n / (((1 + i) ** n) - 1)))
    else:
        return (1 / i) - (n / (((1 + i) ** n) - 1))


def p_a1(i: float, j: float, n: int, a1: float = None) -> float:
    """produce p from a1"""
    if a1:
        if i == j:
            return a1 * ((n * a1) / (1 + i))
        else:
            return a1 * ((1 - ((1 + j) ** n) * ((1 + i) ** (-n))) / (i - j))
    else:
        if i == j:
            return (n * a1) / (1 + i)
        else:
            return (1 - ((1 + j) ** n) * ((1 + i) ** (-n))) / (i - j)


def f_a1(i: float, j: float, n: int, a1: float = None) -> float:
    """produce f from a1"""
    if a1:
        if i == j:
            return a1 * (n * (1 + j) ** (n - 1))
        else:
            return a1 * ((((1 + i) ** n) - ((1 + j) ** n)) / (i - j))
    else:
        if i == j:
            return n * (1 + j) ** (n - 1)
        else:
            return (((1 + i) ** n) - ((1 + j) ** n)) / (i - j)


def rg(parameters: list) -> float:
    """calculate geometric sequence mean"""
    answer = 1
    for i in parameters:
        answer *= (i + 1)
    return answer ** (1 / len(parameters)) - 1


def ie(r: float, m: int) -> float:
    """produce effective interest rate"""
    return (1 + r / m) ** m - 1


def i_from_ie(ie: float, m: int) -> float:
    """produce interest rate from effective interest rate"""
    return (ie + 1) ** (1 / m) - 1
