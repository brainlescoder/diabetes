


from flask import Flask, request, render_template, jsonify

import pandas as pd
import pickle
import numpy as np

app = Flask(__name__, template_folder='templates')
model = pickle.load_model('diabetes_model')

@app.route("/")

@app.route('/diabetes')
def diabetes():
    return render_template('diabetes.html')
def value_prediction(to_predict_list, size):
    # it is the array input from the site
    to_predict = np.array(to_predict_list).reshape(1, size)
    if(size == 8):
        result = model.predict(to_predict)#using the input given
    return result[0]


@app.route('/predict_diabetes', methods =['POST'])
def predict_diabetes():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        if (len(to_predict_list) == 8):
            result = value_prediction(to_predict_list, 8)
    if int(result) == 1:
        prediction = 'Sorry! You have got diabetes.' \
                     'If not then there is a very chance of getting it' \
                     'Contact your physician as soon as possible'

    else:
        prediction = 'Congratulation!! You are in good hands' \
                     'You are perfectly fine, take care'

    return (render_template('result.html', prediction_text = prediction))


if __name__ == '__main__':
    app.run(debug=True)



# colums are
#'Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
#       'BMI', 'DiabetesPedigreeFunction', 'Age'