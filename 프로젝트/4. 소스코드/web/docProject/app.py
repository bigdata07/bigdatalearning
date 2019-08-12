from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///doctor.sqlite" # 설정 파일을 flask에서 만듬.
db = SQLAlchemy(app) # app을 첫번째 인자로 넣어버림.

# 이 객체를 만든다는건 ORM을 사용한다는 의미

@app.route('/search')
def searchpage():
    outcome = request.args.get('search')
    # print(request.form.get('search'))
    return render_template('search.html')

@app.route('/')
def homepage():
    return render_template('main.html')

@app.route('/test')
def nextpage():
    return render_template('test.html')


@app.route('/matching2')
def matchingpage2():
    return render_template("matching2.html")

@app.route('/matching')
def matchingpage():
    doctorlist = [
        {
            'name' : '강동호',
            'hospital' : '가고싶은치과의원',
            'specialist' : True,
            'recognition' : True
        },
        {
            'name' : '이상용',
            'hospital' : '잎사귀치과병원',
            'specialist' : False,
            'recognition': True
        },
        {
            'name' : '김수광',
            'hospital' : '이미지치과의원',
            'specialist' : True,
            'recognition': False
        },
        {
            'name': '신상우',
            'hospital': '종로치과의원',
            'specialist': True,
            'recognition': False
        }
    ]
    return render_template('matching.html', doctorlist = doctorlist)



if __name__ == '__main__':
    app.run()
