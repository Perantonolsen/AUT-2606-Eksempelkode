class Manifold:
    def __init__(self, space_dim, object_dim):
        self.space_dim = space_dim
        self.object_dim = object_dim

class CircularManifold(Manifold):
    def __init__(self,radius, space_dim, object_dim):
        self.radius = radius
        self.space_dim = space_dim
        self.object_dim = object_dim

class Circle(CircularManifold):
    def __init__(self,r):
        CircularManifold.__init__(self,r,2,1)
        self.radius = r

m = Manifold(2,3)
cm = CircularManifold(1,2,3)
C = Circle(1)
