#This is the main file and this should be executed to access the API 

from flask import Flask, jsonify, request
from dbhelper import *
import student 

app = Flask(__name__)

connection = get_sql_connection()
@app.before_request 
def before_request_callback(): 
    create_table(connection)

#to display all records
@app.route('/getrecord')
def getrecord():
    student1 = student.get_record(connection)
    response=jsonify(student1)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

#to insert a new record
@app.route('/insertrecord',methods=['POST'])
def insertrecord():
    student_id=student.insert_record(connection,request.json)
    response=jsonify({
        'student_id': student_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

#to delete a record
@app.route('/deleterecord', methods=['POST'])
def deleterecord():
    return_id = student.delete_record(connection,request.json['student_id'])
    response = jsonify({
        'student_id': return_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

#to update an existing record
@app.route('/updaterecord', methods=['PUT'])
def updaterecord():
    student_id = student.update_record(connection,request.json)
    response = jsonify({
        'student_id': student_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    app.run(debug=True,port=5000)
