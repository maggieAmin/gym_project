class Booking:
    def __init__(self, member, gym_class, id = None):
        self.member = member
        self.gym_class = gym_class
        self.id = id

    def __repr__(self):
        return "<"+str(self.id)+":"+str(self.member)+"-"+str(self.gym_class)+">"