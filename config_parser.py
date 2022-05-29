import json

class Config:
    def __init__(self, file_name = None):
        if file_name is None:
            file_name = "stand_utils/config.json"
        with open(file_name) as f:
            params = json.load(f)
        self.login = params["login"]
        self.password = params["password"]
        self.auth_url =params["auth_url"]
        self.schema_name = params["schema_name"]
