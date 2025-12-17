import sys 
import pandas as pd
from src.exception import CustomException
from sklearn.preprocessing import StandardScaler
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass
    
    # actually making prediction pipeline
    def predict(self, features):
        model_path = 'artifacts/model.pkl'
        preprocessor_path = 'artifacts/preprocessor.pkl'

        model = load_object(filepath=model_path)
        preprocessor = load_object(filepath=preprocessor_path)

        # Transform the features using the preprocessor and make predictions using the model
        scaled_data = preprocessor.transform(features)
        prediction = model.predict(scaled_data)

        return prediction

class CustomData:

    def __init__(self,gender: str, race_ethnicity: str, parental_level_of_education: str, lunch: str, test_preparation_course: str, math_score: int, writing_score: int):

        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.math_score = math_score
        self.writing_score = writing_score

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "math_score": [self.math_score],
                "writing_score": [self.writing_score]
            }
            return pd.DataFrame(custom_data_input_dict)
        except Exception as e:
            raise CustomException(e, sys)