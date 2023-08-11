from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///users.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)


@app.route("/")
def hello_world():
    return render_template("index.html",name="yathish")

@app.route("/oddoreven")
def hello_oddoreven():
    return render_template("oddoreven.html",num=8)

@app.route("/data",methods=['GET','POST'])
def hello_data():
    
    try:
        user_input=request.form['user_input']
        print(user_input)
    except Exception as e:
        print(e)
        user_input=""
    return render_template("form.html",user_input1=user_input)


@app.route("/database",methods=['GET','POST'])
def hello_database():
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect('/')
    return render_template('database.html')
   
if __name__=="__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)


