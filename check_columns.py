import pandas as pd

# Load the dataset
try:
    data = pd.read_excel('DATASETPROJECT.xlsx')
    print("Columns in the dataset:")
    print(data.columns.tolist())
    print("\nFirst 5 rows:")
    print(data.head())
except Exception as e:
    print(f"Error: {e}")