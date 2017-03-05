import requests

if __name__ == '__main__':
	url = 'http://confeccionesclaudia.com/api/categories'
	response = requests.get(url)

	if response.status_code == 200:
		file = open('data.json', 'wb')
		file.write(response.content)
		file.close()