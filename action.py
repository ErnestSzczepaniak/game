import compute
import constant
import callback


class Move():
    def __init__(self, parent):
        self.parent = parent
        self.steps = 0
        self.speed = 0
        self.on_move = None

    def cartesian(self, destination, speed=100):
        dp = speed * constant.dt
        distance = compute.distance(self.parent.position, destination)

        steps = distance / dp

        if steps > 0:
            dx, dy = compute.deltas(self.parent.position, destination)
            self.parent.velocity.value = [dx / steps, dy / steps]
            self.steps = int(steps)
            self.speed = speed

    def polar(self, distance, angle, speed=100):
        destination = compute.destination(
            self.parent.rect.center, distance, angle)
        self.cartesian(destination, speed)

    def cancel(self):
        self.steps = 0

    def update(self):
        if self.steps >= 1:
            self.parent.position.x.value += self.parent.velocity.x.value
            self.parent.position.y.value += self.parent.velocity.y.value
            self.steps -= 1
            if self.on_move is not None:
                self.on_move()
            if self.steps == 0:
                self.parent.velocity.value = [0, 0]


class Follow():
    def __init__(self, parent):
        self.parent = parent
        self.target = None
        self.distance = 0
        self.counter = 0
        self.period = 0
        self.speed = 100

    def start(self, target, distance, period=constant.dt, speed=100):
        self.target = target
        self.distance = distance
        self.counter = 0
        self.period = period / constant.dt
        self.speed = speed

    def cancel(self):
        self.target = None

    def update(self):
        if self.target is not None:
            self.counter += 1
            if self.counter % self.period == 0:
                self.counter = 0
                distance = compute.distance(
                    self.parent.position, self.target.position)
                if distance > self.distance:
                    self.parent.move.cartesian(
                        self.target.position, self.speed)
                else:
                    self.parent.move.cancel()