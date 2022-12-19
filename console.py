import pdb
from models.gym_class import Gym_class
from models.member import Member
from models.booking import Booking
import repositories.gym_class_repository as gym_class_repository
import repositories.member_repository as member_repository
import repositories.booking_repository as booking_repository

member1 = Member('Will Smith')
member_repository.save(member1)

member2 = Member('Jack Sparrow')
member_repository.save(member2)

member3 = Member('Emma Watson')
member_repository.save(member3)

member4 = Member('Jennifer Anston')
member_repository.save(member4)

gym_class1 = Gym_class('Flexibility', 3)
gym_class_repository.save(gym_class1)

gym_class2 = Gym_class('Yoga', 4)
gym_class_repository.save(gym_class2)

gym_class3 = Gym_class('Zumba', 6)
gym_class_repository.save(gym_class3)

booking1 = Booking(member1, gym_class3)
booking_repository.save(booking1)

booking2 = Booking(member2, gym_class3)
booking_repository.save(booking2)

booking3 = Booking(member4, gym_class1)
booking_repository.save(booking3)

booking4 = Booking(member2, gym_class2)
booking_repository.save(booking4)

pdb.set_trace()



