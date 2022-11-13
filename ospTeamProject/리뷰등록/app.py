from flask import Flask, render_template, request
app=Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello'

@app.route("/submit_review_post", methods=['POST'])
def submit_review_post():

    image_file=request.files["image_uploads"]
    image_file.save("static/image/{}".format(image_file.filename))
    data = request.form
    
     