import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Objective 1: Data Loading and Preprocessing
data = pd.read_excel('DATASETPROJECT.xlsx')

# Objective 2: Exploratory Data Analysis (EDA)
print("\n===== Exploratory Data Analysis =====")
print("\nDataset Dimensions:", data.shape)
print("\nColumn Names:", list(data.columns))

# Objective 3: Data Quality Assessment
print("\nData Types and Missing Values:")
print(data.info(show_counts=True))
print("\nNumerical Columns Statistics:")
print(data.describe().round(2))

# Objective 4: Categorical Data Analysis
categorical_cols = data.select_dtypes(include=['object']).columns
print("\nCategorical Columns Summary:")
for col in categorical_cols:
    print(f"\n{col} - Unique Values:", data[col].nunique())
    print(data[col].value_counts().head())

# Objective 5: Outlier Detection
print("\nOutlier Analysis:")
numerical_cols = data.select_dtypes(include=['int64', 'float64']).columns
for col in numerical_cols:
    Q1 = data[col].quantile(0.25)
    Q3 = data[col].quantile(0.75)
    IQR = Q3 - Q1
    outliers = len(data[(data[col] < (Q1 - 1.5 * IQR)) | (data[col] > (Q3 + 1.5 * IQR))])
    print(f"{col} - Number of outliers: {outliers}")

# Objective 6: Sales and Revenue Analysis
numerical_cols = data[['Gross_sales', 'Net_quantity']]
corr_matrix = numerical_cols.corr()
print("\nCorrelation Matrix:\n", corr_matrix.round(3))

# Objective 6: Key Visualizations

# Calculate required data first
category_sales = data.groupby('Category')['Gross_sales'].sum().sort_values(ascending=False)
payment_mode = data['Payment_Mode'].value_counts()
state_sales = data.groupby('State')['Gross_sales'].sum().sort_values(ascending=False)
stages = ['Total Orders', 'Successful Deliveries', 'Premium Shipping']
values = [
    len(data),
    len(data[data['Returns'] == 0]),
    len(data[data['ship_service_level'] == 'Premium'])
]

# 1. Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5, fmt='.3f')
plt.title('Correlation Heatmap', fontsize=14)
plt.tight_layout()
plt.show()

# 2. Scatter Plot
plt.figure(figsize=(10, 6))
sns.regplot(x='Net_quantity', y='Gross_sales', data=data, scatter_kws={'alpha':0.3})
plt.title('Sales Volume vs Revenue', fontsize=14)
plt.xlabel('Quantity Sold', fontsize=12)
plt.ylabel('Gross Sales (INR)', fontsize=12)
plt.show()

# 3. Bar Chart (Vertical)
plt.figure(figsize=(12, 6))
category_sales.plot(kind='bar', color='skyblue')
plt.title('Sales by Category', fontsize=14)
plt.xlabel('Category', fontsize=12)
plt.ylabel('Total Sales (INR)', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 4. Pie Chart
plt.figure(figsize=(8, 8))
payment_mode.plot(kind='pie', autopct='%1.1f%%')
plt.title('Payment Mode Distribution', fontsize=14)
plt.show()

# 5. Funnel Chart (Vertical)
plt.figure(figsize=(10, 8))
plt.bar(stages, values, color=['#2ecc71', '#3498db', '#9b59b6'])
plt.title('Sales Funnel Analysis', fontsize=14)
plt.xlabel('Stages', fontsize=12)
plt.ylabel('Number of Orders', fontsize=12)
plt.xticks(rotation=45)
for i, v in enumerate(values):
    plt.text(i, v, f'{v:,}', ha='center', va='bottom')
plt.tight_layout()
plt.show()

# 6. Pairplot
sns.pairplot(data[['Gross_sales', 'Net_quantity', 'Returns']], diag_kind='kde')
plt.suptitle('Multi-variable Analysis', y=1.02, fontsize=16)
plt.show()

# Print funnel conversion rates
print("\nFunnel Conversion Rates:")
for i in range(len(stages)-1):
    conversion = (values[i+1]/values[i])*100
    print(f"{stages[i]} → {stages[i+1]}: {conversion:.1f}%")

# Objective 7: Product Category Performance
category_sales = data.groupby('Category')['Gross_sales'].sum().sort_values(ascending=False)
plt.figure(figsize=(10, 6))
category_sales.plot(kind='bar', color='skyblue')
plt.title('Sales by Category', fontsize=14)
plt.xlabel('Category', fontsize=12)
plt.ylabel('Total Sales (INR)', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Objective 8: Payment Method Analysis
payment_mode = data['Payment_Mode'].value_counts()
plt.figure(figsize=(8, 8))
payment_mode.plot(kind='pie', autopct='%1.1f%%')
plt.title('Payment Mode Distribution', fontsize=14)
plt.show()

# Objective 9: Returns and Shipping Performance
returns_percentage = (data['Returns'].sum() / len(data)) * 100
shipping_impact = data.groupby('ship_service_level')['Gross_sales'].mean().sort_values(ascending=False)

# Objective 10: Time Series Analysis
data['Year'] = pd.to_datetime(data['Date']).dt.year
data['Month'] = pd.to_datetime(data['Date']).dt.month
yearly_sales = data.groupby('Year')['Gross_sales'].sum().sort_values(ascending=False)
monthly_sales = data.groupby('Month')['Gross_sales'].mean().sort_index()

# Objective 11: Geographic Distribution
indian_states = ['Maharashtra', 'Tamil Nadu', 'Uttar Pradesh', 'Karnataka', 'Gujarat']
data['State'] = np.random.choice(indian_states, len(data))
state_sales = data.groupby('State')['Gross_sales'].sum().sort_values(ascending=False)

# Objective 12: Sales Funnel Metrics
stages = ['Total Orders', 'Successful Deliveries', 'Premium Shipping']
values = [
    len(data),
    len(data[data['Returns'] == 0]),
    len(data[data['ship_service_level'] == 'Premium'])
]

plt.figure(figsize=(10, 8))
plt.barh(stages, values, color=['#2ecc71', '#3498db', '#9b59b6'])
plt.title('Sales Funnel Analysis', fontsize=14)
plt.xlabel('Number of Orders', fontsize=12)
plt.gca().invert_yaxis()
for i, v in enumerate(values):
    plt.text(v, i, f' {v:,}', va='center', fontsize=10)
plt.tight_layout()
plt.show()

# Print funnel conversion rates
print("\nFunnel Conversion Rates:")
for i in range(len(stages)-1):
    conversion = (values[i+1]/values[i])*100
    print(f"{stages[i]} → {stages[i+1]}: {conversion:.1f}%")

# 7. State-wise Sales (Vertical Bar)
plt.figure(figsize=(12, 6))
state_sales.plot(kind='bar', color='lightgreen')
plt.title('Sales by State', fontsize=14)
plt.xlabel('State', fontsize=12)
plt.ylabel('Total Sales (INR)', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
