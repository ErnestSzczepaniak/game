import math


def distance(p1, p2):
    return math.sqrt(((p1.x.value-p2.x.value)**2)+((p1.y.value-p2.y.value)**2))


def deltas(p1, p2):
    return p2.x.value - p1.x.value, p2.y.value - p1.y.value


def angle(p1, p2):
    dx, dy = deltas(p1, p2)
    return math.degrees(math.atan2(dy, dx))


def destination(point, distance, angle):
    theta = math.radians(angle)
    return point[0] + distance * math.cos(theta), point[1] + distance * math.sin(theta)

def are_intersecting(p1, s1, p2, s2):
    pass
    # r1 = [self.position.value[0] - self.size.value[0] / 2, 
    #     self.position.value[1] - self.size.value[1] / 2,
    #     self.position.value[0] + self.size.value[0] / 2, 
    #     self.position.value[1] + self.size.value[1] / 2]

    # r2 = [object.position.value[0] - object.size.value[0] / 2,
    #     object.position.value[1] - object.size.value[1] / 2,
    #     object.position.value[0] + object.size.value[0] / 2,
    #     object.position.value[1] + object.size.value[1] / 2]

    # if (r1[0] > r2[2]) or (r1[2] < r2[0]) or (r1[3] < r2[1]) or (r1[1] > r2[3]):
    #     return False
    # else:
    #     return True