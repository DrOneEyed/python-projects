import mysql.connector
connection= {
          'user': 'root',
      'password': 'rootlap',
      'host': '127.0.0.1',
      'database': 'project'}
cursor = connection.cursor(prepared=True)
sql_insert_query = """ INSERT INTO `python_users`(`id`, `name`, `birth_date`, `age`) VALUES (%s,%s,%s,%s)"""
insert_tuple = (userId, userName, joinDate, age)
result  = cursor.execute(sql_insert_query, insert_tuple)
connection.commit()
print ("Record inserted successfully into python_users table")
