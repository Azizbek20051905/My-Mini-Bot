import requests

class SendMessagesReq:
    def __init__(self, token, filename, chat_id, filetype,name):
        self.token = token
        self.filename = filename
        self.id = chat_id
        self.filetype = filetype
        self.name = name

    def send(self, texts):
        base_url = f'https://api.telegram.org/bot{self.token}/{self.filetype}'

        parameters = {
            "chat_id": str(self.id),
            self.name: self.filename,
            "caption": texts,
        }

        resp = requests.get(base_url, data = parameters)
        print(resp.text)

import requests

class SendMessagesVid:
    def __init__(self, token, filename, chat_id, filetype,name):
        self.token = token
        self.filename = filename
        self.chat_id = chat_id
        self.filetype = filetype
        self.name = name
        
    def sendVideos(self):
        with open(self.filename, 'rb') as file:
            payload = {
                'chat_id': str(self.chat_id),
                'title': self.filename,
                'parse_mode': 'HTML'
            }
            files = {
                self.name: file.read(),
            }
            resp = requests.post(
                f"https://api.telegram.org/bot{self.token}/{self.filetype}",
                data=payload,
                files=files).json()