from flask import Flask, render_template,request
from flask_mysqldb import MySQL
import yaml
app = Flask(__name__)

db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql=MySQL(app) 



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        loginDetails = request.form
        username = loginDetails['username']
        password = loginDetails['password']
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO login(username,password) VALUES(%s,%s)",(username,password))
        mysql.connection.commit()
        cur.close()
       
    return render_template('login.html')


@app.route('/data',methods=['GET','POST'])
def data():
    if request.method=='POST':
        dataDetails = request.form
        DOOR_NUMBER = dataDetails['DOOR_NUMBER']
        NAME = dataDetails['NAME']
        AGE = dataDetails['AGE']
        BLOOD = dataDetails['BLOOD']
        CSTATUS = dataDetails['CSTATUS']
        SYMPTOMS = dataDetails['SYMPTOMS']
        VACCINATED = dataDetails['VACCINATED']
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO data(DOOR_NUMBER,NAME,AGE,BLOOD,CSTATUS,SYMPTOMS,VACCINATED) VALUES(%s,%s,%s,%s,%s,%s,%s)",(DOOR_NUMBER,NAME,AGE,BLOOD,CSTATUS,SYMPTOMS,VACCINATED))
        mysql.connection.commit()
        cur.close()
        
        
    return render_template('data.html') 

@app.route('/precaution')
def precaution():
    return render_template('precaution.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')




if __name__=='__main__':
    app.run(debug=True)