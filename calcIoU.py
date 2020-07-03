from edge import Edge
from point import Point
from polygon import Polygon
from intersection import convexIntersect
import random
from time import time

def calcIoU(poly1, poly2):
    st = time()
    intersec_poly = convexIntersect(poly1, poly2)
    if not intersec_poly:
    # no intersection, IoU 0
        return 0
    else:
        intersec_area = intersec_poly.area()
        union_area = poly1.area() + poly2.area() - intersec_area
        if union_area <= 0:
            # error handle
            return -1
        return intersec_area / union_area
    print("time consumed: {}".format(time() - st))


if __name__ == "__main__":
    poly1 = Polygon([
        Point(-0.7071067811865475, 0.7071067811865476),
        Point(0.30901699437494723, -0.9510565162951536),
        Point(0.5877852522924729, -0.8090169943749476),
    ])
    poly2 = Polygon([
        Point(1, 0),
        Point(0, 1),
        Point(-1, 0),
        Point(0, -1),
        Point(0.7071067811865475, -0.7071067811865477),
    ])
    print(calcIoU(poly1, poly2))
