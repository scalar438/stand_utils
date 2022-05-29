import json

class Config:
    def __init__(self, file_name = None):
        if file_name is None:
            file_name = "config.json"
        with open("config.json") as f:
            params = json.load(f)
        self.login = params["login"]
        self.password = params["password"]
        self.login_url =params["login_url"]
        self.schema_name = params["schema_name"]
