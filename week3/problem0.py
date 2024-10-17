from math import pi, isclose, atan, sin, cos, sqrt

class PolarCoordinate:
    def __init__(self, r, phi):
        self._r = r
        self._phi = phi

    @property
    def r(self):
        return self._r
    
    @property
    def phi(self):
        return self._phi

    def to_cartesian(self):
        return self._r * cos(self._phi), self._r * sin(self._phi)
    
    @classmethod
    def from_cartesian(cls, x, y):
        return cls(sqrt(x ** 2 + y ** 2), atan(y / x))
    
    def __repr__(self):
        return f"PolarCoordinate({self._r}, {self._phi})"
    
    def __str__(self):
        return f"(r: {self._r}, angle: {self._phi})"
    
    def __hash__(self):
        return hash((self._r, self._phi))
    
    def __eq__(self, value):
        return self._r == value._r and self._phi == value._phi
    
    def __ne__(self, value):
        return not self == value
    
p1 = PolarCoordinate(1, pi/6)

print(p1.r == 1)
print(p1.phi == pi/6)

p2 = PolarCoordinate.from_cartesian(3, 4)
print(isclose(p2.r, 5))
print(isclose(p2.phi, atan(4/3)))

x, y = p2.to_cartesian()
print(isclose(x, 3))
print(isclose(y, 4))

p3 = PolarCoordinate(1, 0)
print(str(p3) == "(r: 1, angle: 0)")
print(repr(p3) == "PolarCoordinate(1, 0)")

pp1, pp2, pp3 = PolarCoordinate(1, pi/6), PolarCoordinate.from_cartesian(3, 4), PolarCoordinate(1, 0)
print(p1 == pp1)
print(p2 == pp2)
print(p3 == pp3)

d = {p1: "A", p2: "B", p3: "C"}
print(d[pp1] == "A")
print(d[pp2] == "B")
print(d[pp3] == "C")

s = {p1, p2, p3, pp1, pp2, pp3, p1, p2, p3}
print(len(s) == 3)