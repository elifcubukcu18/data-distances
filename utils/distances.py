def manhattan_distance(point1, point2):
    d_x = abs(point2[0] - point1[0])
    d_y = abs(point2[1] - point1[1])
    return d_x + d_y

def euclidean(a, b):

    d_x = b[0] - a[0]
    d_y = b[1] - a[1]

    return (d_x ** 2 + d_y ** 2) ** 0.5

def manhattan(a, b):
    return minkowski(a, b, 1)


def euclidean(a, b):
    return minkowski(a, b, 2)


def minkowski(a, b, p):
    d_x = b[0] - a[0]
    d_y = b[1] - a[1]

    distance = (abs(d_x)**p + abs(d_y)**p)**(1/p)
    return distance
