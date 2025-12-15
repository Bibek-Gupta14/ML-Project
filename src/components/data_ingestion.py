# all the reading and loading of data will be done here
import pandas as pd
import os
import sys
from src.exception import CustomException
from src.logger import logging

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

from src.components.model_trainer import ModelTrain
from src.components.model_trainer import ModelTrainConfig

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'raw_data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            # 1. Read the dataset
            df = pd.read_csv('notebook/data/stud.csv')
            logging.info('Read the dataset as dataframe')

            # 2. Create the artifacts directory if it doesn't exist
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            # 3. Save the raw data
            df.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info("Raw data is saved")

            # 4. Split the data into train and test sets
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # 5. Save the train and test sets to their respective paths (created in dataconfig)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False)
            logging.info("Ingestion of the data is completed")

            # returning the train and test data paths to data transformation component
            return (
                self.ingestion_config.train_data_path,  
                self.ingestion_config.test_data_path

            )
        except Exception as e:
            raise CustomException(e, sys)
        
if __name__ == "__main__": 
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_data, test_data)

    model_trainer = ModelTrain()
    final_r2 = model_trainer.initiate_model_trainer(train_arr, test_arr)
    logging.info(f"Model training completed. Final R2 on test set: {final_r2}")