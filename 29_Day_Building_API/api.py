from flask import Flask, Response, request, render_template
import json
from bson.json_util import dumps
import pymongo
import os
from datetime import datetime

app = Flask(__name__)

#MongoDB
mongodb_uri = 'mongodb+srv://diego:haha123@thirty-days-of-python.ipjn2.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
client = pymongo.MongoClient(mongodb_uri)
db = client['thirty-days-of-python']

@app.route('/api/v1/students/<name>', methods=['GET'])
def check_student (name):
    student = db.students.find({'name':name},{'_id':0, 'name':1, 'country':1, 'city':1, 'DOB':1, 'skills':1, 'bio':1})
    return Response(dumps(student), mimetype='application/json')


@app.route('/api/v1/students', methods = ['POST'])
def create_student ():
    name = request.form['name']
    country = request.form['country']
    city = request.form['city']
    skills = request.form['skills'].split(', ')
    bio = request.form['bio']
    birthyear = request.form['birthyear']
    created_at = datetime.now()
    student = {
        'name': name,
        'country': country,
        'city': city,
        'birthyear': birthyear,
        'skills': skills,
        'bio': bio,
        'created_at': created_at

    }
    db.students.insert_one(student)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

