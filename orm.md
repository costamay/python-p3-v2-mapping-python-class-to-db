<!-- communicating with the database -->
ORM => OBJECT RELATIONAL MAPPING <=> python object => database

turning objects => database records and vice versa

object<= establish database connection => database

<!-- mapping -->

crud => create, read, update, delete

create => CREATE TABLE table_name(columns)
    => INSERT INTO table_name(columns) VALUES()

read => SELECT * FROM table_name

update  => UPDATE table_name SET name ="Pascal" WHERE id = 2
delete => DELETE FORM table_name WHERE ID =1

classes => database tables
Student => students
Employee => employees

class Student:
    def __init__(self, name, age, id = None):
        self.name = name
        self.age = age
        self.id = id

s = Student("Alex", 20)

students
id  name age
1   Alex 20