# Walmart Sales Prediction

## Project Overview

This project aims to predict weekly sales for Walmart stores using historical sales data. The model leverages features such as store, temperature, fuel price, CPI, unemployment, holiday information, and date components to make accurate predictions. The final application is deployed as a web-based system using Flask, allowing users to input features and get sales predictions.

## Table of Contents

- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Features](#features)
- [Model](#model)
- [Web Application](#web-application)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Dataset

The dataset contains historical sales data for Walmart stores. It includes the following features:
- `Store`: The store number.
- `Date`: The week of sales.
- `Weekly_Sales`: The sales for the given store and date.
- `Temperature`: The average temperature in the region.
- `Fuel_Price`: The cost of fuel in the region.
- `CPI`: The consumer price index.
- `Unemployment`: The unemployment rate.
- `IsHoliday`: Whether the week is a special holiday week.

## Features

The model uses the following features for prediction:
- `Store`
- `Temperature`
- `Fuel_Price`
- `CPI`
- `Unemployment`
- `IsHoliday`
- `Year`
- `Month`
- `Week`

## Model

The model is built using a Decision Tree Regressor. The final trained model is saved using pickle and deployed in a Flask web application.

## Web Application

The web application allows users to input feature values and get sales predictions. It is built using Flask and provides an intuitive interface for user interaction.

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Hsinha11/Walmart_Sales_Prediction.git
   cd Walmart_Sales_Prediction
2. **Create a virtual environment:**
   ```bash
   python -m venv venv
3. **Activate the virtual environment:**
   - On Windows:
     ```bash
     venv\Scripts\activate
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
4. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
5. **Download the pre-trained model from Google Colab and place it in the project directory. Name the file walmart_sales_model.pkl.**
6. **Run the Flask Application**
   ```bash
   python app.py

## Usage

1. Open your web browser and go to `http://127.0.0.1:5000/`.
2. Enter the required feature values:
   - Store
   - Temperature
   - Fuel Price
   - CPI
   - Unemployment
   - IsHoliday (0 or 1)
   - Year
   - Month
   - Week
3. Click on the "Predict" button to get the sales prediction.

The web application will display the predicted weekly sales based on the input features.

## Contributing

We welcome contributions to the Walmart Sales Prediction project! If you have suggestions for improvements, new features, or bug fixes, please follow these steps:

1. **Fork the repository**: Click on the "Fork" button at the top right corner of the repository page to create a copy of the repository on your GitHub account.

2. **Clone your forked repository**:
   ```bash
   git clone https://github.com/your-username/Walmart_Sales_Prediction.git
   cd Walmart_Sales_Prediction
3. **Create a new branch: Create a new branch for your feature or bug fix.**
   ```bash
   git checkout -b feature-name
4. **Make your changes**
   Implement your feature or bug fix.
5.**Commit your changes**
   Ensure your commit messages are clear and descriptive.
   ```bash
   git add .
   git commit -m "Description of the feature or fix"
6. **Push to your forked repository**
   ```bash
   git push origin feature-name
7. **Create a Pull Request**
   Go to the original repository on GitHub and click on the "New Pull Request" button. Select the branch you created from your forked repository and submit the pull request. Provide a clear and detailed description of your changes.
8. **Code Review**
   Your pull request will be reviewed, and you may be asked to make some changes. Once approved, your changes will be merged into the main repository.

#### Thank you for your contributions!

## License

This project is licensed under the MIT License. 
