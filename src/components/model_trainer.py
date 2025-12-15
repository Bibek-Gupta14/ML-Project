# all the model training related code will go here
import os
import sys
from dataclasses import dataclass

from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, AdaBoostRegressor
from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from xgboost import XGBRegressor
from sklearn.metrics import r2_score

from src.exception import CustomException
from src.logger import logging

from src.utils import save_object, evaluate_models


@dataclass
class ModelTrainConfig:
    trained_model_file_path=os.path.join("artifacts","model.pkl")

class ModelTrain:
    def __init__(self):
        self.model_train_config=ModelTrainConfig()

    def initiate_model_trainer(self,train_array,test_array):
        try:
            logging.info("Splitting training and test input data")
            X_train,y_train= train_array[:,:-1], train_array[:,-1]
            X_test,y_test= test_array[:,:-1], test_array[:,-1]

            models={
                "Random Forest": RandomForestRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "Linear Regression": LinearRegression(),
                "XGB Regressor": XGBRegressor(),
                "AdaBoost Regressor": AdaBoostRegressor(),
                "Lasso": Lasso(),
                "Ridge": Ridge(),
                "KNeighbors Regressor": KNeighborsRegressor()
            }

            params = {
                'Random Forest': {
                    'n_estimators': [50, 100, 200],
                    'max_depth': [None, 10, 20],
                    'min_samples_split': [2, 5, 10]
                },
                'Decision Tree': {
                    'max_depth': [None, 10, 20],
                    'min_samples_split': [2, 5, 10]
                },
                'Gradient Boosting': {
                    'n_estimators': [50, 100, 200],
                    'learning_rate': [0.01, 0.1, 0.2],
                    'max_depth': [3, 5, 10]
                },
                'Linear Regression': {},
                'XGB Regressor': {
                    'n_estimators': [50, 100, 200],
                    'learning_rate': [0.01, 0.1, 0.2],
                    'max_depth': [3, 5, 10]
                },
                'AdaBoost Regressor': {
                    'n_estimators': [50, 100, 200],
                    'learning_rate': [0.01, 0.1, 0.2]
                },
                'Lasso': {
                    'alpha': [0.01, 0.1, 1.0, 10.0]
                },
                'Ridge': {
                    'alpha': [0.01, 0.1, 1.0, 10.0]
                },
                'KNeighbors Regressor': {
                    'n_neighbors': [3, 5, 7, 9],
                    'weights': ['uniform', 'distance']
                }
            }            
            model_report={}
            logging.info("Starting model evaluation")

            model_report = evaluate_models(X_train, y_train, X_test, y_test, models, params)
            logging.info("Model evaluation completed")

            #getting the best model from the dict
            best_model_score=max(model_report.values())
            best_model_name=list(model_report.keys())[list(model_report.values()).index(best_model_score)]
            best_model=models[best_model_name]


            # creating a threshold value
            if(best_model_score < 0.5):
                raise CustomException("No best model found with r2 score greater than the threshold 0.5")
            
            logging.info(f"Best model found: {best_model_name} with score: {best_model_score}")

            save_object(
                file_path=self.model_train_config.trained_model_file_path,
                obj=best_model
            )

            predicted=best_model.predict(X_test)
            final_r2_score=r2_score(y_test,predicted)
            return final_r2_score

        except Exception as e:
            raise CustomException(e,sys)

