import numpy as np


class Node:
    def __init__(self, n: int, x: float, y: float):
        """

        :param n:
        :param x:
        :param y:
        """
        self.number = int(n)
        self.x = x
        self.y = y


class Element:
    def __init__(self, node1: Node, node2: Node, A: float, E: float):
        """

        :param node1:
        :param node2:
        :param A:
        :param E:
        """
        self.node1 = node1
        self.node2 = node2
        self.l = np.sqrt((node1.x - node2.x) ** 2 + (node1.y - node2.y) ** 2)
        self.area = A
        self.E = E
        if node2.x != node1.x:
            self.teta = np.arctan((node2.y - node1.y) / (node2.x - node1.x))
        else:
            self.teta = np.pi / 2
        u1 = str(self.node1.number) + "x"
        v1 = str(self.node1.number) + "y"
        u2 = str(self.node2.number) + "x"
        v2 = str(self.node2.number) + "y"
        self.tag_matrix = np.array((u1 + u1, u1 + v1, u1 + u2, u1 + v2,
                                    v1 + u1, v1 + v1, v1 + u2, v1 + v2,
                                    u2 + u1, u2 + v1, u2 + u2, u2 + v2,
                                    v2 + u1, v2 + v1, v2 + u2, v2 + v2))
        self.k_of_element()

    def k_of_element(self):  # it gives k matrix of element in global coordinates
        c = np.cos(self.teta)
        s = np.sin(self.teta)
        k = self.area * self.E / self.l * np.array((c ** 2, c * s, -c ** 2, -c * s,
                                                    c * s, s ** 2, -c * s, -s ** 2,
                                                    -c ** 2, -c * s, c ** 2, c * s,
                                                    -c * s, -s ** 2, c * s, s ** 2))
        self.k = k


# ...............................................................................................................

def produce_tag(n: int, degrees_of_freedom: list):
    """

    :param n: number of nodes
    :param degrees_of_freedom: like:x,y,phi
    :return: a matrix containing : 1x1x 1x1y and so on...
    """
    tag_matrix = np.array([])
    for i1 in range(n):
        for j1 in range(len(degrees_of_freedom)):
            for i2 in range(n):
                for j2 in range(len(degrees_of_freedom)):
                    strng = str(int(i1 + 1)) + degrees_of_freedom[j1] + str(int(i2 + 1)) + degrees_of_freedom[j2]
                    tag_matrix = np.append(tag_matrix, [strng])
    return tag_matrix


def assemble(element: Element, tag: np.array, K: np.array):
    e_tag = element.tag_matrix
    # print(e_tag)
    for k, v in enumerate(e_tag):
        # print(v)
        for k2, v2 in enumerate(tag):
            # print(v2)
            if v == v2:
                # print(element.k[k])
                K[k2] += element.k[k]
    return K
