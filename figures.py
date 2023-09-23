from math import tan, pi, atan2, acos
from npPirata import subtractVectors, vectorMagnitude, normVector, dot, multVectorScalar


class Intercept(object):
    def __init__(self, distance, point, normal, texCoords, obj):
        self.distance = distance
        self.point = point
        self.normal = normal
        self.obj = obj
        self.texCoords = texCoords


class Shape(object):
    def __init__(self, position, material):
        self.position = position
        self.material = material

    def ray_intersect(self, orig, dir):
        return None


class Sphere(Shape):
    def __init__(self, position, radius, material):
        self.radius = radius
        super().__init__(position, material)

    def ray_intersect(self, orig, dir):
        L = subtractVectors(self.position, orig)
        magnitudL = vectorMagnitude(L)
        tca = dot(L, dir)
        d = (magnitudL ** 2 - tca ** 2) ** 0.5

        if type(d) is complex:
            d = float(d.real)

        if d > self.radius:
            return None

        thc = (self.radius ** 2 - d ** 2) ** 0.5
        t0 = tca - thc
        t1 = tca + thc

        if t0 < 0:
            t0 = t1
        if t0 < 0:
            return None
        
        dir = multVectorScalar(dir, t0)
        point = [orig[i] + dir[i] for i in range(3)]
        normal = subtractVectors(point, self.position)
        normal = normVector(normal)

        u = (atan2(normal[2], normal[0]) / (2 * pi)) + 0.5
        v = acos(normal[1]) / pi


        return Intercept(t0, point, normal, (u, v), self)

