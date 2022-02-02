# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 09:43:41 2022

@author: laleh
"""

from fastapi import FastAPI
import uvicorn
import pickle
from BankNotes import BankNote



app=FastAPI()




model=pickle.load(open('Model_LR2.pkl', 'rb'))



@app.get("/")
def greet():
    return {"Hello World!"}

#@app.get("/{name}")
#def hello(name:str):
#    return {'message': f'Hello,{name}'}
"""
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str
    price: float
    tax: str

@app.post("/items/")
def create_item(item: Item):
    return item
"""

@app.post("/predict")
def predictx(req: BankNote):
    return {'message': req}

    preg=req.pregnacies
    glucose=req.glucose
    bp=req.bp
    skinthickness=req.skinthickness
    insulin=req.insulin
    bmi=req.bmi
    dpf=req.dpf
    age=req.age
    features=list([preg,glucose,bp,skinthickness, insulin,bmi,dpf,age])
    
    predict=model.predict([features])
    probab=model.predict_proba([features])
    if (predict==1):
        return {"ans":"You have benn tested positive with {} probability".format(probab[0][1])}
    else:
        return {"ans":"You have benn tested negative with {} probability".format(probab[0][0])}
    
    

    
    
    

