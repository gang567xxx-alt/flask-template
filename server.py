from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title='My Home Page')

@app.route('/about')
def about():
    title='About Me'
    name='Sanyapong Ngokngam'
    email='gang567xxx@gmail.com'
    phon='062-546-9925'
    return render_template('about.html',
                           title=title,
                           name=name,
                           email=email,
                           phon=phon)

@app.route('/favorite/foods')
def favorite_foods():
    title='Favorite Foods'
    foods = ['ก้อยกะปอม', 'ลาบงัว', 'อ่อมกบ', 'ซี้นหลอด']
    return render_template('fav_foods.html',
                           title=title,
                           foods=foods)

@app.route('/sports')
def sports():
    title='Favorite Sports'
    sports = ['ฟุตบอล', 'บาสเกตบอล', 'วอลเลย์บอล', 'แบดมินตัน']
    return render_template('sports.html',
                           title=title,
                           sports=sports)

@app.route('/greeting/<username>')
def greeting(username):
    title='Greeting Page'
    return render_template('welcome.html',
                           title=title,
                           username=username)