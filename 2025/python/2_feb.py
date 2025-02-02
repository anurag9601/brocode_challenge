def perimeter_of_triangle(points):

    #Euclidean distance formula
    def distance(p1, p2):
        return ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2) ** 0.5

    side1 = distance(points[0], points[1])
    side2 = distance(points[1], points[2])
    side3 = distance(points[2], points[0])

    perimeter = side1 + side2 + side3

    return round(perimeter, 2)

# print(perimeter_of_triangle([[15, 7], [5, 22], [11, 1]]))
# print(perimeter_of_triangle([[0, 0], [0, 1], [1, 0]]))
# print(perimeter_of_triangle([[-10, -10], [10, 10 ], [-10, 10]]))


