import os
import sys
from dataclasses import dataclass
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from src.exception import CustomException
from src.logger import logging
from src.utils import save_object

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts", "model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, X_train, y_train, X_test, y_test):
        try:
            logging.info("Training Balanced Random Forest Classifier")
            
            model = RandomForestClassifier(n_estimators=100, class_weight='balanced', random_state=42)
            model.fit(X_train, y_train)

            y_pred = model.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            logging.info(f"Model Evaluation Complete. Accuracy: {accuracy}")

            save_object(self.model_trainer_config.trained_model_file_path, model)
            return accuracy
        except Exception as e:
            raise CustomException(e, sys)