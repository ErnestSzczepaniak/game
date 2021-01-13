import variable


class Position(variable.Variable):
    def __init__(self, x=0, y=0):
        super().__init__('x', 'y')
        self.x.value = x
        self.y.value = y
    
class Size(variable.Variable):
    def __init__(self, x=0, y=0):
        super().__init__('x', 'y')
        self.x.value = x
        self.y.value = y
    
class Velocity(variable.Variable):
    def __init__(self, x=0, y=0):
        super().__init__('x', 'y')
        self.x.value = x
        self.y.value = y
    
class Acceleration(variable.Variable):
    def __init__(self, x=0, y=0):
        super().__init__('x', 'y')
        self.x.value = x
        self.y.value = y
    
class Spin(variable.Variable):
    def __init__(self, left=0, right=0):
        super().__init__('left', 'right')
        self.left.value = left
        self.right.value = right
