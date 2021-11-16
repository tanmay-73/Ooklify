from flask import Flask
from flask import jsonify
import speedtest

app = Flask(__name__)
@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return jsonify({'name':'Jimit','address':'India'})
@app.route('/ookla/', methods=['GET', 'POST'])
def shell():
    s = speedtest.Speedtest()
    s.get_best_server()
    s.download()
    s.upload()
    s.results.share()
    return jsonify(s.results.dict())
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1005)