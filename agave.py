import requests

key = 'sSZmea1S_5_Rkpv1Od3HcxVh7B0a'
secret = 'YiMyZbcjTy2uwEHyg5yME0tF8tEa'
apihost = 'https://agave.iplantc.org/'

class App:
	def __init__(self, username='dalanders', password='Shadow@3876', key=key, secret=secret, apihost=apihost):
		self.apihost = apihost
		self.username = username
		self.password = password
		self.key = key
		self.secret = secret
		self.token = self.getToken()
		self.renewtoken = self.

	def getToken(self):
		dataPayload = {'grant_type':'client_credentials','username':self.username,'password':self.password,'scope':'PRODUCTION'}
		headersPayload = {'Content-Type':'application/x-www-form-urlencoded'}
		req = requests.post(apihost + '/token', auth=(self.key, self.secret), data=dataPayload, headers=headersPayload)
		return req.json()['access_token']

	def get(self, rtype, path):
		rtype = rtype + '/2.0/'
		headersPayload = {'Authorization':'Bearer ' + self.token}
		req = requests.get(apihost + rtype + path, headers = headersPayload)
		return req.json()

	def post(self, rtype, path, data):
		rtype = rtype + '/2.0/'
		dataPayload = data
		headersPayload = {'Authorization':'Bearer ' + self.token}
		req = requests.post(apihost + rtype + path, headers = headersPayload, data=dataPayload)
		return req.json()

	def delete(self, rtype, path):
		rtype = rtype + '/2.0/'
		headersPayload = {'Authorization':'Bearer ' + self.token}
		req = requests.delete(apihost + rtype + path, headers = headersPayload)
		return req.json()

	def put(self, rtype, path, data):
		rtype = rtype + '/2.0/'
		dataPayload = data
		headersPayload = {'Authorization':'Bearer ' + self.token}
		req = requests.put(apihost + rtype + path, headers = headersPayload, data=dataPayload)
		return req.json()