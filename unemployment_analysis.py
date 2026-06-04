import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("unemployment.csv")

# Display first 5 rows
print("First 5 Rows:")
print(df.head())

# Dataset Information
print("\nDataset Information:")
print(df.info())

# Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove Missing Values
df = df.dropna()

# Basic Statistics
print("\nStatistical Summary:")
print(df.describe())

# Rename columns if needed
# Example:
# df.rename(columns={"Estimated Unemployment Rate (%)":"Unemployment_Rate"}, inplace=True)

# -------------------------------
# Unemployment Rate Distribution
# -------------------------------

plt.figure(figsize=(10,5))
sns.histplot(df.iloc[:, -1], kde=True)
plt.title("Distribution of Unemployment Rate")
plt.show()

# -------------------------------
# State-wise Average Unemployment
# -------------------------------

state_column = df.columns[0]
rate_column = df.columns[-1]

state_avg = df.groupby(state_column)[rate_column].mean().sort_values(ascending=False)

plt.figure(figsize=(12,6))
state_avg.plot(kind='bar')
plt.title("Average Unemployment Rate by State")
plt.ylabel("Unemployment Rate")
plt.tight_layout()
plt.show()

# -------------------------------
# COVID Impact Analysis
# -------------------------------

if 'Date' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'])

    plt.figure(figsize=(12,6))
    plt.plot(df['Date'], df[rate_column])
    plt.title("Unemployment Rate Over Time")
    plt.xlabel("Date")
    plt.ylabel("Unemployment Rate")
    plt.grid(True)
    plt.show()

# -------------------------------
# Top 10 States with Highest Unemployment
# -------------------------------

top10 = state_avg.head(10)

plt.figure(figsize=(10,5))
sns.barplot(x=top10.values, y=top10.index)
plt.title("Top 10 States by Unemployment Rate")
plt.xlabel("Unemployment Rate")
plt.show()

print("\nAnalysis Completed Successfully!")
