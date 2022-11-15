import pyrebase
import json

class DBhandler:
    def _init_(self):
        with open('./authentication/firebase_auth.json') as f:
            config=json.load(f)
        
        firebase=pyrebase.initialize_app(config)
        self.db=firebase.database()

    def insert_restaurant(self,Rname,data):
        restaurant_info={
            "address":data['address'],
            "tel1":data['tel1'],
            "tel2":data['tel2'],
            "tel3":data['tel3'],
            "foodchoice":data['foodchoice'],
            "moodchoice":data['moodchoice'],
            "parking":data['parking'],
            "openhour":data['openhour'],
            "openmin":data['openmin'],
            "closehour":data['closehour'],
            "closemin":data['closemin']
        }
        self.db.child("restaurant").child(Rname).set(restaurant_info)
        print(data)
        return True