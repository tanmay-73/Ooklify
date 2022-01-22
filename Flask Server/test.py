from flask import Flask
from flask import jsonify
import speedtest

app = Flask(__name__)
@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return jsonify({'name':'Admin','address':'10.20.21.1'})
@app.route('/ookla/', methods=['GET', 'POST'])
def shell():
    s = speedtest.Speedtest()
    s.get_best_server()
    #s.download()
    #s.upload()     
    #s.ping()    
   # down=int(s.results.download)/1000000
   # up=int(s.results.upload)/1000000
   # ping=int(s.results.ping)
    return jsonify({'download':int(s.download())/1000000,'upload':int(s.upload())/1000000,'ping':s.results.ping})
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10500)
