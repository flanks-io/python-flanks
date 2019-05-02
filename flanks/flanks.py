import requests


class Flanks():
    access_key = ''
    dns = ''
    session = ''
    
    def __init__(self, access_key, env='sandbox'):
        self.access_key = access_key 
        self.dns = 'https://'+env+'splitapp.one'
        self.session = requests.Session()
        headers = {
            'Content-Type': "application/json",
            'Pragma': "no-cache",
            'cache-control': "no-cache",
        }
        self.session.headers.update(headers)

    def create_user(self,username, password, bank, password2=None):
        data = {
            'username': username,
            'password': password,
            'bank': bank,
            'password2': password2
        }
        r = self.session.post(self.dns + '/server/api/aggregation/user', data=data)
        if 'message' in r.json():
            raise Exception(r.json()['message'])
        return r.json()['user_token']

    
    def get_one_shot(self,username, password, bank, password2=None):
        data = {
            'username': username,
            'password': password,
            'bank': bank,
            'password2': password2,
            'access_key': self.access_key
        }
        r = self.session.post(self.dns + '/server/api/aggregation/user', data=data)
        if 'message' in r.json():
            raise Exception(r.json()['message'])
        return r.json()['user_token']
    
    def get_data(self,user_token):
        data = {
            "user_token": user_token,
            "access_key": self.access_key
        }
        r = self.session.post(self.dns + '/server/api/aggregation/data', data=data)
        if 'message' in r.json():
            raise Exception(r.json()['message'])
        return r.json()


    def delete_user(self,user_token):
        data = {
            "user_token": user_token,
            "access_key": self.access_key
        }
        r = self.session.post(self.dns + '/server/api/aggregation/data', data=data)
        return r.json()['message'] 
