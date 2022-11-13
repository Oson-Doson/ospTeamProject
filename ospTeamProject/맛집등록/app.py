from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def food():
    return render_template("restaurantUpload.html")

@app.route("/submit_restaurant_post",methods=['POST'])
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

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
