import numpy as np

class Point:
    def __init__(self, x: float, y: float = 0, z: float = 0, c: float = 0):
        self.x = x
        self.y = y
        self.z = z
        self.c = c


# the first point is located in x0=0, y0=0
class Diff_and_Adv:
    def __init__(self, M, Dx: float = 1, Dy: float = 1, Dz: float = 1):
        self.M = M
        self.Dx = Dx
        self.Dy = Dy
        self.Dz = Dz

    def concentration(self, coefficient: float, t: float, x: float, y: float = 0, z: float = 0, u: float = 0,
                      v: float = 0, w: float = 0):

        """
        param coefficient: if 1D: it is A* np.sqrt(4 * np.pi * t)
                            if 2d: it is Lz * 4 * np.pi * t
                            if 3d: it is (4 * np.pi * t) **3/2
        """
        concentration = (self.M / (coefficient * np.sqrt(self.Dx * self.Dy * self.Dz))) * np.exp(
            -(x - u * t) ** 2 / (4 * self.Dx * t) - (y - v * t) ** 2 / (4 * self.Dy * t) - (
                    z - w * t) ** 2 / (4 * self.Dz * t))
        return concentration


"""attention: the  ship was on the west side of the city so we consider only the parameters on the east-west side"""


def Peclet(u: float, Dx: float, L: float = 100):
    pe=abs(u)*L/Dx
    if pe >= 1:
        print( f"The Peclet number is {pe:.3f} , which is greater than 1 , so advection is dominant ! ")
    else:
        print( f"The Peclet number is {pe:.3f} , which is less than 1 , so diffusion is dominant ! ")
