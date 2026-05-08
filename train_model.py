import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor

# Load dataset
df = pd.read_csv("OLX_cars_dataset00.csv")

# Select useful columns
features = [
    'Make',
    'Model',
    'Year',
    "KM's driven",
    'Fuel',
    'Registration city',
    'Transmission',
    'Assembly',
    'Condition'
]

target = 'Price'

# Remove missing values
df = df[features + [target]].dropna()

# Split data
X = df[features]
y = df[target]

# Categorical columns
categorical_cols = [
    'Make',
    'Model',
    'Fuel',
    'Registration city',
    'Transmission',
    'Assembly',
    'Condition'
]

# Numerical columns
numerical_cols = [
    'Year',
    "KM's driven"
]

# Preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols)
    ],
    remainder='passthrough'
)

# Pipeline
model = Pipeline([
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor())
])

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model.fit(X_train, y_train)

# Save model
joblib.dump(model, 'car_price_model.pkl')

print("Model trained and saved successfully!")