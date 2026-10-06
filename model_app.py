from fastapi import FastAPI
from fastapi.responses import JSONResponse
from model.predict import model_predict,model,MODEL_VERSION
from schema.user_input import userInput



app=FastAPI()


# human redable 
@app.get('/')
def home():
    return {'message':'Insurance Premium Prediction API'}

#machine redable
@app.get('/health')
def health():
    return {
        'status':200,
        'version':MODEL_VERSION,
        'model loaded':model is not None
    }


@app.post('/predict')
def predict(data:userInput):

    user_input={
        "bmi":data.bmi,
        "age_group":data.age_group,
        "lifestyle_risk":data.lifestyle_risk,
        "city_tier":data.city_tier,
        "income_lpa":data.income_lpa,
        "occupation":data.occupation
    }

    try:
        prediction=model_predict(user_input)
        
        return JSONResponse(status_code=200,content={'predicted_category':prediction})
    
    except Exception as e:
        return JSONResponse(status_code=500,content=str(e))
