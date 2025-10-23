# from database import db
# from fastapi import FastAPI,HTTPException
# from pydantic import BaseModel, Field
# from sqlalchemy import text
# import os
# from dotenv import load_dotenv
# import bcrypt
# import uvicorn 


# load_dotenv()

# app = FastAPI(title="Simple App", version="1.0.0")

# class Simple(BaseModel):
#     name: str = Field(..., example="Sam Larry")
#     email: str =  Field(..., example="sam@email.com")
#     password: str = Field(..., example="sam123")

# @app.post("/signup")
# def signup(input:Simple):
#     try:
#         duplicate_query=text("""
#         SELECT * FROM users
#         WHERE email =:email 

#         """)
#         existing = db.execute(duplicate_query, {"email":input.email})
#         if existing:
#             print("Email already exist")
#             #raise HTTPException(status_code = 400, details="email already exists")


#         query = text("""
#             INSERT INTO users (name, email, password)
#             VALUES (:name, :email, :password);
#         """) 

#        #hashing password
#         salt = bcrypt.gensalt()
#         hashedpassword = bcrypt.hashpw(input.password.encode("utf-8"), salt)
#         print(hashedpassword)

#         data = {"name": input.name, "email": input.email, "password": hashedpassword}
#         db.execute(query, data)
#         db.commit()
        
#         return {"Message": "User created succesfully",
#                 "data": {"name": input.name, "email": input.email}}

#     except Exception as e:
#         raise HTTPException(status_code=500, detail = e )

# if __name__=="__main__":
#      uvicorn.run(app,host=os.getenv("host"), port=int(os.getenv("port")))



import bcrypt
from database import db
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import text
import os
from dotenv import load_dotenv
import uvicorn

load_dotenv()

app=FastAPI(title="Simple App", version="1.0.0")

class simple(BaseModel):
    name: str = Field(..., example= "Sherif Oke")
    email: str= Field(..., example= "oke@gmail.com")
    password: str=Field(..., example= "ade121")
    #userType: str = Field(..., exa)


@app.get("/", description="This endpoint just return a welcome message")
def root():
    return {"Message": "Welcome to my FastAPI App"}

@app.post("/signup")
def signUp(input:simple):
    try:
        duplicate_query=text(""" SELECT * FROM users WHERE email=:email """)
        existing=db.execute(duplicate_query,{"email":input.email})
        if existing:
            print("Email already exist")
            # raise HTTPException(status_code=400, detail="Email already exist")
        query= text("""
            INSERT INTO users (name, email, password)
        VALUES(:name, :email, :password);
        """)

        # hashing password
        salt=bcrypt.gensalt()
        hashedpassword=bcrypt.hashpw(input.password.encode('utf-8'), salt)
        print(hashedpassword)

        # mapping data
        data= {"name":input.name, "email":input.email, "password":hashedpassword}
        db.execute(query,data)
        db.commit()
        return {"Message": "User created sucessfuly", "data":{"name":input.name, "email":input.email}}
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)
    

class LoginRequired(BaseModel):
    email: str = Field(..., example="sam@email.com")
    password: str = Field(..., example= "sam123")

@app.post("/login")
def login(input: LoginRequired):
    try:
        query = text("""
         SELECT * FROM users WHERE email = :email            
""")
        result = db.execute(query, {"email": input.email}).fetchone()

        if not result:
            raise HTTPException(status_code=500, detail = "invalid email or password")
        
        verified_password = bcrypt.checkpw(input.password.encode("utf-8"), result.password.encode("utf-8"))

        if not verified_password:
            raise HTTPException(status_code=404, detail =" invalid email or password")
        return {
            "message": "Login Successful"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail = str(e))

    

if __name__=="__main__":
     uvicorn.run(app,host=os.getenv("host"), port=int(os.getenv("port")))