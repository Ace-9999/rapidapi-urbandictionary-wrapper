import requests

api_key = None
global api_key

class UrbanClient(api_key):
	api_key = api_key

	def get_definition(word):
		res=InnerSystem.request(word, api_key)
		return res["definition"]

	def get_url(word):
		res=InnerSystem.request(word, api_key)
		return res["permalink"]

	def get_example(word):
		res=InnerSystem.request(word, api_key)
		return res["example"]

	def get_stats(word):
		res=InnerSystem.request(word, api_key)
		return res["thumbs_up"], res["thumbs_down"]
	
	def get_word_info(word):
		res=InnerSystem.request(word, api_key)
		return res

class InnerSystem:
	def request(to_define, api_key):
		url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"

		querystring = {"term":to_define}

		headers = {
			'x-rapidapi-key': {api_key},
			'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com"
			}

		response = requests.request("GET", url, headers=headers, params=querystring)
		return response.json()["list"][0]