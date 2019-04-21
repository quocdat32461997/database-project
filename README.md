Dependencies:
  - MySQL-server
      Download from MySQL website
  - mysql.connector 
      pip install mysql
  - faker
    pip install faker
  - names
  
1: Start MySQL Server
    --> mysql.server start
    You runs the server on your computer and add password to mysql.connector in initialize_data.py
2: Execute test.py 
    This file will execute functins stored in generate_data.py and execute insert_command functions stored in insert_data.py
    This fill generates data and insert data into database server
