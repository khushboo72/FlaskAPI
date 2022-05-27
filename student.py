from dbhelper import get_sql_connection

def get_record(connection):
    cursor = connection.cursor()
    query = ("SELECT * FROM studentdata")
    cursor.execute(query)
    response = []
    for (student_id,studentname,studentcity ,studentcontact) in cursor:
        response.append({'student_id': student_id,
                        'studentname': studentname,
                         'studentcity': studentcity,
                         'studentcontact': studentcontact,
                         })
    return response

def insert_record(connection,students):
    cursor = connection.cursor()
    query = ("INSERT INTO studentdata(studentname,studentcity ,studentcontact) VALUES (%s,%s,%s)")
    data = ( students['studentname'],students['studentcity'],students['studentcontact'])
    cursor.execute(query, data)
    connection.commit()
   
    
def delete_record(connection, student_id):
    cursor = connection.cursor()
    query = ("DELETE FROM studentdata WHERE student_id= " + str(student_id))
    cursor.execute(query)
    connection.commit()

    
   
def update_record(connection, students):
    cursor = connection.cursor()
    query = (("UPDATE studentdata SET studentname=%s, studentcity=%s, studentcontact=%s" " WHERE student_id=%s"))
    data = (students['studentname'],students['studentcity'],students['studentcontact'],students['student_id'])                             
    cursor.execute(query,data)
    connection.commit()
    

if __name__ == '__main__':
    connection = get_sql_connection()
    
