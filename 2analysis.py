import pandas as pd
import matplotlib.pyplot as plt

print("================================")
print(" STUDENT MARKS ANALYSIS SYSTEM ")
print("================================")

# Load CSV file
df = pd.read_csv("students.csv")

print("\nOriginal Dataset:")
print(df)

# Data Cleaning
df.dropna(inplace=True)

print("\nDataset After Cleaning:")
print(df)

# Average Marks
average = df["Marks"].mean()

# Highest Scorer
highest = df.loc[df["Marks"].idxmax()]

# Lowest Scorer
lowest = df.loc[df["Marks"].idxmin()]

print("\nAnalysis Results")
print("----------------------------")

print("Average Marks:", round(average, 2))

print("\nHighest Scorer")
print(highest)

print("\nLowest Scorer")
print(lowest)

# Visualization
plt.figure(figsize=(8,5))
plt.bar(df["Name"], df["Marks"])

plt.title("Student Marks Analysis")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.savefig("marks_chart.png")

plt.show()

print("\nChart Saved Successfully!")