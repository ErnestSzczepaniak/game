class Callback():
    def __init__(self, function, *args, **kwargs):
        self.function = function
        self.args = args
        self.kwargs = kwargs

    def __call__(self):
        self.function(*self.args, **self.kwargs)
