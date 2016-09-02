from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'
#
# @app.route('/joinus', methods=['POST'])
# def join_us():
#

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)