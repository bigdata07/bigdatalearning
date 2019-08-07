from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('test.html')

@app.route('/')
def mainpage():
    return 'Hello World!'

@app.route('/')
def searchpage():
    return 'Hello World!'

@app.route('/')
def matchingpage():
    return 'Hello World!'

@app.route('/')
def analysispage():
    return 'Hello World!'




if __name__ == '__main__':
    app.run()
