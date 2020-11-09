class Vector:

    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'x = {self.x}, y = {self.y}, z = {self.z}'

    def __add__(self, other):

        return Vector(
            x=self.x + other.x,
            y=self.y + other.y,
            z=self.z + other.z
        )

    def __sub__(self, other):
        return Vector(
            x=self.x - other.x,
            y=self.y - other.y,
            z=self.z - other.z
        )

    def __mul__(self, other):
        return Vector(
            x=self.x * other.x,
            y=self.y * other.y,
            z=self.z * other.z
        )

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        return self

    def __imul__(self, other):
        self.x *= other.x
        self.y *= other.y
        self.z *= other.z
        return self


A = Vector(1, 2, 3)
B = Vector(5, 2, 3)
print(A)
A += B
print(A)
