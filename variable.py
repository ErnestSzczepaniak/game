import sys
import callback
import copy


class Value():
    def __init__(self):
        self._value = 0
        self._min = -sys.maxsize
        self._max = sys.maxsize
        self.on_change = None
        self.backup = ()

    def save(self):
        self.backup = (self._value, self._min, self._max, self.on_change)

    def restore(self):
        self._value = self.backup[0]
        self._min = self.backup[1]
        self._max = self.backup[2]
        self.on_change = self.backup[3]

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        tmp = self._value
        if value < self._min:
            self._value = self._min
        elif value > self._max:
            self._value = self._max
        else:
            self._value = value

        if self._value != tmp and self.on_change is not None:
            self.on_change()

    @property
    def min(self):
        return self._min

    @property
    def max(self):
        return self._max

    @min.setter
    def min(self, value):
        self._min = value
        self.value = self._value

    @max.setter
    def max(self, value):
        self._max = value
        self.value = self._value


class Variable():
    def __init__(self, *names):
        for name in names:
            self.__dict__[name] = Value()
    
    def save(self):
        for key, item in self.__dict__.items():
            item.save()

    def restore(self):
        for key, item in self.__dict__.items():
            item.restore()

    @property
    def value(self):
        return [item.value for item in self.__dict__.values()]
    
    @value.setter
    def value(self, values):
        for value, key in zip(values, self.__dict__.keys()):
            self.__dict__[key].value = value

    @property
    def min(self):
        return [value.min for value in self.__dict__.values()]

    @min.setter
    def min(self, values):
        for value, key in zip(values, self.__dict__.keys()):
            self.__dict__[key].min = value

    @property
    def max(self):
        return [value.max for value in self.__dict__.values()]

    @max.setter
    def max(self, values):
        for value, key in zip(values, self.__dict__.keys()):
            self.__dict__[key].max = value

    # def __str__(self):
    #     str = ''
    #     for key, item in self.dict.items():
    #         show_min = '-inf' if item.min == -sys.maxsize else item.min
    #         show_max = 'inf' if item.max == sys.maxsize else item.max
    #         str += '{}: [{}] ({}, {}) '.format(key,
    #                                            item.value, show_min, show_max)
    #     return str
