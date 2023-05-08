import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        request_list = []
        requests = json.loads(self.get_response_body())
        for request in requests:
            request_list.append(request)
        return request_list