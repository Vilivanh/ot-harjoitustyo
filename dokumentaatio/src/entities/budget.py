class Budget:
    def __init__(self, name, user, start, end, tulot = None, menot = None):
        self.user = user
        self.name = name
        self.start = start
        self.end = end
        self.tulot = tulot
        self.menot = menot