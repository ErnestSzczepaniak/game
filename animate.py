import loader


class Animate():
    def __init__(self, parent):
        self.active = False
        self.parent = parent
        self.index = 0
        self.length = 0
        self.move = ''
        self.direction = ''

    def start(self, move, direction):
        self.active = True
        if self.move != move:
            self.index = 0
        self.move = move
        self.direction = direction
        self.length = len(loader.animations['hero'][move][direction])

    def update(self):
        if self.active:
            self.parent.image = loader.animations['hero'][self.move][self.direction][self.index]
            self.index += 1
            self.parent.dirty = True
            if self.index == (self.length - 1):
                self.index = 0
