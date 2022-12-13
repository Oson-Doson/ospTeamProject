from flask import Flask, render_template,request,redirect,url_for
from database import DBhandler
import sys
sys.setrecursionlimit(10**6)
from config import kakaomap_key
import math 


app = Flask(__name__)
DB=DBhandler()

# ====================================================================================================================================

@app.route('/')
def home():
    return redirect(url_for('osondoson_home')) #홈 화면 

@app.route('/list')
def view_list():
    return redirect(url_for('list_restaurants')) #맛집세부 화면

@app.route('/restaurantUpload')
def reg_restaurant():
    return render_template('restaurantUpload.html') #맛집등록 화면

@app.route('/mapSearch')  #맛집지도 화면
def view_map():
    korean=DB.get_restaurants_byfoodchoice(str('한식'))
    chinese=DB.get_restaurants_byfoodchoice(str('중식'))
    japanese=DB.get_restaurants_byfoodchoice(str('일식'))
    western=DB.get_restaurants_byfoodchoice(str('양식'))
    cafe=DB.get_restaurants_byfoodchoice(str('카페'))
    return render_template(
        'mapSearch.html', 
        map_key=kakaomap_key, 
        korean=list(korean.values()), 
        # korean=korean,
        chinese=list(chinese.values()), 
        japanese=list(japanese.values()), 
        western=list(western.values()), 
        cafe=list(cafe.values())
    )  

@app.route('/allergycheck') #알레르기 팝업창 (대표메뉴등록화면)
def allergy_popup():
    return render_template('allergyPopup.html')


@app.route('/reviewUpload') # 추가한 부분 - 리뷰등록 화면
def reviewUpload():
    return render_template("reviewUpload.html")


@app.route('/menuShow') # 추가한 부분 - 대표메뉴조회 화면
def menuShow():
    return render_template("menuShow.html")

# 맛집등록 post ==============================================================================================================

@app.route("/submit_restaurant_post", methods=['POST'])
def reg_restaurant_submit_post():
  
    image_file=request.files["file"]
    image_file.save("static/image/{}".format(image_file.filename))
    data=request.form

    if DB.insert_restaurantUpload(data['Rname'], data, image_file.filename):
        return render_template("result.html", data=data, image_path="static/image/"+image_file.filename)
    else:
        return "Restaurant name already exist!"
                                                                                                        
# 맛집 등록 -> result.html -> 대표 메뉴 등록으로 이동 ===============================================================================
@app.route('/menuUpload', methods=['post'])
def menuUpload():
    Rname=request.form
    return render_template("menuUpload.html",data=Rname)
    
# 대표메뉴등록 post ==================================================================================================================

@app.route("/submit_menu_post", methods=['POST'])
def reg_menu_submit_post():
    image_file = request.files["menuimage"]
    image_file.save("static/menu-image-upload/{}".format(image_file.filename))

    data = request.form
    
    if DB.insert_menuUpload(data['menuname'], data, image_file.filename):
        return redirect(url_for('menu_result', res_name=data['Rname']))
    else:
        return "Menu name already exist!"

# 리뷰 등록 post ======================================================================================================================
@app.route("/submit_review_post", methods=['POST'])
def submit_review_post():

    image_file=request.files["picture-input"]
    image_file.save("static/review-image/{}".format(image_file.filename))
    data = request.form

    if DB.insert_review(data['nickname'], data, image_file.filename):
        return redirect(url_for('review_result',res_name=data['Rname']))

# 홈 화면 라우팅 ======================================================================================================================

@app.route("/osondoson")
def osondoson_home():

    # 맛집 데이터 , 리뷰 데이터 불러오기
    total=DB.get_restaurants()
    review=DB.get_reviews()

    # 맛집을 카테고리 별로 담을 리스트 생성
    korean={}
    chinese={}
    japanese={}
    western={}
    cafe={}

    # 반복문 변수 초기화
    i=0

    # restaurant 테이블에서 가져온 맛집 데이터에 *리뷰 개수* 정보와 *평균 별점* 정보를 추가해주기
    for res in total.items():
        rates=[]
        for re_res in review.items():
            if(res[1]['Rname']==re_res[1]['restaurant_name']):
                rates.append(float(re_res[1]['star']))
        if len(rates)==0:
            res[1]['avg_rate']=0
            res[1]['review_num']=0
        else:
            res[1]['avg_rate']=round(sum(rates)/len(rates), 2)
            res[1]['review_num']=len(rates)
                
    # 맛집의 카테고리 분류
    for res in total.items() :
        res[1]['avg_rate_per']=res[1]['avg_rate']*20
        if(res[1]['foodchoice']=='한식'):
            korean[i]=res[1]
        if(res[1]['foodchoice']=='중식'):
            chinese[i]=res[1]
        if(res[1]['foodchoice']=='일식'):
            japanese[i]=res[1]
        if(res[1]['foodchoice']=='양식'):
            western[i]=res[1]
        if(res[1]['foodchoice']=='카페'):
            cafe[i]=res[1]
        i=i+1
    
    # 카테고리 별 맛집들을 평균 별점을 기준으로 내림차순 정렬하기
    total=dict(sorted(total.items(),key=lambda x: x[1]['avg_rate'], reverse=True))
    korean=dict(sorted(korean.items(),key=lambda x: x[1]['avg_rate'], reverse=True))
    chinese=dict(sorted(chinese.items(),key=lambda x: x[1]['avg_rate'], reverse=True))
    japanese=dict(sorted(japanese.items(),key=lambda x: x[1]['avg_rate'], reverse=True))
    western=dict(sorted(western.items(),key=lambda x: x[1]['avg_rate'], reverse=True))
    cafe=dict(sorted(cafe.items(),key=lambda x: x[1]['avg_rate'], reverse=True))


    # <section 2 리뷰왕 맛집> 에 쓰일 데이터

        # total 맛집을 리뷰 개수 기준으로 내림차순 정렬 후 , a 변수에 담기
    a=sorted(total.items(),key=lambda x: x[1]['review_num'], reverse=True)[0:3]
        # 리뷰 개수가 많은 식당을 세 개 뽑아서 해당 식당의 key 값을 gold, silver, bronze 에 저장
    gold=a[0]
    silver=a[1]
    bronze=a[2]
        # gold, silver, bronze 를 이용하여 세 맛집의 *맛집 이름* 정보를 goldreview, silverreview, bronzereview 에 저장
    goldreview=DB.get_review_byname(gold[1]['Rname'])
    silverreview=DB.get_review_byname(silver[1]['Rname'])
    bronzereview=DB.get_review_byname(bronze[1]['Rname'])

    #페이징을 위한 코드
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

    # <section 1 맛집 카테고리 탭> 에 쓰일 데이터 : 2페이지
    total_sec=dict(list(total.items())[6:12])
    korean_sec = dict(list(korean.items())[6:12])
    chinese_sec = dict(list(chinese.items())[6:12])
    japanese_sec = dict(list(japanese.items())[6:12])
    western_sec = dict(list(western.items())[6:12])
    cafe_sec = dict(list(cafe.items())[6:12])

    # <section 1 맛집 카테고리 탭> 에 쓰일 데이터 : 1페이지
    total = dict(list(total.items())[start_idx:end_idx])
    korean = dict(list(korean.items())[start_idx:end_idx])
    chinese = dict(list(chinese.items())[start_idx:end_idx])
    japanese = dict(list(japanese.items())[start_idx:end_idx])
    western = dict(list(western.items())[start_idx:end_idx])
    cafe = dict(list(cafe.items())[start_idx:end_idx])

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


# 맛집 세부화면 라우팅 ==================================================================================================================
@app.route("/list_res")
def list_restaurants():
    page = request.args.get("page", 0, type=int)
    category = request.args.get("category", "total")
    moodchoice=request.args.get("moodchoice","키워드")
    limit = 9

    start_idx=limit*page
    end_idx=limit*(page+1)

    if category=="total":
        if moodchoice == '키워드' or moodchoice == 'All':
            data = DB.get_restaurants()
        else:
            data = DB.get_restaurants_byOnlymoodchoice(moodchoice)
    else:
        if moodchoice == '키워드' or moodchoice == 'All':
            data = DB.get_restaurants_byfoodchoice(category)
        else:
            data = DB.get_restaurants_bymoodchoice(category, moodchoice)
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
    if tot_count <= limit:
        data = dict(list(data.items())[:tot_count])
    else:
        data = dict(list(data.items())[start_idx:end_idx])
    print(data)
    return render_template(
        "list.html",
        datas=data.items(),
        total=tot_count,
        limit=limit,
        page=page,
        page_count=math.ceil(tot_count/9),
        moodchoice=moodchoice,
        category=category)
                          

# 동적 라우팅 : 맛집 리스트 화면 -> 맛집 세부화면 ============================================================================
@app.route("/view_detail/<name>/")
def view_restaurant_detail(name):
    data=DB.get_restaurant_byname(str(name))  #맛집 이름으로 데이터 가져오는 함수
    avg_rate=DB.get_avgrate_byname(str(name))  #맛집 이름으로 평균 평점 가져오는 함수
    review_num=DB.get_reviewnum_byname(str(name))
    return render_template("details.html",data=data,avg_rate=avg_rate,review_num=review_num)

# 동적 라우팅 : 맛집 세부화면 -> 맛집 리뷰등록 화면 ==============================================================================
@app.route("/review_post/<name>/")
def review_post(name):
    return render_template("reviewUpload.html",data=name)

# 동적 라우팅 : 맛집 세부화면 -> 대표메뉴조회 화면 =======================================================================================
@app.route("/show_menu/<res_name>/", methods=['POST', 'GET'])
def view_foods(res_name):
    page=request.args.get("page", 0, type=int)
    limit=3
    start_idx=limit*page
    end_idx=limit*(page+1)
    data = DB.get_food_byname(str(res_name))
    tot_count = len(data)
    data = dict(list(data.items())[start_idx:end_idx])
    # 레스토랑 이름 전달
    res_name=res_name

    return render_template("menuShow.html", datas=data.items(), total=tot_count, res_name=res_name, limit=limit, page=page, page_count=int((tot_count/3)))

# 동적 라우팅 : 메뉴 등록 -> 대표메뉴조회 화면 ============================================================================================
@app.route("/menu/<res_name>/")
def menu_result(res_name):
    page=request.args.get("page", 0, type=int)
    limit=3
    start_idx=limit*page
    end_idx=limit*(page+1)
    data = DB.get_food_byname(str(res_name))
    tot_count = len(data)
    data = dict(list(data.items())[start_idx:end_idx])
    # 레스토랑 이름 전달
    res_name=res_name

    return render_template("menuShow.html", datas=data.items(), total=tot_count, res_name=res_name, limit=limit, page=page, page_count=int((tot_count/3)))

# 동적 라우팅 : 맛집 세부화면 -> 맛집 메뉴등록 화면 ====================================================================================
@app.route("/menu_post/<name>/")
def menu_post(name):
    return render_template("menuUpload copy.html",data=name)



# 동적 라우팅 : 맛집 세부화면 -> 맛집 리뷰조회 화면 ====================================================================================
@app.route("/review_show/<res_name>/", methods=['POST'])
def review_show(res_name):
    data=DB.get_review_byname(str(res_name))  #맛집 이름으로 리뷰 데이터 가져오는 함수
    avg_rate=DB.get_avgrate_byname(str(res_name))  #맛집 이름으로 평균 평점 가져오는 함수
    review_num=DB.get_reviewnum_byname(str(res_name))
    res_name=res_name
    return render_template("reviewShow.html",datas=data, avg_rate=avg_rate, review_num=review_num, res_name=res_name)

# 동적 라우팅 : 리뷰 등록 -> 맛집 리뷰조회 화면 이동 =======================================================================================
@app.route("/review/<res_name>/")
def review_result(res_name):
    data=DB.get_review_byname(str(res_name))  #맛집 이름으로 리뷰 데이터 가져오는 함수
    avg_rate=DB.get_avgrate_byname(str(res_name))  #맛집 이름으로 평균 평점 가져오는 함수
    review_num=DB.get_reviewnum_byname(str(res_name))
    res_name=res_name
    return render_template("reviewShow.html",datas=data, avg_rate=avg_rate, review_num=review_num, res_name=res_name)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5001', debug=True, threaded=True)
    
