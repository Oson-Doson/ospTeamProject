from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def food():
    return render_template("restaurantUpload.html")

@app.route("/submit_restaurant_post",methods=['POST'])
def reg_restaurant_submit_post():

    data=request.form
    return render_template("result.html",data=data)


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
