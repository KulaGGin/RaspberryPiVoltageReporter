from FakeTransformerCurrentProvider import FakeTransformerCurrentProvider
import requests

class TransformerCurrentReporter():
    def __init__(self, fakeTransformerCurrentProvider, url):
        self.url = url
        self.fakeTransformerCurrentProvider = fakeTransformerCurrentProvider

    def ReportCurrent(self):
        current = self.fakeTransformerCurrentProvider.GetCurrent()
        recording = {'reading': '0.1', 'xpage': 'plain', 'outputSyntax': 'plain'}
        response = requests.get(self.url, params=recording, verify=True)
        print(f"Made a request to page: {self.url}")
        print(f"Response code is: {response}")
        print(f"Response content is: {response.text}")
        print(f"Tried to push current with value: {current}")