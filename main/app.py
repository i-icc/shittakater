# -*- coding: utf-8 -*-
from flask import Flask, render_template, redirect, request, url_for
from main import Shittakater

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')    

@app.route('/result')
def result(shittakater = Shittakater()):
    try:
        if not shittakater.is_ok: return render_template('/error.html',status=shittakater.result["status"], word=shittakater.result["word"])
        tweets = []
        for _ in range(3):
            shittakater.make()
            tweets.append(shittakater.result["result2"])
            tweets.append(shittakater.result["result"])
        return render_template('result.html',result=shittakater.result,tweets=tweets)
    except Exception as e:
        # return "ok"+str(e)
        return render_template('/error.html',status=shittakater.result["status"], word=shittakater.result["word"])

@app.route('/search', methods=['POST'])
def search():
    try:
        word = request.form["word"]
        shittakater = Shittakater()
        shittakater.lean(word)
        return result(shittakater)
    except Exception as e:
        # return "sea"+str(e)
        return render_template('/error.html',status=shittakater.result["status"], word=shittakater.result["word"])

if __name__ == '__main__':
    # app.run()
    app.run(host='0.0.0.0', port=5000, debug=True)
