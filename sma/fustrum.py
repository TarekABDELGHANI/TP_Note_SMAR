from pygame.math import Vector2
class Fustrum :
    def __init__(self,parent = None, r=100):
        self.radius = r
        self.parent = parent

    # Verifie si un objet est dans le champ de vision de notre Agent
    def inside(self,obj):
        if hasattr(obj,"position") :
            if hasattr(obj,"mass") :
                if isinstance(obj.position,Vector2) :
                    if obj.position.distance_to(self.parent.position) < self.radius :
                        return True
        return False