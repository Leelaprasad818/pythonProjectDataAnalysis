import pandas as pd
import numpy as np

# Create sample data with the expected columns
data = pd.DataFrame({
    'Category': np.random.choice(['Electronics', 'Clothing', 'Home', 'Books', 'Sports'], 100),
    'Sales': np.random.uniform(10, 1000, 100),
    'Quantity': np.random.randint(1, 20, 100),
    'Payment Mode': np.random.choice(['Credit Card', 'Debit Card', 'Cash', 'UPI', 'Net Banking'], 100),
    'Returns': np.random.choice([0, 1], 100, p=[0.95, 0.05]),
    'State': np.random.choice(['California', 'Texas', 'New York', 'Florida', 'Illinois'], 100),
    'Shipping Service': np.random.choice(['Standard', 'Express', 'Premium', 'Same Day'], 100)
})

# Save to Excel file
data.to_excel('DATASETPROJECT.xlsx', index=False)
print('Sample dataset created successfully!')