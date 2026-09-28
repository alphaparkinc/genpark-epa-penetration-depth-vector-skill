from client import EPA2D

simplex = [(-1.0, -1.0), (1.0, -1.0), (0.0, 1.0)]
depth, normal = EPA2D.compute_penetration(simplex)
print(f"Penetration Depth: {depth:.4f}, Normal: {normal}")
