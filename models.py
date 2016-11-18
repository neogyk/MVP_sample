from flask_sqlalchemy import SQLAlchemy
from Evo import app
import config 
from werkzeug.security import generate_password_hash,check_password_hash

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'True'
app.config.from_object('config')
db = SQLAlchemy(app)


	
class Position(db.Model):
	__tablename__ = "position"
	id = db.Column('id',db.Integer,primary_key = True)
	name = db.Column(db.String(20)) 
	description = db.Column(db.Text)	
	user = db.relationship('User',primaryjoin ="Position.id ==  User.position_id" ,backref='position', lazy='subquery')	
	def __init__(self,name,description):
		self.name = name
		self.decription = description
	def serialize(self):
		return {"position_name":self.name,
			"position_description":self.description
			}
	
class Department(db.Model):
	__tablename__ = "department"
	id = db.Column('id',db.Integer,primary_key = True)
	name = db.Column(db.String(20))
	parent = db.Column(db.Integer)
	user = db.relationship('User',primaryjoin ="Department.id ==  User.department_id" ,backref='department', lazy='subquery')
	description = db.Column(db.Text)
	def __init__(self,name,parent,description):
		self.name = name
		self.parent = parent
		self.description = description
	def serialize(self):
		return {"department_name":self.name,
			"department_position":self.description,
			"department_parent":self.parent,
			"department_admin":self.user
			}


class User(db.Model):
	__tablename__ = "user"
	id = db.Column(db.Integer,primary_key = True)
	first_name = db.Column(db.String(20))
	second_name = db.Column(db.String(20))
	department_id = db.Column('department_id',db.Integer,db.ForeignKey('department.id'),unique = True)	
	birth_date = db.Column(db.DateTime)
	phone = db.Column(db.String(8))
	email = db.Column(db.String(20))
	position_id = db.Column('position_id',db.Integer,db.ForeignKey('position.id'))
	def __init__(self,first_name,second_name,phone,email):
		self.first_name = first_name
		self.second_name = second_name
		#self.birth_date = birth_date
		self.phone = phone
		self.email = email
	def edit(self,position,department):
		self.position_id = position
		self.department_id = department
	def __repr__(self):
		return "<User %r>" % self.first_name
    

class Superuser(db.Model):
	__tablename__ = "superuser"
	id = db.Column(db.Integer,primary_key = True)
	login = db.Column(db.String)
	password = db.Column(db.String)
	def __init__(self,login,password):
		self.login = login
		self.password = self.set_password(password)
	def set_password(self,password):
		return generate_password_hash(password)
	def check_password(self,password):
		return check_password_hash(self.password, password)