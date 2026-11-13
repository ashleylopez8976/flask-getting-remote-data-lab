import requests
import json


class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        # Fetch the URL and return the response body as bytes.
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        # Convert the JSON response into Python lists and dictionaries.
        return json.loads(self.get_response_body())