from db.run_sql import run_sql
from models.member import Member

def save(member):
    if member_exists(member.name):
        return
    sql ="INSERT INTO members(name) VALUES (%s) RETURNING *"
    values = [member.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    member.id = id
    return member

def select_all():
    members = [ ]
    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for row in results:
        member = Member(row['name'], row['id'])
        members.append(member)
    return members

def select(id):
    member = None
    sql = "SELECT * FROM members WHERE id =%s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        member = Member(result['name'], result['id'])
    return member

def update(member):
    sql = "UPDATE members SET name=%s WHERE id=%s"
    values = [member.name, member.id]
    run_sql(sql, values)

def member_exists(name):
    members = select_all()
    for member in members:
        if member.name == name:
            return True
    else:
        return False