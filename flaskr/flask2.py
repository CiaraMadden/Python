#A minimal API
from flask import Flask, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

"""
Below if for flask
@app.route('/')
def index():
	return jsonify({'status':'OK'})
"""

#Below is for Flask-RESTful
class HelloWorld(Resource):
	def get(self):
		return {'status':'ok','Name':'Ciara'}

#adds resource to url
api.add_resource(HelloWorld, '/')

if __name__=='__main__':
	app.run(debug=True,host='0.0.0.0')
