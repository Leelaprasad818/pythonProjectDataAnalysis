import pandas as pd

# Load the dataset
data = pd.read_excel('DATASETPROJECT.xlsx')

# Display basic information about the dataset
print("\nDataset Info:")
data.info()

# Display descriptive statistics
print("\nDescriptive Statistics:")
print(data.describe())

# Display data types
print("\nData Types:")
print(data.dtypes)

# Display first few rows
print("\nFirst 5 rows:")
print(data.head())