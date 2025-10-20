from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os 

load_dotenv()


#b_url = dialect+driver://dbuser;dbpassword;dbhost;dbport;dbname

#db_url =f'mysql+pymysql://{os.getenv("dbuser")}:{os.getenv("dbpassword")}:{os.getenv("dbhost")}:{os.getenv("dbport")}:{os.getenv("dbname")}'
db_url = f'mysql+pymysql://{os.getenv("dbuser")}:{os.getenv("dbpassword")}@{os.getenv("dbhost")}:{os.getenv("dbport")}/{os.getenv("dbname")}'


engine = create_engine(db_url)

session = sessionmaker(bind=engine)

db = session()

query = text("select * from user")

user = db.execute(query).fetchall()
print(user)


# create table user (
# id int auto_increment primary key,
# name varchar(255) not null,
# email varchar(255) not null,
# password varchar(255) not null);

# insert into user
# values(1, "Sam Larry", "sam@gmail.com", "sam123"),
# (2, "Sam Ayomide", "Ayomide@gmail.com", "ayo123");

# select * from user;



# from sqlalchemy import create_engine, text
# from sqlalchemy.orm import sessionmaker, declarative_base
# from sqlalchemy.exc import SQLAlchemyError
# from dotenv import load_dotenv
# import os
# load_dotenv()
# #db url= dialect+driver://duser;dbpassword;dbhost;dbport;dbname
# db_url=f"mysql+pymysql://{os.getenv("dbuser")}:{os.getenv("dbpassword")}@{os.getenv("dbhost")}:{os.getenv("dbport")}/{os.getenv("dbname")}"
# engine = create_engine(db_url)
# session = sessionmaker(bind=engine)
# db = session()
# query = text("SELECT * FROM user")
# users = db.execute(query).fetchall()
# print(users)