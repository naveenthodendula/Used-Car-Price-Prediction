from flask import Flask, render_template, request, redirect, url_for, session
import pandas as pd
import joblib

app = Flask(__name__)

# Secret key for session
app.secret_key = "carpriceprediction"

# Load trained model
model = joblib.load('car_price_model.pkl')


@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':

        try:
            data = {
                'Make': request.form.get('Make'),
                'Model': request.form.get('Model'),
                'Year': int(request.form.get('Year')),
                "KM's driven": int(request.form.get("KM's driven")),
                'Fuel': request.form.get('Fuel'),
                'Registration city': request.form.get('Registration city'),
                'Transmission': request.form.get('Transmission'),
                'Assembly': request.form.get('Assembly'),
                'Condition': request.form.get('Condition')
            }

            input_df = pd.DataFrame([data])

            prediction = model.predict(input_df)[0]
            prediction = round(float(prediction), 2)

            # Save prediction temporarily
            session['prediction'] = prediction

            # Redirect after POST
            return redirect(url_for('home'))

        except Exception as e:
            session['prediction'] = f"Error: {e}"
            return redirect(url_for('home'))

    # GET request
    prediction = session.pop('prediction', None)

    return render_template('index.html', prediction=prediction)


if __name__ == '__main__':
    app.run(debug=True)