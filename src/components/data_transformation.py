import sys
import os
import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from src.exception import CustomException
from src.logger import logging
from src.utils import save_object
from dataclasses import dataclass

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts', "preprocessor.pkl")
    label_encoder_obj_file_path = os.path.join('artifacts', "label_encoder.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def initiate_data_transformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Obtaining TF-IDF preprocessor and LabelEncoder")
            tfidf = TfidfVectorizer(stop_words='english', max_features=5000)
            le = LabelEncoder()

            text_col = "Ticket Description"
            target_col = "Ticket Type"

            # Transform features
            input_feature_train_arr = tfidf.fit_transform(train_df[text_col]).toarray()
            input_feature_test_arr = tfidf.transform(test_df[text_col]).toarray()

            # Transform targets
            target_feature_train_arr = le.fit_transform(train_df[target_col])
            target_feature_test_arr = le.transform(test_df[target_col])

            logging.info("Saving preprocessing and transformation objects")
            save_object(self.data_transformation_config.preprocessor_obj_file_path, tfidf)
            save_object(self.data_transformation_config.label_encoder_obj_file_path, le)

            return (
                input_feature_train_arr,
                target_feature_train_arr,
                input_feature_test_arr,
                target_feature_test_arr
            )
        except Exception as e:
            raise CustomException(e, sys)