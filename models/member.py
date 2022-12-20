class Member:
    def __init__(self, name, id = None):
        self.name =name
        self.id = id

    def __repr__(self):
        return "<"+str(self.id)+":"+str(self.name)+">"