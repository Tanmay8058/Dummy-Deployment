from flask import Flask, render_template
from forms import Prediction
import pandas as pd
import joblib

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'

model = joblib.load('model.joblib')

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    form = Prediction()
    message = ""
    if form.validate_on_submit():
        x_new = pd.DataFrame(dict(
            area=[form.area.data],
            rooms=[form.rooms.data]
        ))
        price_predicted = model.predict(x_new)[0]
        message = f"The predicted price is {price_predicted:,.0f} INR!"
    else:
        if form.is_submitted():
            message = "Please provide valid input details!"
    return render_template('predict.html', title='Predict', form=form, message=message)

if __name__ == '__main__':
    app.run(debug=True)
