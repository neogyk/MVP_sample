import unittest
import os
import Evo
from models import *



class EvoTest(unittest.TestCase):
	def setUp(self):
		self.app = Evo.app.test_client()
		Evo.app.config['TESTING']=True
	def test_main_page(self):
		responce = self.app.get('/login')
		assert '<html>' in responce.data,"Error"	
	def add_items(self):
		self.department = Department("R&D",0,"Research and Development")
		self.position = Position("Lead Researcher","Main researcher in the department")
		import datetime 
		birthdate= datetime.datetime.now()		
		self.user = User('volodimir','klichko',birthdate,'0985127378','klichko@gmail.com',self.position.id,self.department.id,False)	
	def test_db(self):
		self.add_items()
		print(self.department)
		assert db.session.add(self.department),"Department add false"
		assert db.session.add(self.position),"Position add false"
		assert db.session.add(self.user),"User add false"
		assert session.commit(),"Commit false"

		assert Position.query.get(1).name=="Lead Researcher",'False quering Position'
		assert Department.query.get(1).name=="R&D",'False quering Department'
		assert User.query.get(1).first_name=="volodimir",'False quering User'	
	
	def tearDown(self):
		db.session.rollback()
if __name__ == "__main__":
    unittest.main()
