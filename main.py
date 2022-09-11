from re import search
from unittest import result
from flask import Flask, render_template, request

from scrap import wework_job, remote_jobs

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/post', methods=['GET','POST'])
def post():
    params = request.form['inputdata']
    params = str(params)
    if params is not None :
        data1 = remote_jobs(params)
        data2 = wework_job(params)
        data = data1 + data2
        return render_template("next.html", data = data )

if __name__ == '__main__':
  app.run('0.0.0.0', port=5000, debug=True)