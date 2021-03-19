from flask import Flask
import os
import pymongo

mongodb_uri = 'mongodb+srv://diego:epHV0dlGnEeFytsW@thirty-days-of-python.ipjn2.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
client = pymongo.MongoClient(mongodb_uri)
database = client['thirty-days-of-python']

"""Criando collection students: Inside of TDOP will be create collection with name students with first document"""
# database.students.insert_one({
#     '_id': 1,
#     'name':'Diego',
#     'country':'Brasil',
#     'age':24,
#     'skills': ['Helpdesk', 'Python', 'Gaming']
# })

"""Inserting many values with for OBS: Can be used insert_many"""
# students = [
#     {'_id': 2, 'name': 'David', 'country': 'UK', 'age': 34, 'skills': ['JavaScript', 'HTML', 'CSS']},
#     {'_id': 3,'name': 'John', 'country': 'Sweden',  'age': 28, 'skills': ['Python', 'MongoDB', 'Flask']},
#     {'_id': 4,'name': 'Sami', 'country': 'Finland', 'age': 25, 'skills': ['Java', 'C+', 'C#' ]}
# ]
#
# for student in students:
#     database.students.insert_one(student)

"""Method find/find_one OBS: Looks like a SELECT"""
first_student = database.students.find_one()
student_from_uk = database.students.find_one({'country':'UK'})
students_with_python = database.students.find({'skills':'Python'}) # if you need to check value in array just insert a normal dict
show_all = database.students.find()
show_only_name_and_skills = database.students.find({}, {'_id':0, 'name': 1, 'skills': 1}) # if you dont put 0 in _id he will show anyways

"""Find with Query"""
query = {"age":{"$gt":25}} # $gt means only above 25
above_25 = database.students.find(query)
query = {"skills":"Python"}
python_users = database.students.find(query)

"""Find with Limit"""
only_three = database.students.find().limit(3) # show the first 3 documments

"""Find with Sort"""
sorted_name = database.students.find().sort('name')
reversed_sorted_name = database.students.find().sort('name',-1)
sorted_age = database.students.find().sort('age')
reversed_sorted_age = database.students.find().sort('age',-1)

"""Update documment with query"""
query = {'age':34}
new_value = {'$set':{'age':999}}
database.students.update_one(query, new_value) # update age with 34 to 999
database.students.update_many({}, {'$pull': {'skills':'Logic'}}) # remove all logic from skills
database.students.update_many({}, {'$push': {'skills':'Logic'}}) # insert in all documments, in skills value logic

"""Delete from db"""

query = {'name':'Sami'}
database.students.delete_one(query) # delete_many({}) will delete all documents from collection


"""Drop a collection""" # delete a collection
database.students.drop()

for student in database.students.find():
    print(student) # not showing because we drop :)
