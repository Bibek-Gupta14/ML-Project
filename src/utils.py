import os
import sys
import dill # type: ignore
from src.exception import CustomException
from src.logger import logging
from sklearn.model_selection import GridSearchCV

from sklearn.metrics import r2_score

def save_object(file_path, obj):
    ''' This function is responsible for saving the object to a file '''
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,'wb') as file_obj:
            dill.dump(obj,file_obj)

    except Exception as e:
        raise CustomException(e,sys)

def evaluate_models(X_train, y_train, X_test, y_test, models, params):
    try:
        model_report={}
        for i in range(len(list(models))):

            model=list(models.values())[i]
            model_name=list(models.keys())[i]

            # Hyperparameter tuning
            param=params[model_name]
            grid = GridSearchCV(estimator=model, param_grid=param, cv=3)
            grid.fit(X_train, y_train)
    
            model.set_params(**grid.best_params_)   # setting the best params found by grid search to the model
            model.fit(X_train,y_train)

            y_train_pred=model.predict(X_train)
            y_test_pred=model.predict(X_test)

            train_model_score=r2_score(y_train,y_train_pred)
            test_model_score=r2_score(y_test,y_test_pred)

            model_report[model_name]=test_model_score
            logging.info(f"Training the model: {model_name} and performance: {test_model_score}")

        return model_report

    except Exception as e:
        raise CustomException(e,sys) 
    
def load_object(filepath):
    ''' This function is responsible for loading the object from a file '''
    try:
        with open(filepath,'rb') as file_obj:
            return dill.load(file_obj)
    except Exception as e:
        raise CustomException(e,sys)