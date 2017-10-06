from __future__ import print_function
import requests

if __name__ == '__main__':
	
	r = requests.get('http://127.0.0.1:5000/')

	print(r.status_code)
	print(r.headers)
	print(r.text)
	print(r.json())

