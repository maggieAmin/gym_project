from db.run_sql import run_sql

from models.gym_class import Gym_class
# from models.member import Member

def save(gym_class):
    sql = "INSERT INTO gym_classes(title, capacity) VALUES (%s, %s) RETURNING id"
    values = [gym_class.title, gym_class.capacity]
    results = run_sql(sql, values)
    gym_class.id = results[0]['id']
    return gym_class

def select_all():
    gym_classes = [ ]
    sql = "SELECT * FROM gym_classes"
    results = run_sql(sql)
    for row in results:
        gym_class = Gym_class(row['title'], row['capacity'], row['id'])
        gym_classes.append(gym_class)
    return gym_classes

def select(id):
    gym_class = None
    sql = "SELECT * FROM gym_classes WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        gym_class = Gym_class(result['title'], result['capacity'], result['id'])
    return gym_class

def gym_classes_for_member(member):
    gym_classes = [ ]
    sql = "SELECT gym_classes.* FROM gym_classes INNER JOIN "