"""Expanding Polytope Algorithm (EPA) 2D Engine.
100% Python Standard Library.
"""

import math

class EPA2D:
    """Expanding Polytope Algorithm for 2D penetration depth and normal."""
    @staticmethod
    def compute_penetration(simplex):
        min_dist = float("inf")
        normal = (0.0, 0.0)
        n = len(simplex)
        for i in range(n):
            j = (i + 1) % n
            p1, p2 = simplex[i], simplex[j]
            edge = (p2[0] - p1[0], p2[1] - p1[1])
            norm = (-edge[1], edge[0])
            norm_len = math.hypot(norm[0], norm[1])
            if norm_len > 0:
                norm = (norm[0] / norm_len, norm[1] / norm_len)
                d = abs(p1[0] * norm[0] + p1[1] * norm[1])
                if d < min_dist:
                    min_dist = d
                    normal = norm
        return min_dist, normal
