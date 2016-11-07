from models import *
db.create_all()

d = Department("111",1,"22 to say")
p = Position('222 Dev','11212-2')
db.session.add(d)
db.session.add(p)
db.session.commit()
#department = Department.query.get(2)
#position = Position.query.get(2)
import datetime 
birthdate= datetime.datetime.now()		
u = User('nadia','didukh',d.id,birthdate,'hero','ledidukh@gmail.com',p.id,False)
#assert session.add(d),"Department add false"

db.session.add(u)
db.session.commit()
