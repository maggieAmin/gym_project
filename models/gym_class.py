class Gym_class:
    def __init__(self, title, capacity, id = None):
        self.title = title
        self.capacity = capacity
        self.id = id

    def __repr__(self):
        return "<"+str(self.id)+":"+str(self.title)+"-"+str(self.capacity)+">"