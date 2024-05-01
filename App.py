from flask import Flask, render_template, request, send_from_directory
import pymysql as sql


def sql_connect():
    conn = sql.connect(
        host="localhost",
        user="root",
        password="indra@123",
        database="demo1"
    )
    c = conn.cursor()
    return conn, c
app = Flask(__name__, template_folder='template')


@app.route('/')
def nav():
    return render_template('nav.html')
@app.route('/menu')
def men():
    return render_template('menu.html')
@app.route('/signup')
def signup():
    return render_template('signup.html')
@app.route('/login')
def lo():
    return render_template('login.html')
@app.route('/homme')
def homm():
    return render_template('homme.html')
@app.route('/table')
def res():
    return render_template('table.html')
@app.route('/signup', methods=['POST'])
def de():
    if request.method == 'POST' :
        username = request.form['username']
        password = request.form['password']
        print(username,password)
        conn, c = sql_connect()
        c.execute("INSERT INTO pbl1(username,password) VALUES (%s,%s)",(username, password))
        conn.commit()
        return render_template('home.html')
@app.route('/table', methods=['POST'])
def re():
    if request.method == 'POST' :
        customername = request.form['customername']
        tableno = request.form['tableno']
        print(customername,tableno)
        conn, c = sql_connect()
        c.execute("INSERT INTO reserve(customername,tableno) VALUES (%s,%s)",(customername, tableno))
        conn.commit()
        return render_template('reee.html')
@app.route('/login',methods=['POST'])
def lv():
    if request.method=="POST":
        username=request.form['username']
        password=request.form['password']
        conn,c=sql_connect()
        if c.execute("SELECT * FROM pbl1 WHERE username=%s and password=%s",(username,password)):
            conn.commit()
            return render_template("homme.html")
        else:
            return render_template("nav.html")
@app.route('/images/<path:images>')
def serve_image(images):
    return send_from_directory("images", images)
if __name__ == '__main__':
    app.run(debug=True)