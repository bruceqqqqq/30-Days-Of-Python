from flask import Flask, render_template, request, redirect, url_for, Response
import os
import pymongo
from bson.json_util import dumps
from bson.json_util import ObjectId
from datetime import datetime

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

mongodb_uri = 'mongodb+srv://diego:haha123@thirty-days-of-python.ipjn2.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
client = pymongo.MongoClient(mongodb_uri)
db = client['thirty-days-of-python']

@app.route('/')
def home():
    techs = ['HTML', 'CSS', 'Flask', 'Python']
    name = '30 dias de programação em Python'
    return render_template('home.html', techs = techs, name = name, title = 'Home')


@app.route('/about')
def about():
    name = '30 dias de programação em Python'
    return render_template('about.html', name = name, title = 'About Us')


@app.route('/result')
def result():
    return render_template('result.html', title = 'Result')


@app.route('/feedback-result')
def feedback_result():
    return render_template('feedback-result.html', title ='Feedback Result')


@app.route('/students', methods=['POST', 'GET'])
def students():
    students_list = []
    for s in db.students.find({}):
        s['skills'] =  ', '.join(s['skills'])
        students_list.append(s)
    return render_template('students.html', title='Estudantes', estudantes=students_list)


@app.route('/post', methods=['GET', 'POST'])
def post():
    name = 'Analisador de Texto'
    if request.method == 'GET':
        return render_template('post.html', name = name, title = name)
    if request.method == 'POST':
        content = request.form['content']
        letras = len(content)
        palavras = len(content.split(' '))
        content = content.split()
        maior = 0
        for palavra in content:
            if content.count(palavra) > maior:
                maior = content.count(palavra)
                mais_frequente = palavra
        if content:
            return render_template('result.html', phrase=content, letters=letras, words=palavras, palavra_mais_frequente=mais_frequente, wordsrow=set(content))
        else:
            return render_template('post.html', name=name, title=name, error='O campo abaixo não pode estar vazio!' )


@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    name = 'Feedback'
    if request.method == 'GET':
        return render_template('feedback.html', name = name, title = name)
    if request.method == 'POST':
        content = request.form['content']
        if content:
            db.feedback.insert_one({
              'feedback':content
            })
            total = 0
            for fb in db.feedback.find():
                total += 1
            return render_template('feedback-result.html', total=total)
        else:
            return render_template('feedback.html', name=name, title=name, error='O campo abaixo não pode estar vazio!' )


@app.route('/api', methods=['POST', 'GET'])
def api():
    if request.method == 'GET':
        return render_template('api.html', title='API')
    if request.method == 'POST':
        content = request.form['content'].title()
        if content:
            return check_student(content)
        else:
            return render_template('api.html', title='API', error='O campo abaixo não pode estar vazio!')


@app.route('/api/v1/students/<name>', methods=['GET'])
def check_student (name):
    student = db.students.find({'name':name},{'_id':1, 'name':1, 'country':1, 'city':1, 'DOB':1, 'skills':1, 'bio':1})
    if student.count() > 0:
        return Response(dumps(student), mimetype='application/json')
    else:
        return render_template('api.html', title='API', error='Não há ninguém com este nome.')


@app.route('/students/add', methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        return render_template('create_student.html')
    if request.method == 'POST':
        name = request.form['name']
        country = request.form['country']
        city = request.form['city']
        DOB = request.form['DOB']
        skills = request.form['skills'].split(', ')
        bio = request.form['bio']
        created_at = datetime.now().strftime("%d/%m/%Y %H:%M %p")
        student = {
            'name':name,
            'country':country,
            'city':city,
            'DOB':DOB,
            'skills':skills,
            'bio':bio,
            'created_at':created_at
        }
        db.students.insert_one(student)
        return redirect(url_for('students'))

@app.route('/students/update/<id>', methods=['POST','GET'])
def update_student(id):
    student = db.students.find_one({'_id':ObjectId(id)})
    if request.method == 'GET':
        return render_template('update_student.html',
                               id=student['_id'],
                               name=student['name'],
                               country=student['country'],
                               city=student['city'],
                               DOB=student['DOB'],
                               skills=', '.join(student['skills']),
                               bio=student['bio']
                                )
    if request.method == 'POST':
        query = {'_id':ObjectId(id)}
        name = request.form['name']
        country = request.form['country']
        city = request.form['city']
        DOB = request.form['DOB']
        skills = request.form['skills'].split(', ')
        bio = request.form['bio']
        created_at = datetime.now().strftime("%d/%m/%Y %H:%M %p")
        student = {
            'name': name,
            'country': country,
            'city': city,
            'DOB': DOB,
            'skills': skills,
            'bio': bio,
            'created_at': created_at
        }
        db.students.update_one(query, {'$set':student})
        return redirect(url_for('students'))

@app.route('/students/delete/<id>', methods=['POST', 'DELETE'])
def delete_student(id):
    db.students.delete_one({'_id':ObjectId(id)})
    return redirect(url_for('students'))

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
