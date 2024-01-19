import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        result = response.content
        print(result)
        return result

    def load_json(self):
        response = self.get_response_body()
        result = json.loads(response)
        print(result)
        return result
    
tony = GetRequester('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json')
tony.get_response_body()
tony.load_json()