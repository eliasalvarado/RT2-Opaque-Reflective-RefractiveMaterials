
OPAQUE = 0
REFLECTIVE = 1
TRANSPARENT = 2

class Material(object):
    def __init__(self, diffuse = (1, 1, 1), specular = 1, ks = 0, matType = OPAQUE, texture = None):
        self.diffuse = diffuse
        self.specular = specular
        self.ks = ks
        self.matType = matType
        self.texture = texture

