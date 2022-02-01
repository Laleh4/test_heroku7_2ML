# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 09:43:41 2022

@author: laleh
"""

from fastapi import FastAPI
import uvicorn
import pickle
#from BankNotes import BankNote
#from models import Women



app=FastAPI()

import pathlib



TT=pathlib.Path("__file__").parent.resolve()
path_L=str(TT).replace("\\","/") 

P=pathlib.PureWindowsPath(path_L)

path_L=str(P.parents[0])

with open('Model_LR2.pkl', 'rb') as f:
       Model_LR2 = pickle.load(f)
       
"""        
f=open(path_L+"/Model_LR2.pkl","rb")
model=pickle.load(f)
f.close()
"""
@app.get("/")
def greet():
    return {"Hello World!"}
"""
@app.get("/{name}")
def hello(name:str):
    return {'message': f'Hello,{name}'}




@app.post("/predict")
def predict(req: BankNote):
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
    
""" 
    
    
    
#if __name__ == '__main__':

#    #uvicorn.run(app, host='127.0.0.1', port=8000, debug=True)  # local
#    uvicorn.run(app, host='0.0.0.0', port=5000, debug=True)
