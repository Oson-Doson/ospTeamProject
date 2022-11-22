import pyrebase
import json

class DBhandler:
    def __init__(self):
        with open('./authentication/firebase_auth.json') as f:
            config=json.load(f)

        firebase = pyrebase.initialize_app(config)
        self.db = firebase.database()

    
        
    def insert_restaurantUpload(self, name, data, image_path):
        restaurant_info = {
            "Rname":data['Rname'],
            "address":data['address'],
            "tel1":data['tel1'],
            "tel2":data['tel2'],
            "tel3":data['tel3'],
            "foodchoice":data['foodchoice'],
            "moodchoice":data['moodchoice'],
            "pircechoice":data['pricechoice'],
            "parking":data['parking'],
            "openhour":data['openhour'],
            "openmin":data['openmin'],
            "closehour":data['closehour'],
            "closemin":data['closemin'],
            "image_path":image_path
        }
        
        
        if self.restaurant_duplicate_check(name):
            self.db.child("restaurant").child(name).set(restaurant_info)
            print(data,image_path)
            return True
        else:
            return False

    def restaurant_duplicate_check(self, name):
        restaurants = self.db.child("restaurant").get()
        for res in restaurants.each():
            if res.key() == name:
                return False
            return True

    def insert_review(self, name, data, image_path):
        review_content = {
            "nickname": data['nickname'],
            "mood": data['moodchoice'],
            "taste": data['taste'],
            "star": data['star'],
            "text": data['text'],
            "image_path": image_path
        }
        self.db.child("review").child(name).set(review_content)
        print(data, image_path)
        return True
    

    def insert_menuUpload(self,name,data,image_path):
        menu_info={
            "식당이름" : data['Rname'],
            "메뉴 이름" : data['menuname'],
            "메뉴 가격" : data['menuprice'],
            "메뉴 상세" : data['menudetail'],
            "비건 여부" : data['vegan'],
            "알러지 여부" : data['allergy'],
            "알러지 목록" : data['allergylist'],
            "image_path" : image_path
        }

        if self.menu_duplicate_check(name):
                self.db.child("menu").child(name).set(menu_info)
                print(data,image_path)
                return True
        else:
                return False

    def menu_duplicate_check(self, name):
        menus = self.db.child("menu").get()
        for m in menus.each():
            if m.key() == name:
                return False
            return True
