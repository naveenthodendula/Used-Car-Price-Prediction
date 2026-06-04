🚗 Used Car Price Prediction

A Machine Learning-powered web application that predicts the price of a used car based on its specifications. The model analyzes key vehicle attributes and provides an estimated market value instantly through an interactive web interface.

🌐 Live Demo

🔗 Live Application: https://used-car-price-prediction-1-nf16.onrender.com

📖 Project Overview

Buying or selling a used car often involves uncertainty regarding its fair market value. This project leverages Machine Learning to estimate car prices based on various vehicle features such as manufacturer, model, year, mileage, fuel type, transmission, and more.

The application is deployed on Render, allowing users to access real-time predictions through a web browser.

🎯 Features
Predict used car prices instantly
User-friendly web interface
Machine Learning regression model
Real-time predictions
Cloud deployment using Render
End-to-end ML pipeline implementation
📊 Input Features

The model uses the following features:

Feature	Description
Manufactured Company	Car manufacturer
Model	Car model
Year	Manufacturing year
KM Driven	Total kilometers driven
Fuel	Fuel type
Registration City	Registered city
Transmission	Manual / Automatic
Assembly	Local / Imported
Condition	Vehicle condition

🛠️ Tech Stack
Programming Language
Python
Libraries
Pandas
NumPy
Scikit-learn
Pickle
Web Framework
Flask
Frontend
HTML
CSS
Deployment
Render

🔄 Project Workflow

1️⃣ Data Collection
Gathered used car dataset
Inspected data quality

2️⃣ Exploratory Data Analysis (EDA)
Analyzed price distributions
Identified trends and patterns
Detected outliers

3️⃣ Data Preprocessing
Handled missing values
Encoded categorical variables
Prepared features for training

4️⃣ Model Training
Trained regression models
Compared model performance
Selected the best-performing model

5️⃣ Model Evaluation
Evaluated using regression metrics
Optimized for better prediction accuracy

6️⃣ Web Application Development
Built a Flask-based prediction interface
Connected frontend with trained model

7️⃣ Deployment
Deployed application on Render
Enabled online access for users

📂 Project Structure
Used-Car-Price-Prediction/
│
├── static/
│   ├── css/
│
├── templates/
│   ├── index.html
│
├── model/
│   ├── car_price_model.pkl
│
├── app.py
├── requirements.txt
├── README.md
└── dataset.csv

🚀 Installation & Setup
Clone the Repository
git clone https://github.com/naveenthodendula/Used-Car-Price-Prediction.git
Navigate to Project Folder
cd Used-Car-Price-Prediction
Create Virtual Environment
python -m venv venv
Activate Virtual Environment

Windows:

venv\Scripts\activate

Mac/Linux:

source venv/bin/activate
Install Dependencies
pip install -r requirements.txt
Run the Application
python app.py
📸 Screenshots
Home Page

<img width="1910" height="968" alt="Screenshot 2026-06-04 190009" src="https://github.com/user-attachments/assets/fc3dad67-cd17-4de6-926b-cfdb1d49af04" />


Prediction Result

<img width="647" height="833" alt="Screenshot 2026-06-04 190125" src="https://github.com/user-attachments/assets/a5b4737b-bb8f-4bc5-af68-d42968eb9234" />

📈 Future Improvements

Add more vehicle features
Improve model accuracy
Integrate multiple ML models
Add model explainability
Build a responsive mobile interface
Deploy using Docker and CI/CD pipelines
🤝 Contributing

Contributions, suggestions, and feedback are welcome.

Fork the repository
Create a new branch
Make changes
Submit a pull request

👨‍💻 Author

Naveen Thodendula

📧 Email: naveenthodendula@gmail.com

💼 LinkedIn: https://www.linkedin.com/in/naveen-thodendula-9797b230b/

🐙 GitHub: https://github.com/naveenthodendula

⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

It helps others discover the project and motivates future improvements.
