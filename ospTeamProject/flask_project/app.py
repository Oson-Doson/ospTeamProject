from flask import Flask, render_template
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
    
if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5001', debug=True)