from flask import Flask, render_template,request,redirect,url_for
from database import DBhandler
import sys
sys.setrecursionlimit(10**6)
from config import kakaomap_key


app = Flask(__name__)
DB=DBhandler()

DB= DBhandler()

@app.route('/')
def home():
    return redirect(url_for('osondoson_home'))

# 맛집리스트화면으로 연결 & 페이징
@app.route('/list')
def view_list():
    return redirect(url_for('list_restaurants'))

@app.route('/restaurantUpload')
def reg_restaurant():
    return render_template('restaurantUpload.html')

@app.route('/mapSearch')
def view_map():
    korean=DB.get_restaurants_byfoodchoice(str('한식'))
    chinese=DB.get_restaurants_byfoodchoice(str('중식'))
    japanese=DB.get_restaurants_byfoodchoice(str('일식'))
    western=DB.get_restaurants_byfoodchoice(str('양식'))
    cafe=DB.get_restaurants_byfoodchoice(str('카페'))
    return render_template(
        'mapSearch.html', 
        map_key=kakaomap_key, 
        korean=korean, 
        chinese=chinese, 
        japanese=japanese, 
        western=western, 
        cafe=cafe
    )  

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
        return redirect(url_for('menu_result',res_name=data['Rname']))
    else:
        return "Menu name already exist!"


# 리뷰 등록 post
@app.route("/submit_review_post", methods=['POST'])
def submit_review_post():

    image_file=request.files["picture-input"]
    image_file.save("static/review-image/{}".format(image_file.filename))
    data = request.form

    if DB.insert_review(data['nickname'], data, image_file.filename):
        return redirect(url_for('review_result',res_name=data['Rname']))



@app.route("/osondoson")
def osondoson_home():
    print('로딩 시간이 왜이렇게 오래걸리는지를 알기 위한 print문...')
    total=DB.starSort()
    print('1111111111111111111111111111111111111111111111')
    korean=DB.starSort_cate('한식')
    print('1111111111111111111111111111111111111111111111')
    chinese=DB.starSort_cate('중식')
    print('1111111111111111111111111111111111111111111111')
    japanese=DB.starSort_cate('일식')
    print('1111111111111111111111111111111111111111111111')
    western=DB.starSort_cate('양식')
    print('1111111111111111111111111111111111111111111111')
    cafe=DB.starSort_cate('카페')
    print('222222222222222222222222222222222222222')
    #home.html section 2 ) total 을 리뷰 개수 순으로 내림차순 정렬 , 리뷰 개수가 가장 많은 세 개의 식당 정보를 gold, silver, bronze 변수에 저장
    a=DB.reviewNumSort()
    print('3333333333333333333333333333333333333')
    gold=a[0]
    silver=a[1]
    bronze=a[2]
    goldreview=DB.get_review_byname(gold[1]['Rname'])
    silverreview=DB.get_review_byname(silver[1]['Rname'])
    bronzereview=DB.get_review_byname(bronze[1]['Rname'])
    print('3333333333333333333333333333333333333')
    page = 0
    limit = 6
    start_idx=limit*page
    end_idx=limit*(page+1)
    tot_count=len(total)
    kor_count=len(korean)
    chi_count=len(chinese)
    jap_count=len(japanese)
    wes_count=len(western)
    caf_count=len(cafe)
    print('22222222222222222222222222222222222222222222222')
    total_sec=dict(list(total.items())[6:12])
    korean_sec = dict(list(korean.items())[6:12])
    chinese_sec = dict(list(chinese.items())[6:12])
    japanese_sec = dict(list(japanese.items())[6:12])
    western_sec = dict(list(western.items())[6:12])
    cafe_sec = dict(list(cafe.items())[6:12])
    print('22222222222222222222222222222222222222222222222')
    total = dict(list(total.items())[start_idx:end_idx])
    korean = dict(list(korean.items())[start_idx:end_idx])
    chinese = dict(list(chinese.items())[start_idx:end_idx])
    japanese = dict(list(japanese.items())[start_idx:end_idx])
    western = dict(list(western.items())[start_idx:end_idx])
    cafe = dict(list(cafe.items())[start_idx:end_idx])
    print('33333333333333333333333')
    return render_template(
        'home.html',
        totals=total.items(),
        totals_sec=total_sec.items(), 
        koreans=korean.items(),
        koreans_sec=korean_sec.items(),
        chineses=chinese.items(),
        chineses_sec=chinese_sec.items(), 
        japaneses=japanese.items(),
        japaneses_sec=japanese_sec.items(), 
        westerns=western.items(),
        westerns_sec=western_sec.items(),
        cafes=cafe.items(),
        cafes_sec=cafe_sec.items(), 
        tot_count=tot_count,
        kor_count=kor_count,
        chi_count=chi_count,
        jap_count=jap_count,
        wes_count=wes_count,
        caf_count=caf_count,
        gold=gold,
        silver=silver,
        bronze=bronze,
        greview=goldreview,
        sreview=silverreview,
        breview=bronzereview,
        gnum=len(goldreview),
        snum=len(silverreview),
        bnum=len(bronzereview))


#app.py 에서 get_restaurants 호출
@app.route("/list_res")
def list_restaurants():
    page = request.args.get("page", 0, type=int)
    category = request.args.get("category", "total")
    limit = 9

    start_idx=limit*page
    end_idx=limit*(page+1)

    if category=="total":
        data = DB.get_restaurants()
    else:
        data = DB.get_restaurants_byfoodchoice(category)

    res_name=DB.get_restaurantsName()
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

    print(data)

    return render_template(
        "list.html",
        datas=data.items(),
        total=tot_count,
        limit=limit,
        page=page,
        page_count=int((tot_count/9)+1),
        category=category)
                          

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
    page=request.args.get("page", 0, type=int)
    limit=3

    start_idx=limit*page
    end_idx=limit*(page+1)
    data = DB.get_food_byname(str(res_name))
    print("#data###########")
    print(data)
    tot_count = len(data)
    data = dict(list(data.items())[start_idx:end_idx])
    print("#data22############")
    print(data)
    # 레스토랑 이름 전달
    res_name=res_name
    return render_template("menuShow.html", datas=data, total=tot_count, res_name=res_name, limit=limit, page=page, page_count=int((tot_count/3)+1))

# 동적 라우팅 : 메뉴 등록 -> 메뉴조회 화면 이동
@app.route("/menu/<res_name>/")
def menu_result(res_name):
    page=request.args.get("page", 0, type=int)
    limit=3

    start_idx=limit*page
    end_idx=limit*(page+1)
    data = DB.get_food_byname(str(res_name))
    print("#data###########")
    print(data)
    tot_count = len(data)
    data = dict(list(data.items())[start_idx:end_idx])
    print("#data22############")
    print(data)
    # 레스토랑 이름 전달
    res_name=res_name
    return render_template("menuShow.html", datas=data, total=tot_count, res_name=res_name, limit=limit, page=page, page_count=int((tot_count/3)+1))

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

# 동적 라우팅 : 리뷰 등록 -> 리뷰조회 화면 이동
@app.route("/review/<res_name>/")
def review_result(res_name):
    data=DB.get_review_byname(str(res_name))  #맛집 이름으로 리뷰 데이터 가져오는 함수
    avg_rate=DB.get_avgrate_byname(str(res_name))  #맛집 이름으로 평균 평점 가져오는 함수
    review_num=DB.get_reviewnum_byname(str(res_name))
    res_name=res_name
    print("####dataaa:",data)
    return render_template("reviewShow.html",datas=data, avg_rate=avg_rate, review_num=review_num, res_name=res_name)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5001', debug=True, threaded=True)
    
