import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

# Sample data
data = pd.DataFrame({
    'Age': [25, 40, 30],
    'Income': [50000, 80000, 60000],
    'Gender': ['Male', 'Female', 'Male']
})

# Define features
numeric_features = ['Age', 'Income']
categorical_features = ['Gender']

# Build preprocessor
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features),
        ('cat', OneHotEncoder(), categorical_features)
    ])

# Apply preprocessing
processed = preprocessor.fit_transform(data)
print(processed.toarray())