
class Space:
    def __init__(self, name):
        self.name = name

    def activate(self,GameOfLife, player):
        raise NotImplementedError("Subclasses must implement activate()")

    
    class start(space):
        def __init__(self):
            super().__init__("Start")

    def apply(self, GameOfLife, player):
        pass

    class payday():
        def __init__(self):
            super().__init__("Payday")

    def apply(self, GameOfLife, player):
        pass

    class taxpay():
        def __init__(self):
            super().__init__("Taxpay")

    def apply(self, GameOfLife, player):
        pass

    class peaceful_day():
        def __init__(self):
            super().__init__("Peaceful Day")

    def apply(self, GameOfLife, player):
        pass

    class event():
        def __init__(self):
            super().__init__("Event")

    def apply(self, GameOfLife, player):
        pass

    class choice():
        def __init__(self):
            super().__init__("Choice")

    def apply(self, GameOfLife, player):
        pass

    class retirement():
        def __init__(self):
            super().__init__("Retirement")

    def apply(self, GameOfLife, player):
        pass

    