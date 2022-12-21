from db.run_sql import run_sql

from models.gym_class import Gym_class
# from models.member import Member

def save(gym_class):
    sql = "INSERT INTO gym_classes(title, class_datetime, capacity) VALUES (%s, %s, %s) RETURNING id"
    values = [gym_class.title, gym_class.class_datetime, gym_class.capacity]
    results = run_sql(sql, values)
    gym_class.id = results[0]['id']
    return gym_class

def select_all():
    gym_classes = [ ]
    sql = "SELECT * FROM gym_classes"
    results = run_sql(sql)
    for row in results:
        gym_class = Gym_class(row['title'], row['class_datetime'], row['capacity'], row['id'])
        gym_classes.append(gym_class)
    return gym_classes

def select(id):
    gym_class = None
    sql = "SELECT * FROM gym_classes WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        gym_class = Gym_class(result['title'], result['class_datetime'], result['capacity'], result['id'])
    return gym_class

def update(gym_class):
    sql = "UPDATE gym_classes SET (title, class_datetime, capacity) = (%s, %s, %s) WHERE id=%s" 
    values = [gym_class.title, gym_class.class_datetime, gym_class.capacity]
    run_sql(sql, values)

def select_upcoming():
    upcoming_gym_classes = [ ]
    sql = "SELECT * FROM gym_classes WHERE class_datetime > current_date "
    results = run_sql(sql)
    for row in results:
        gym_class = Gym_class(row['title'], row['class_datetime'], row['capacity'], row['id'])
        upcoming_gym_classes.append(gym_class)
    return upcoming_gym_classes