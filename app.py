from flask import Flask, request, render_template # type: ignore
import sys
from src.pipeline.predict_pipeline import CustomData, PredictPipeline
from src.logger import logging
from src.exception import CustomException

app = Flask(__name__)
application = app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
def predict_ion():
    if request.method == 'GET':
        return render_template('home.html')
    
    else:
        try:
            data = CustomData(
                gender = request.form.get('gender'),
                race_ethnicity = request.form.get('race_ethnicity'),
                parental_level_of_education = request.form.get('parental_level_of_education'),
                lunch = request.form.get('lunch'),
                test_preparation_course = request.form.get('test_preparation_course'),
                math_score = int(request.form.get('math_score')),
                writing_score = int(request.form.get('writing_score'))
            )
            df = data.get_data_as_data_frame()
            print(df)

            prediction = PredictPipeline()
            results = prediction.predict(df)

            logging.info("Prediction successful")
            logging.info(f"The prediction results are: {results}")

            return render_template('home.html', results=results[0])
        
        except Exception as e:
            logging.info(f"Exception occurred during prediction: {e}")
            raise CustomException(e, sys)
        
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
    