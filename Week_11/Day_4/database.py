from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from pymysql.constants import CLIENT
import os 

load_dotenv()

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from pymysql.constants import CLIENT
import os

# Build DB URL from environment variables
db_url = f'mysql+pymysql://{os.getenv("dbuser")}:{os.getenv("dbpassword")}@{os.getenv("dbhost")}:{os.getenv("dbport")}/{os.getenv("dbname")}'

# Create engine with support for multiple statements
engine = create_engine(db_url, connect_args={"client_flag": CLIENT.MULTI_STATEMENTS})

# Create session
Session = sessionmaker(bind=engine)
db = Session()

# Define all create table queries
create_table_query = text("""
CREATE TABLE IF NOT EXISTS user (
    userid INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);
"""),


create_table_query = text("""
CREATE TABLE IF NOT EXISTS courses (
    courseid INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    level VARCHAR(100) NOT NULL
);
"""),

create_table_query = text("""
CREATE TABLE IF NOT EXISTS enrollments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    userid INT,
    courseid INT,
    FOREIGN KEY (userid) REFERENCES user(userid),
    FOREIGN KEY (courseid) REFERENCES courses(courseid)
);
""")

db.execute(create_table_query)
print("Tables have been created successfully.")


# from sqlalchemy import create_engine, text
# from sqlalchemy.orm import sessionmaker
# from dotenv import load_dotenv
# from pymysql.constants import CLIENT
# import os

# load_dotenv()

# db_url = f'mysql+pymysql://{os.getenv("dbuser")}:{os.getenv("dbpassword")}@{os.getenv("dbhost")}:{os.getenv("dbport")}/{os.getenv("dbname")}'

# engine = create_engine(db_url, connect_args={"client_flag": CLIENT.MULTI_STATEMENTS})
# Session = sessionmaker(bind=engine)
# db = Session()

# queries = [
#     text("""
#         CREATE TABLE IF NOT EXISTS users (
#             userid INT AUTO_INCREMENT PRIMARY KEY,
#             name VARCHAR(255) NOT NULL,
#             email VARCHAR(255) NOT NULL,
#             password VARCHAR(255) NOT NULL
#         );
#     """),
#     text("""
#         CREATE TABLE IF NOT EXISTS courses (
#             courseid INT AUTO_INCREMENT PRIMARY KEY,
#             title VARCHAR(100) NOT NULL,
#             level VARCHAR(100) NOT NULL
#         );
#     """),
#     text("""
#         CREATE TABLE IF NOT EXISTS enrollments (
#             id INT AUTO_INCREMENT PRIMARY KEY,
#             userid INT,
#             courseid INT,
#             FOREIGN KEY (userid) REFERENCES users(userid),
#             FOREIGN KEY (courseid) REFERENCES courses(courseid)
#         );
#     """)
# ]

# for query in queries:
#     db.execute(query)

# db.commit()
# print("Tables created successfully!")





#b_url = dialect+driver://dbuser;dbpassword;dbhost;dbport;dbname

#db_url =f'mysql+pymysql://{os.getenv("dbuser")}:{os.getenv("dbpassword")}:{os.getenv("dbhost")}:{os.getenv("dbport")}:{os.getenv("dbname")}'
# db_url = f'mysql+pymysql://{os.getenv("dbuser")}:{os.getenv("dbpassword")}@{os.getenv("dbhost")}:{os.getenv("dbport")}/{os.getenv("dbname")}'


# # engine = create_engine(db_url)
# engine = create_engine(
#     db_url,
#     connect_args={"client_flag": CLIENT.MULTI_STATEMENTS}
# )

# session = sessionmaker(bind=engine)

# db = session()

# # # query = text("select * from user")

# # user = db.execute(query).fetchall()
# # print(user)

# create_table_query = text("""
# CREATE TABLE IF NOT EXISTS user(
#  userid int auto_increment primary key,
#  name varchar(255) not null,
#  email varchar(255) not null,
#  password varchar(255) not null);
# """)

# create_table_query = text("""
# CREATE TABLE IF NOT EXISTS courses(
#  courseid int auto_increment primary key,
#  title varchar(100) not null,
#  level varchar(100) not null );
# """)

# create_table_query = text("""
# CREATE TABLE IF NOT EXISTS enrollments(
#  id int auto_increment primary key,
#  userid int,
#  courseid int,
#  FOREIGN KEY (userid) REFERENCES user(id), 
#  FOREIGN KEY (courseid) REFERENCES courses(id);    
# """)

# db.execute(create_table_query)
# print("Table have created succesfully")

# create table user (
# id int auto_increment primary key,
# name varchar(255) not null,
# email varchar(255) not null,
# password varchar(255) not null);

# insert into user
# values(1, "Sam Larry", "sam@gmail.com", "sam123"),
# (2, "Sam Ayomide", "Ayomide@gmail.com", "ayo123");

# select * from user;


# create_table_query = text('''
# CREATE TABLE IF NOT EXISTS user(
#  userid int auto_increment primary key,
#  name varchar(255) not null,
#  email varchar(255) not null,
#  password varchar(255) not null);

# ''')

# db.execute(create_table_query)
# print("Table have created succesfully")