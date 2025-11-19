import pandas as pd
from sklearn.model_selection import train_test_split

# Preprocessing the dataset
df = pd.read_csv('Data/survey-lung-cancer.csv')
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)
train_df.to_csv('Data/train_lung_cancer.csv', index=False)
test_df.to_csv('Data/test_lung_cancer.csv', index=False)