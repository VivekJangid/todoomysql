from flask import Flask , request
from flaskext.mysql import MySQL

import pymysql

app = Flask(__name__)

mysql = MySQL()

mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'vivek'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'flask'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

#Connect DB
conn = mysql.connect()
db_query = conn.cursor(pymysql.cursors.DictCursor)
db_query.execute("CREATE TABLE IF NOT EXISTS `todo` (id int(3) NOT NULL PRIMARY KEY auto_increment,name VARCHAR(15) , title VARCHAR(25));")

@app.route('/GET')
def get_data():
    db_query.execute("SELECT * FROM todo ;")
    result = db_query.fetchall()
    if result is None:
        return {result},{"Success" : False}, 404
    return {result}

@app.route('/GET/<id>')
def get_dataid():
    db_query.execute(f"SELECT * FROM todo WHERE id = {id};")
    result = db_query.fetch()
    if result is None:
        return "False", 404
    return {result}

@app.route('/POST' , methods = ['POST'])
def post_data():
    name = request.json['name']
    title = request.json['title']
    db_query.execute("INSERT into todo (name,title) values (%s,%s)",(name,title))
    conn.commit()
    return "SUCCESS"

@app.route('/DELETE/<id>' , methods = ['POST'])
def post_dataid():
    db_query.execute(f"DELETE FROM tbl_user WHERE user_id= {id}")
    conn.commit()
    return {"Success" : True}

@app.route('/UPDATE/<id>' , methods = ['POST'])
def post_data():
    name = request.json['name']
    title = request.json['title']
    db_query.execute(f"UPDATE todo SET name='{name}', title='{title}' WHERE user_id={id} ;")
    conn.commit()
    return "SUCCESS"


if __name__ == "__main__":
    app.run()