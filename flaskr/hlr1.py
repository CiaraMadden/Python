#A minimal API
from flask import Flask, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

data = dict()

class Update(Resource):
	def post(self, name, location):
		#to be able to acces the data dict on line 8
		global data
		data[name] = location
		return {'status':'ok'}

class Locate(Resource):
	def get(self,name):
		#to be able to acces the data dict on line 8
		global data
		try:
			return {'sub':name,'location':data[name]}
		except:
			return{'MESSAGE': 'User ' + name + ' not registered'}


#adds resource to url
api.add_resource(Update, '/sms/update/<name>/<location>')
api.add_resource(Locate, '/sms/<name>/')


if __name__=='__main__':
	app.run(debug=True,host='0.0.0.0')

#curl ..... -x POST