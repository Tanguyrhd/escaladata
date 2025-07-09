from fastapi import FastAPI
from supabase import create_client, Client
import os

app = FastAPI()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(url, key)

@app.get('/')
def root():
    return {'Hello': 'escaladata is building up'}

@app.get("/data")
def get_data():
    response = supabase.table("master").select("*").execute()
    return response.data

# with open("../models/logistic_reg.pkl", "rb") as f:
#     model = pickle.load(f)

# with open("../models/vectorizer.pkl", "rb") as f:
#     vectorizer = pickle.load(f)

# @app.get('/predict')
# def predict(
#     tweet='fill in your tweets'
# ):
#     X_input=vectorizer.transform([tweet])

#     pred=model.predict(X_input)[0]

#     return {'MBTI personality result': str(pred)}


# then run to test LOCALLY
# uvicorn vibe_api:app --reload
