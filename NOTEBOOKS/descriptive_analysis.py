# Exploratory visualizations and summary statistics of the data
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv("Data/survey-lung-cancer.csv")

# EDA and summary of statistics
print("First 5 rows of the dataset:")
print(data.head()) 
print("\nSummary statistics of the dataset:")
print(data.describe())
print("\nMissing values in each column:")
print(data.isnull().sum())

# Visualizations

# -- Distribution of Age --
print("\nVisualizing the distribution of Age:")
plt.figure(figsize=(10,6))
sns.histplot(data['AGE'], bins=20, kde=True)
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

