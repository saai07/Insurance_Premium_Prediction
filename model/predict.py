import pickle 
import pandas as pd
from fastapi.responses import JSONResponse



#loading the model
with open("model/model.pkl", "rb") as f:
    model = pickle.load(f)
 
MODEL_VERSION = "1.0.0"

class_labels = model.classes_.tolist()

def predict_output(user_input:dict):
    df = pd.DataFrame([user_input])
    
    
    predicted_class = model.predict(df)[0]
    
    probabilities = model.predict_proba(df)[0]
    
    confidence = max(probabilities)
    
    #class_probabilities = dict(zip(class_labels, probabilities))
    class_probs = dict(zip(class_labels , map(lambda x: round(x, 4) , probabilities)))
    
    return {
        "predicted_class": predicted_class,
        "confidence": round(confidence, 4),
        "class_probabilities": class_probs
    }
