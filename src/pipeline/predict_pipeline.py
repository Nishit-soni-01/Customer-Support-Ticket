import sys
import os
import pandas as pd
from src.exception import CustomException
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path = os.path.join("artifacts", "model.pkl")
            preprocessor_path = os.path.join("artifacts", "preprocessor.pkl")
            label_encoder_path = os.path.join("artifacts", "label_encoder.pkl")
            
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)
            le = load_object(file_path=label_encoder_path)
            
            # Vectorize text and execute classification
            data_scaled = preprocessor.transform(features)
            pred_encoded = model.predict(data_scaled)
            
            # Decode the numeric classification back to the string category name
            pred_decoded = le.inverse_transform(pred_encoded)
            return pred_decoded
            
        except Exception as e:
            raise CustomException(e, sys)

class NLPData:
    def __init__(self, ticket_description: str):
        self.ticket_description = ticket_description

    def get_data_as_data_frame(self):
        try:
            return pd.DataFrame({"Ticket Description": [self.ticket_description]})
        except Exception as e:
            raise CustomException(e, sys)