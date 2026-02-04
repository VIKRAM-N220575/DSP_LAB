#1.importing needed libraries so that we can use them later in the code
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#2.Loading the dataset
data = pd.read_csv('Customer Purchasing Behaviors.csv')

#3.To display the number of rows and columns in the dataset
print("Dataset Shape:", data.shape)
print("Number of Rows:", data.shape[0])
print("Number of Columns:", data.shape[1])
print("\n")

#4.Displaying the column names
print("Column Names:")
for i, col in enumerate(data.columns):
    print(f"Column {i}: {col}")
print("\n")

#5.Displaying the first 5 rows of the dataset
print("First 5 Rows of the Dataset:")
print(data.head(3))
print("\n")

#6.Checking the data types of each column
print("Data Types of Each Column:")
for col in data.columns:
    print(f"{col}: {data[col].dtype}")
print("\n")

#7.Checking for missing values in each column
print("Missing Values in Each Column:")
for col in data.columns:
    missing_count = data[col].isnull().sum()
    print(f"{col}: {missing_count} missing values")
print("\n")

#8.Filling missing values for numerical columns with the mean of the column
numerical_cols = data.select_dtypes(include=[np.number]).columns
for col in numerical_cols:
    mean_value = data[col].mean()
    floor_mean_value = np.floor(mean_value)
    data[col].fillna(floor_mean_value)
    print(f"Filled missing values in {col} with floor of mean value: {floor_mean_value}")
print("\n")

#9.Filling missing values for categorical columns with the mode of the column
categorical_cols = data.select_dtypes(include=['object','string']).columns
for col in categorical_cols:
    mode_value = data[col].mode()[0]
    data[col].fillna(mode_value)
    print(f"Filled missing values in {col} with mode value: {mode_value}")
print("\n")

#10.To verify that there are no missing values left
print("Missing Values After Filling:")
for col in data.columns:
    missing_count = data[col].isnull().sum()
    print(f"{col}: {missing_count} missing values")
print("\n")

#11. To calculate the mean of numerical columns
print("Mean of Numerical Columns:")
for col in numerical_cols:
    mean_value = data[col].mean()
    print(f"{col}: Mean = {mean_value}")
print("\n")

#12. To calculate the median of numerical columns
print("Median of Numerical Columns:")
for col in numerical_cols:
    median_value = data[col].median()
    print(f"{col}: Median = {median_value}")
print("\n")

#13. To calculate the standard deviation of numerical columns
print("Standard Deviation of Numerical Columns:")
for col in numerical_cols:
    std_value = data[col].std()
    print(f"{col}: Standard Deviation = {std_value}")
print("\n")

#14. Finding the maximum and minimum values in numerical columns
print("Maximum and Minimum Values in Numerical Columns:")
for col in numerical_cols:
    max_value = data[col].max()
    min_value = data[col].min()
    print(f"{col}: Max = {max_value}, Min = {min_value}")
print("\n")

#15. Generating a summary using describe() method
print("Summary Statistics of Numerical Columns:")
print(data[numerical_cols].describe())
print("\n")


#16. Histogram for the purchase amount column
# On x-axis: Purchase Amount
# On y-axis: Frequency
# color: Blue
# Output: A histogram plot showing the distribution of purchase amounts
plt.figure(figsize=(10, 6))
sns.histplot(data['purchase_amount'], bins=30, kde=True, color='red')
plt.title('Distribution of Purchase Amount')
plt.xlabel('Purchase Amount')
plt.ylabel('Frequency')
plt.show()
print("\n")

#17. A bar plot for the count of customers by region
# On x-axis: Region
# On y-axis: Number of Customers
# color: Green
# Output: A bar plot showing the number of customers in each region
plt.figure(figsize=(10, 6))
sns.countplot(x='region', data=data,hue='region', palette='viridis',legend=False)
plt.title('Number of Customers by Region')
plt.xlabel('Region')
plt.ylabel('Number of Customers')
plt.show()
print("Number of customers in each region:")
print(data['region'].value_counts())
print("\n")

#18. A box plot for purchase amount column
# On x-axis: Region
# On y-axis: Purchase Amount
# color: Orange
# Output: A box plot showing the distribution of purchase amounts across different regions
plt.figure(figsize=(10, 6))
sns.boxplot(x='region', y='purchase_amount', hue='region', data=data, palette='Set2')
plt.title('Purchase Amount by Region')
plt.xlabel('Region')
plt.ylabel('Purchase Amount')
plt.show()


plt.figure(figsize=(8, 5))
sns.boxplot(y=data['purchase_amount'])
plt.title('Box Plot of Purchase Amount')
plt.ylabel('Purchase Amount')
plt.show()

# 19. A scatter plot to visualize the relationship between age and purchase amount
# On x-axis: Age
# On y-axis: Purchase Amount
# color: Purple
# Output: A scatter plot showing the relationship between age and purchase amount
plt.figure(figsize=(10, 6))
sns.scatterplot(x='age', y='purchase_amount', data=data)
plt.title('Age vs Purchase Amount')
plt.xlabel('Age')
plt.ylabel('Purchase Amount')
plt.show()
print("\n")

# 20. A correlation heatmap for numerical columns
# Output: A heatmap showing the correlation between numerical columns in the dataset
# Select only numerical columns
numerical_data = data.select_dtypes(include=["int64", "float64"])

# Compute correlation matrix
corr_matrix = numerical_data.corr()

# Plot heatmap with weather-map style colors
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap="turbo")
plt.title("Correlation Heatmap")
plt.show()
