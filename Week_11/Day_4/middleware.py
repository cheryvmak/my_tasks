# import jwt
# from dotenv import load_dotenv
# import os
# import datetime

# load_dotenv()

# secret_key = os.get_env("secret key")

# def create_token(details, expiry):
#     expiry = datetime.now() + expiry

#     details.update({"exp": expiry})

#     encoded_jwt = jwt.encode(details, secret_key)

#     return encoded_jwt