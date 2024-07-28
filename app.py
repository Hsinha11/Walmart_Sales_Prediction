from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load the trained model
model_path = 'models/model.pkl'
with open(model_path, 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the data from the form
        store = int(request.form['store'])
        temperature = float(request.form['temperature'])
        fuel_price = float(request.form['fuel_price'])
        cpi = float(request.form['cpi'])
        unemployment = float(request.form['unemployment'])
        isHoliday = int(request.form['isHoliday'])
        year = int(request.form['year'])
        month = int(request.form['month'])
        week = int(request.form['week'])
        
        # Print the input data for debugging
        print(f"Input data - Store: {store}, Temperature: {temperature}, Fuel_Price: {fuel_price}, CPI: {cpi}, Unemployment: {unemployment}, IsHoliday: {isHoliday}, Year: {year}, Month: {month}, Week: {week}")
        
        # Create a DataFrame with the input features
        input_data = pd.DataFrame([[store, temperature, fuel_price, cpi, unemployment, isHoliday, year, month, week]], 
                                  columns=['Store', 'Temperature', 'Fuel_Price', 'CPI', 'Unemployment', 'IsHoliday', 'Year', 'Month', 'Week'])
        
        # Make prediction
        prediction = model.predict(input_data)
        output = prediction[0]
        
        print(f"Prediction: {output}")  # Print the prediction for debugging
        
        return render_template('index.html', prediction=output)
    
    except Exception as e:
        print(f"Error: {str(e)}")  # Print the error message for debugging
        return render_template('index.html', prediction='Error: ' + str(e))

if __name__ == '__main__':
    app.run(debug=True)
