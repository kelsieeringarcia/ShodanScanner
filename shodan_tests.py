# import statements
import json
from ShodanClient import ShodanClient

def load_config():
    file_path = "config.default.json"
    with open(file_path) as file:
        data = json.load(file)
    return data

def main():

    data = load_config()

    client = ShodanClient(api_key=data["api_keys"]["shodan"]["key"])


if __name__ == "__main__":
    main()