
from flask import Flask, render_template,request
from database import DBhandler
import sys


app = Flask(__name__)
DB=DBhandler()

DB= DBhandler()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/list')
def view_list():
    return render_template('list.html')

@app.route('/restaurantUpload')
def reg_restaurant():
    return render_template('restaurantUpload.html')

@app.route('/mapSearch')
def view_map():
    return render_template('mapSearch.html')  

@app.route('/allergycheck')
def allergy_popup():
    return render_template('allergyPopup.html')

# 가은 - 맛집등록 post

@app.route("/submit_restaurant_post", methods=['POST'])
def reg_restaurant_submit_post():
  
    image_file=request.files["file"]
    image_file.save("static/image/{}".format(image_file.filename))
    data=request.form

    if DB.insert_restaurantUpload(data['Rname'], data, image_file.filename):
        return render_template("result.html", data=data, image_path="static/image/"+image_file.filename)
    else:
        return "Restaurant name already exist!"
    
   

#result.html에서 대표 메뉴 등록으로 이동
@app.route('/menuUpload', methods=['post'])
def menuUpload():
    data=request.form
    return render_template("menuUpload.html",data=data)
    


# 민정 - 대표메뉴등록 post

#@app.route('/menuUpload')
#def menuUpload():
    
 #   return render_template("menuUpload.html")

@app.route("/submit_menu_post", methods=['POST'])
def reg_menu_submit_post():
    # image_file=request.files["file"]
    # image_file.save("static/image/{}".format(image_file.filename))
    name = request.form['menuname']
    price = request.form['menuprice']
    textarea = request.form['menudetail']
    vegan = request.form.get('vegan')
    allergy = request.form.get('allergy')
    allergylist = request.form.get('allergylist')

    print("음식명 : "+name)
    print("가격 : "+price)
    print("메뉴 상세 설명 : "+textarea)
    print("추가 정보 - 비건 여부 : "+str(vegan))
    print("추가 정보 - 알레르기 여부 : "+str(allergy))
    print("알레르기 종류 : "+allergylist)
    return name, price, textarea, vegan, allergy, allergylist
    

# 아래는 여진언니 꺼에서...

@app.route("/submit_review_post", methods=['POST'])
def submit_review_post():

    image_file=request.files["image_uploads"]
    image_file.save("static/image/{}".format(image_file.filename))
    data = request.form

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5001', debug=True)
    