from __future__ import print_function
import requests

if __name__ == '__main__':
	
	r = requests.get('https://api.google.ie')

	print(r)
	print(r.status_code)