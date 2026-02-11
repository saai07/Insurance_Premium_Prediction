from pydantic import BaseModel , Field , computed_field , field_validator
from typing import Annotated , Literal
from config.city_list import tier_1_cities , tier_2_cities



class PredictionRequest(BaseModel):
    age: Annotated[int , Field(ge = 0 , lt= 120 , description = "Age of the user in years") ]
    weight: Annotated[float , Field(ge = 0 , lt= 120 , description = "Weight of the user in kilograms") ]
    height: Annotated[float , Field(ge = 0 , lt= 2.5 , description = "Height of the user in meters") ]
    smoker: Annotated[bool , Field(description = "Whether the user is a smoker or not") ]
    income_lpa: Annotated[float , Field(ge = 1 , description = "Income of the user in lakhs per annum") ]
    city: Annotated[str , Field(description = "City of the user") ]
    occupation: Annotated[Literal['retired', 'freelancer', 'student', 'government_job',
       'business_owner', 'unemployed', 'private_job'] , Field(description = "Occupation of the user") ]
    
    
    @computed_field
    @property
    def bmi(self) -> float:
        return self.weight / (self.height ** 2)
    
    @computed_field
    @property
    #lifestyle risk
    def lifestyle_risk(self) -> str:
        if self.smoker and self.bmi > 30:
            return "high"
        elif self.smoker or self.bmi > 27:
            return "medium"
        else:
            return "low"
        
    @computed_field
    @property
    def age_group(self) -> str:
        if self.age < 25:
            return "young"
        elif self.age < 40:
            return "adult"
        elif self.age < 60:
            return "middle_aged"
        else:   
            return "senior"
    
    @computed_field
    @property
    def city_tier(self) -> int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3
        
    @field_validator("city")
    @classmethod
    def normilize_city(cls , value:str) -> str:
        return value.strip().title()