import math

class Regular_Polygons:
    def __init__(self, n):
        self.n = n

    def interior_angle(self):
        answer = 180*(self.n-2)/self.n
        return answer
    # https://careerkarma.com/blog/python-typeerror-int-object-is-not-callable/ ran into scenario 2 here, missing *

    def exterior_angle(self):
        answer = 360/self.n
        return answer

    def radians(self):
        answer = (self.n-2)*math.pi/self.n
        return answer

    def turns(self):
        answer = (self.n-2)/2*self.n
        return answer

    def test_exterior_and_interior_angles(self):
        if(self.interior_angle() + self.exterior_angle() != 180):
            return "Error: sum of interior and exterior angles not equal to 180 degrees"
        else:
            return "Exterior and interior angle functions working"

regular_polygons_instance = Regular_Polygons(5)

print(regular_polygons_instance.interior_angle())
print(regular_polygons_instance.exterior_angle())
print(regular_polygons_instance.radians())
print(regular_polygons_instance.turns())
print(regular_polygons_instance.test_exterior_and_interior_angles())