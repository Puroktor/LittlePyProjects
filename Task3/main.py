import math


class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def __str__(self):
        return str(self.x) + " " + str(self.y) + "\n"


class Triangle(object):

    def __init__(self, point1, point2, point3):
        side1, side2, side3 = sorted([point1.distance_to(point2),
                                      point1.distance_to(point3),
                                      point2.distance_to(point3)])
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def is_similar(self, other):
        return math.isclose(self.side1 / other.side1, self.side2 / other.side2) and \
               math.isclose(self.side2 / other.side2, self.side3 / other.side3)

    def __str__(self):
        return str(self.point1) + str(self.point2) + str(self.point3)


def read_triangles(file_name):
    with open(file_name, "r") as file:
        coords = []
        for line in file:
            xy = [float(num) for num in line.strip().split()]
            if not xy:
                continue
            coords.append(Point(xy[0], xy[1]))
    triangles = [Triangle(coords[i], coords[i + 1], coords[i + 2])
                 for i in range(0, len(coords), 3)]
    return triangles


def sort_triangles(triangles):
    sorted_triangles = []
    for triangle in triangles:
        added = False
        for group in sorted_triangles:
            if group[0].is_similar(triangle):
                group.append(triangle)
                added = True
        if not added:
            sorted_triangles.append([triangle])
    return sorted_triangles


def write_triangles(file_name, triangles):
    with open(file_name, "w") as file:
        for group in triangles:
            file.writelines('%s\n' % str(triangle) for triangle in group)
            file.write("----------------\n")


def main(number):
    triangles = read_triangles("tests/input%s.txt" % number)
    sorted_triangles = sort_triangles(triangles)
    write_triangles("tests/output%s.txt" % number, sorted_triangles)


if __name__ == '__main__':
    main("06")
