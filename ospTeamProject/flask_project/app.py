from flask import Flask, render_template,request
app = Flask(__name__)


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

# 아래는 가은언니꺼에서 따온 거   

@app.route("/submit_restaurant_post", methods=['POST'])
def reg_restaurant_submit_post():
    data=request.form
    return render_template("result.html",data=data)

@app.route('/menu_upload')
def menuUpload():
    return render_template("menuUpload.html")

@app.route("/submit_menu_post", methods = ['POST'])
def reg_menu_submit_post():
    image_file=request.files["file"]
    image_file.save("static/image/{}".format(image_file.filename))
    data=request.form
    return render_template("", data=data)
    

# 아래는 여진언니 꺼에서...

@app.route("/submit_review_post", methods=['POST'])
def submit_review_post():

    image_file=request.files["image_uploads"]
    image_file.save("static/image/{}".format(image_file.filename))
    data = request.form

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5001', debug=True)
    