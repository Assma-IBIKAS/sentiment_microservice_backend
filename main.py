from fastapi import FastAPI, Header, HTTPException, Depends
from pydantic import BaseModel
from jose import jwt
from dotenv import load_dotenv
import os
from Hugging_face import query


load_dotenv()

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")

payload = {}

class user_schema(BaseModel):
    user_name : str
    password : str

data = {
    "user_name" : "Assma",
    "password" : "@Assma@"
}

app = FastAPI(title="Sentiment Microservice - Auth")

@app.get("/")
def test():
    return "Hello to Sentiment Microservice !!"

@app.post("/login")
def login(info:user_schema):
    if info.user_name  == data["user_name"] and info.password == data["password"]:
        token = jwt.encode(payload,key=JWT_SECRET_KEY,algorithm=JWT_ALGORITHM)
        return token   # ghaygenerer lik wahd code secret o savih f wahd l fichier
    else : 
        return 'Something Wrong !!!'

@app.get("/test_token")
def verify_token(token: str = Header(...)):
    # return token
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        return 'Token Valide'
    except:
        raise HTTPException(status_code = 401,detail = "Something Wrong !!!")

# def verify_token(token):
#     try:
#        token_new = jwt.decode(token = token,key=JWT_SECRET_KEY,algorithm=JWT_ALGORITHM)
#     except :
#         raise HTTPException(status_code=401, detail="Something Wrong !!!")
#     return token_new
 
# class PredictSchema(BaseModel):
#   text: str
# token:str = Depends(verify_token)
@app.post("/predict")
def predict(text: str, token:str = Depends(verify_token) ):

        predict = query({
            "inputs": text,
        })

        label = predict[0][0]["label"]
        score = predict[0][0]["score"]
        score_int = int(label.split()[0]) 
        if score_int <= 2:
            sentiment = "negatif"
        elif score_int == 3:
            sentiment = "neutre"
        else:
            sentiment = "positif"
        return {"score": score_int, "sentiment":sentiment} 
    