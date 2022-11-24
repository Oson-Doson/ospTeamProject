import pyrebase
import json

class DBhandler:
    def __init__(self):
        with open('./authentication/firebase_auth.json') as f:
            config=json.load(f)

        firebase = pyrebase.initialize_app(config)
        self.db = firebase.database()

    
    """식당 데이터 등록""" 

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
            self.db.child("restaurant").push(restaurant_info)
            print(data,image_path)
            return True
        else:
            return False

    def restaurant_duplicate_check(self, name):
        restaurants = self.db.child("restaurant").get()
        for res in restaurants.each():
            value=res.val()

            if value['Rname'] == name:
                return False
        return True


    """리뷰 데이터 등록"""

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
    


    """메뉴 데이터 등록""" 

    def insert_menuUpload(self,name,data,image_path):
        menu_info={
            "restaurant_name" : data['Rname'],
            "menuname" : data['menuname'],
            "menuprice" : data['menuprice'],
            "menudetail" : data['menudetail'],
            "vegan" : data['vegan'],
            "allergy" : data['allergy'],
            "allergylist" : data['allergylist'],
            "image_path" : image_path
        }

    
        if self.menu_duplicate_check(name):
                self.db.child("menu").child(name).push(menu_info)
                print(data,image_path)
                return True
        else:
                return False

    def menu_duplicate_check(self, name):
        menus = self.db.child("menu").get()
        for m in menus.each():
            value=m.val()

            if value['menuname'] == name:
                return False
        return True


    def get_restaurants(self):
        restaurants=self.db.child("restaurant").get().val()


    """맛집 이름으로 restaurant 테이블에서 정보 가져오기"""

    def get_restaurant_byname(self,name):
        restaurants=self.db.child("restaurant").get()
        target_value=""
        for res in restaurants.each():
            value=res.val()

            if value['name']==name:
                target_value=value
        return target_value


    """맛집 이름으로 review 테이블에서 평점 가져와서 평균 계산하기"""

    def get_avgrate_byname(self,name):
        reviews=self.db.child("review").get()
        rates=[]
        for res in reviews.each():
            value=res.val()
            if value['restaurant_name']==name:
                rates.append(float(value['rate']))
        return sum(rates)/len(rates)