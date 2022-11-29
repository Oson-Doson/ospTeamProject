from flask import Flask, render_template,request,redirect,url_for
from database import DBhandler
import sys
from config import kakaomap_key


app = Flask(__name__)
DB=DBhandler()

DB= DBhandler()

@app.route('/')
def home():
    return render_template('home.html')

# 맛집리스트화면으로 연결 & 페이징
@app.route('/list')
def view_list():
    return redirect(url_for('list_restaurants'))

@app.route('/restaurantUpload')
def reg_restaurant():
    return render_template('restaurantUpload.html')

@app.route('/mapSearch')
def view_map():
    return render_template('mapSearch.html', map_key=kakaomap_key)  

@app.route('/allergycheck')
def allergy_popup():
    return render_template('allergyPopup.html')

# 추가한 부분 - 리뷰등록 url
@app.route('/reviewUpload')
def reviewUpload():
    return render_template("reviewUpload.html")

# 추가한 부분 - 대표메뉴조회 url
@app.route('/menuShow')
def menuShow():
    return render_template("menuShow.html")

# 맛집등록 post

@app.route("/submit_restaurant_post", methods=['POST'])
def reg_restaurant_submit_post():
  
    image_file=request.files["file"]
    image_file.save("static/image/{}".format(image_file.filename))
    data=request.form

    if DB.insert_restaurantUpload(data['Rname'], data, image_file.filename):
        return render_template("result.html", data=data, image_path="static/image/"+image_file.filename)
    else:
        return "Restaurant name already exist!"
    
   
                                                                                                        
#맛집 등록 -> result.html -> 대표 메뉴 등록으로 이동
@app.route('/menuUpload', methods=['post'])
def menuUpload():
    Rname=request.form
    return render_template("menuUpload.html",data=Rname)
    


# 대표메뉴등록 post

@app.route("/submit_menu_post", methods=['POST'])
def reg_menu_submit_post():
    image_file=request.files["menuimage"]
    image_file.save("static/menu-image-upload/{}".format(image_file.filename))

    data=request.form
    
    if DB.insert_menuUpload(data['menuname'],data,image_file.filename):
        return render_template("home.html")
    else:
        return "Menu name already exist!"




# 리뷰 등록 post
@app.route("/submit_review_post", methods=['POST'])
def submit_review_post():

    image_file=request.files["picture-input"]
    image_file.save("static/review-image/{}".format(image_file.filename))
    data = request.form

    if DB.insert_review(data['nickname'], data, image_file.filename):
        return render_template("home.html")


#app.py 에서 get_restaurants 호출
@app.route("/list_res")
def list_restaurants():
    page = request.args.get("page", 0, type=int)
    limit = 9

    start_idx=limit*page
    end_idx=limit*(page+1)

    data=DB.get_restaurants()
    res_name=DB.get_restaurantsName()
    print(res_name)
    avg_rate=[]
    keys=list(data)
    print(keys)
    for res in res_name:
        avg_rate.append(DB.get_avgrate_byname(res))
 
    
    for i in range(len(data)):
        key=keys[i]
        data[key]['avg_rate']=avg_rate[i]

    print(data)
    tot_count=len(data)
    data = dict(list(data.items())[start_idx:end_idx])

    return render_template(
        "list.html",
        datas=data.items(),
        total=tot_count,
        limit=limit,
        page=page,
        page_count=int((tot_count/9)+1))
                          

# 동적 라우팅 : 맛집 리스트 화면 - 맛집 세부화면 연결 
@app.route("/view_detail/<name>/")
def view_restaurant_detail(name):
    data=DB.get_restaurant_byname(str(name))  #맛집 이름으로 데이터 가져오는 함수
    avg_rate=DB.get_avgrate_byname(str(name))  #맛집 이름으로 평균 평점 가져오는 함수
    review_num=DB.get_reviewnum_byname(str(name))
    print("####data:",data)
    return render_template("details.html",data=data,avg_rate=avg_rate,review_num=review_num)

# 동적 라우팅 : 맛집 세부화면 - 맛집 리뷰등록 화면 
@app.route("/review_post/<name>/")
def review_post(name):
    print(name)
    return render_template("reviewUpload.html",data=name)

# 동적 라우팅 : 맛집 세부화면 - 대표메뉴조회 화면
@app.route("/show_menu/<res_name>/", methods=['POST'])
def view_foods(res_name):
    data = DB.get_food_byname(str(res_name))
    tot_count = len(data)
    # 레스토랑 이름 전달
    res_name=res_name
    return render_template("menuShow.html", datas=data, total=tot_count, res_name=res_name)

# 동적 라우팅 : 맛집 세부화면 - 맛집 메뉴등록 화면 
@app.route("/menu_post/<name>/")
def menu_post(name):
    print(name)
    return render_template("menuUpload copy.html",data=name)

# 동적 라우팅 : 맛집 세부화면 - 맛집 리뷰조회 화면 
@app.route("/review_show/<res_name>/", methods=['POST'])
def review_show(res_name):
    data=DB.get_review_byname(str(res_name))  #맛집 이름으로 리뷰 데이터 가져오는 함수
    avg_rate=DB.get_avgrate_byname(str(res_name))  #맛집 이름으로 평균 평점 가져오는 함수
    review_num=DB.get_reviewnum_byname(str(res_name))
    res_name=res_name
    print("####dataaa:",data)
    return render_template("reviewShow.html",datas=data, avg_rate=avg_rate, review_num=review_num, res_name=res_name)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5001', debug=True)
    
