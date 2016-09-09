from flask import Flask, request
from flask.ext.sqlalchemy import SQLAlchemy
import os


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)


class StuJoinInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    college = db.Column(db.String(80))
    stuId = db.Column(db.String(30), unique=True)
    tel = db.Column(db.Integer(), unique=True)
    qq = db.Column(db.Integer(), unique=True)
    mail = db.Column(db.String(40), unique=True)
    interests = db.Column(db.Text)

    def __init__(self, name, college, stuId, tel, qq, mail, interests):
        self.name = name
        self.college = college
        self.stuId = stuId
        self.tel = tel
        self.qq = qq
        self.mail = mail
        self.interests = interests

    def __repr__(self):
        return '<User %r>' % self.name

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/post-test', methods=['POST'])
def post_test():
    name = request.form['name']
    password = request.form['password']
    print name
    print password
    return 'welcome'

@app.route('/join-us', methods=['POST'])
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

db.drop_all()
db.create_all()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
