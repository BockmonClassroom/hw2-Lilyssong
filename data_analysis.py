import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data from the CSV file
data = pd.read_csv("data/plants_data_with_units.csv")

# Print the first few rows of the dataset to preview the data
print(data.head())

# Plot histograms for Leaf-width and Leaf-length
data.hist(column=["Leaf-width (cm)", "Leaf-length (cm)"], bins=10, figsize=(10, 5), grid=False)
plt.suptitle("Histograms of Leaf Dimensions")
plt.show()

# Plot boxplot for Leaf-width by Plant Name
plt.figure(figsize=(10, 6))
sns.boxplot(x="Plant Name", y="Leaf-width (cm)", data=data)
plt.title("Boxplot of Leaf Width by Plant")
plt.show()

# Plot scatter plot of Leaf-length vs Leaf-width with Plant Name as hue
sns.scatterplot(x="Leaf-length (cm)", y="Leaf-width (cm)", hue="Plant Name", data=data, palette="viridis")
plt.title("Scatter Plot of Leaf Dimensions")
plt.xlabel("Leaf Length (cm)")
plt.ylabel("Leaf Width (cm)")
plt.legend(title="Plant Name")
plt.show()

# Calculate summary statistics for each plant type
summary = data.groupby("Plant Name").agg(
    mean_width=("Leaf-width (cm)", "mean"),
    mean_length=("Leaf-length (cm)", "mean"),
    median_width=("Leaf-width (cm)", "median"),
    median_length=("Leaf-length (cm)", "median"),
    std_width=("Leaf-width (cm)", "std"),
    std_length=("Leaf-length (cm)", "std"),
)

# Print the summary statistics to the console
print(summary)

# Save the summary statistics to a CSV file
summary.to_csv("data/summary_statistics.csv")
