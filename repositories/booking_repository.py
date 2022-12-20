from db.run_sql import run_sql
from models.booking import Booking
from models.gym_class import Gym_class
from models.member import Member
import repositories.gym_class_repository as gym_class_repository
import repositories.member_repository as member_repository

def save(booking):
    sql = "INSERT INTO bookings (member_id, gym_class_id) VALUES (%s, %s) RETURNING id"
    values = [booking.member.id, booking.gym_class.id]
    results = run_sql(sql, values)
    booking.id = results[0]['id']
    return booking

def select_all():
    bookings = [ ]
    sql = "SELECT * FROM bookings"
    results = run_sql(sql)
    for row in results:
        member = member_repository.select(row['member_id'])
        gym_class = gym_class_repository.select(row['gym_class_id'])
        booking = Booking(member, gym_class, row['id'])
        bookings.append(booking)
    return bookings
    
def select(id):
    booking = None
    sql ="SELECT * FROM bookings WHERE id=%s"
    values =[id]
    results = run_sql(sql, values)
    if results:
        result =results[0]
        member = member_repository.select(result['member_id'])
        gym_class = gym_class_repository.select(result['gym_class_id'])
        print(member, gym_class)
        booking = Booking(member, gym_class, result['id'])
    return booking

def update(booking_id, member_id, gym_class_id):
    sql = "UPDATE bookings SET (member_id, gym_class_id) = (%s, %s) WHERE id=%s"
    values = [member_id, gym_class_id, booking_id]
    run_sql(sql, values)
