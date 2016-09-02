from flask import Flask, request
from flask.ext.sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)
db.create_all()

class StuJoinInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.name

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/joinus', methods=['POST'])
def join_us():
    name = request.form['name']
    college = request.form['college']
    stuId = request.form['stuId']
    tel = request.form['tel']
    qq = request.form['qq']
    mail = request.form['mail']
    interests = request.form['interests']
    print request.form['name']
    print request.form['college']
    print request.form['stuId']
    print request.form['tel']
    print request.form['qq']
    print request.form['mail']
    print request.form['interests']
    stu_join_info = StuJoinInfo(name, college, stuId, tel, qq, mail, interests)
    db.session.add(stu_join_info)
    db.session.commit()
    return 'welcome'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)