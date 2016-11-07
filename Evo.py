from flask import Flask,render_template,request,redirect,session,g,url_for,jsonify
from models import *

app = Flask(__name__)

@app.route('/')
def main():
	return render_template("auth.html")

@app.route('/login',methods = ['POST'])
def login():
	if request.method == "POST":
		data = request.json
		email = data['email']
		password = data['password']	
		try:
			user = User.query.filter('email')
			if user.check_password(password):
				status = "Logined"
				session['email']=email
		except:
			status = "Failed"
	return jsonify({'status':status})

@app.route('/register',methods = ['POST'])
def register():
	if request.method == "POST":
		data = request.json
		user = User(data['first_name'],data['second_name'],data['birth_date'],data['phone'],data['email'],data['password'])
		try:
			db.session.add(u)
			db.session.commit()
			status = 'Success'
		except:
			status = 'Error'
	return jsonify({'status':status})

@app.route('/logout')
def logout():
	session.pop('username',None)
	return redirect(url_for('/'))

@app.route('/user',methods = ['GET','POST','PUT','DELETE'])
def user():
	if request.method == "GET":
		if 'username' in session:
			users = User.query.all()
			return render_template(main.html)
	elif request.method == "POST":
		data = request.json
		user = Department(data['name'],data['parent'],data['description'])
		try:
			db.session.add(department)
			db.session.commit()
			status = 'Success'
		except:
			status = 'Error'
		return jsonify({'status':status})
	elif request.method == "PUT":
		pass
	elif request.method == "DELETE":
		pass

@app.route('/departnment',methods = ['GET','POST','PUT','DELETE'])
def department():
	if request.method == "GET":
		pass
	elif request.method == "POST":
		pass 
	elif request.method == "PUT":
		pass
	elif request.method == "DELETE":
		pass

@app.route('/position',methods = ['GET','POST','PUT','DELETE'])
def position():
	if request.method == "POST":
		data = request.json
		department = Department(data['name'],data['parent'],data['description'])
		try:
			db.session.add(department)
			db.session.commit()
			status = 'Success'
		except:
			status = 'Error'
		return jsonify({'status':status})
	elif request.method == "PUT":
		pass
	elif request.method == "DELETE":
		pass


if __name__ == '__main__':
    app.run()
