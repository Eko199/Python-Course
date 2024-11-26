import numpy as np
import math

def pointsToMatrix(points):
    return [
        [*points[0], 1],
        [*points[1], 1],
        [*points[2], 1]
    ]

class Solution:
    def checkStraightLine(self, coordinates):
        return len(coordinates) <= 2 \
            or (math.isclose(np.linalg.det(pointsToMatrix(coordinates[:3])), 0, abs_tol = 1e-8)
                and self.checkStraightLine(coordinates[1:]))