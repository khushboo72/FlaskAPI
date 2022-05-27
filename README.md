# FlaskAPI
---> To Get a record
Accepted Verb: GET
URL: http://127.0.0.1:5000/getrecord  

---> To Insert a record
Accepted Verb: POST
URL: http://127.0.0.1:5000/insertrecord
Sample body to be passed:
{
    "studentname":"Raj",
    "studentcity":"Vapi",
    "studentcontact": 954545443

}

---> To Update a record
Accepted Verb:PUT 
URL: http://127.0.0.1:5000/updaterecord
Sample body to be passed:
{
    "student_id":1,
    "studentname":"Rajesh",
    "studentcity":"Pune",
    "studentcontact": 9023587
}

---> To Delete a record
Accepted Verb: POST
URL: http://127.0.0.1:5000/deleterecord
Sample body to be passed:
{
    "student_id":1 
}
