class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"
    
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"