import requests

if __name__ == '__main__':
	url = 'http://httpbin.org/get'
	args = {'firstName': 'Luis', "lastName": 'Charres'}
	response = requests.get(url, params = args)
	print(response.url)

	if response.status_code == 200:
		response_json = response.json() #Dictionary
		firstName = response_json['args']['firstName']
		print(firstName)
