from flask import Flask,render_template, request
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import pickle

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/prediction', methods=['POST'])
def prediction():
    age = request.form['age']
    gender = request.form['gender']
    estimated_salary = request.form['estimated_salary']
    if gender.lower() == 'male':
        gender_male = '1'
        gender_female = '0'
    else:
        gender_male = '0'
        gender_female = '1'

    input_data = np.array([[age, estimated_salary,gender_female, gender_male]])
    model = pickle.load(open('rfmodel.pkl','rb'))
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        result = "Yes, the person is likely to purchase the product."
    else:
        result = "No, the person is not likely to purchase the product."

    return render_template('index.html', prediction_text=result)

if __name__=='__main__':
    app.run()