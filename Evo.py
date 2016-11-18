from flask import Flask,render_template,request,redirect,session,g,url_for,jsonify
from models import *

app = Flask(__name__)
app.secret_key = 'some secret key'

@app.route('/')
def main():
	return render_template("auth.html")
#Login controller
@app.route('/login',methods = ['POST'])
def login():
	if request.method == "POST":
		data = request.json
		email = data['login']
		password = data['password']	
		superuser = Superuser.query.filter_by(login=email).first()
		status = "Error"
		if superuser.check_password(password):
			status = "Logined"
			session['login']=email
		else:
			status = "Error"	
		print(status)
	return jsonify({'status':status})

#registration controller
@app.route('/register',methods = ['POST'])
def register():
	if request.method == "POST":
		data = request.json
		#check()
		superuser = Superuser(data['login'],data['password'])
		db.session.add(superuser)
		db.session.commit()
		status = 'Success'
		print(status)
	return jsonify({'status':status})

#logout
@app.route('/logout')
def logout():
	session.pop('username',None)
	return redirect(url_for('/'))

@app.route('/user',methods = ['GET','POST','PUT','DELETE'])
def user():
	if request.method == "GET":
		if 'login' in session:
			users = User.query.all()
			departments =  Department.query.all()
			positions = Position.query.all()
			position_data = [d.serialize() for d in positions]
			print(position_data)
			department_data = [d.serialize() for d in departments]
			data = {'department':department_data,'position':position_data}
			print(data)
			print(department_data)
			return render_template("user.html",data = data)
	elif request.method == "POST":
		data = request.json
		print(data)
		user = User(data['first_name'],data['second_name'],data['email'],data['phone'])
		db.session.add(user)
		if db.session.commit():
			status = "Success"
		else:
			status = "Error"
		return jsonify({'status':status})
	elif request.method == "PUT":
		data = request.json
		user = User.query.filter_by(id = data['id']).first()
		db.session()
	elif request.method == "DELETE":
		data = request.json
		user = User.query.filter_by(id = data['id']).first()
		db.session.delete(user)

@app.route('/department',methods = ['GET','POST','PUT','DELETE'])
def department():
	if request.method == "GET":
		departments = Department.query.all()
	elif request.method == "POST":
		data = request.json
		print(data)
		department = Department(data['name'],0,data['description'])
		print(department)
		db.session.add(department)
		if db.session.commit():
			status = "Success"
		else:
			status = "Error"
		return jsonify(status=status)

	elif request.method == "PUT":
		pass
	elif request.method == "DELETE":
		pass

@app.route('/position',methods = ['GET','POST','PUT','DELETE'])
def position():
	if request.method == "GET":
		position = Position.query.all()
		responce_data = jsonify([d.serialize for d in position])
		return responce_data
	elif request.method == "POST":
		data = request.json
		position = Position(data['position_name'],data['position_description'])
		print(data)
		db.session.add(position)
		if db.session.commit():
			status = 'Success'
		else:
			status = "Error"
		return jsonify({'status':status})
	elif request.method == "PUT":
		pass
	elif request.method == "DELETE":
		pass


if __name__ == '__main__':
    app.run()
