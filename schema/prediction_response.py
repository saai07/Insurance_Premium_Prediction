from pydantic import BaseModel , Field , computed_field , field_validator
from typing import Annotated , Literal

class PredictionResponse(BaseModel):
    predicted_class :str = Field(
        ...,
        description = "Predicted class label",
        example = "high")
    
    
    confidence : float = Field(
        ...,
        ge = 0,
        le = 1,
        description = "Confidence score of the prediction",
        example = 0.85
    )
    
    class_probabilities : dict = Field(
        ...,
        description = "Probabilities for each class label",
        example = {"low": 0.1, "medium": 0.05, "high": 0.85}
    )
    