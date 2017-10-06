from __future__ import print_function
import requests


def insertInfo(name,location):
	requests.post('http://127.0.0.1:5000/sms/update/'+name+'/'+location)

def getInfo(name,location):
	requests.get('http://127.0.0.1:5000/sms/'+name)

if __name__ == '__main__':
	
	insertInfo('Ciara', 'Dublin')
	getInfo('Ciara','Dublin')
	getInfo('Derri','2')


"""
	print(r.status_code)
	print(r.headers)
	print(r.text)
	print(r.json())
"""
