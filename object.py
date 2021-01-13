import attribute


class Object():
    def __init__(self):
        self.position = attribute.Position()
        self.size = attribute.Size()
        self.velocity = attribute.Velocity()
        self.acceleration = attribute.Acceleration()
        self.spin = attribute.Spin()
