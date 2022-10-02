# Tell me a joke

import requests
import json

def get_joke():
    response = requests.get("https://icanhazdadjoke.com/", headers={"Accept": "application/json"})
    return json.loads(response.text)["joke"]

if __name__ == "__main__":
    print(get_joke())