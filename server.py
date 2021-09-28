# -*- mode: python; coding: utf-8 -*-

from flask import Flask, jsonify, render_template

PORT=8082

app = Flask(__name__,
            static_folder='./static',
            static_url_path='',
            template_folder='./templates')
app.config["JSON_AS_ASCII"] = False


@app.route('/')
def index():
    appname = '初めてのVue'
    title = '初めてのFlaskアプリケーション'
    return render_template('index.html',
                           appname=appname,
                           title=title)


@app.route('/hello')
def hello():
    title = 'Hello World'
    return render_template('hello.html',
                           title=title)


@app.route('/app-2')
def app_2():
    title = 'app-2'
    return render_template('app-2.html',
                           title=title)


@app.route('/app-3')
def app_3():
    title = 'app-3'
    return render_template('app-3.html',
                           title=title)

@app.route('/app-4')
def app_4():
    title = 'app-4'
    return render_template('app-4.html',
                           title=title)

@app.route('/app-5')
def app_5():
    title = 'app-5'
    return render_template('app-5.html',
                           title=title)

@app.route('/app-6')
def app_6():
    title = 'app-6'
    msg = 'Change me.'
    return render_template('app-6.html',
                           title=title,
                           msg=msg)

@app.route('/app-7')
def app_7():
    title = 'app-7'
    return render_template('app-7.html',
                           title=title)


@app.route('/app-8')
def app_8():
    title = 'app-8'
    return render_template('app-8.html',
                           title=title)


@app.route('/comp-1')
def comp_1():
    title = 'component 1'
    return render_template('comp-1.html',
                           title=title)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=True)
