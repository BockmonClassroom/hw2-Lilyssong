import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the data from the CSV file
data = pd.read_csv("data/plants_data_with_units.csv")

# Print the first few rows of the dataset to preview the data
print(data.head())

# ------------------------------------------------------
# 1. HISTOGRAMS
# ------------------------------------------------------

# Plot histograms for all data with proper axis labels
plt.figure(figsize=(12, 5))

# Leaf width histogram - all plants
plt.subplot(1, 2, 1)
plt.hist(data["Leaf-width (cm)"], bins=10, color='skyblue', edgecolor='black')
plt.title("Histogram of Leaf Width - All Plants")
plt.xlabel("Leaf Width (cm)")
plt.ylabel("Frequency")
plt.grid(False)

# Leaf length histogram - all plants
plt.subplot(1, 2, 2)
plt.hist(data["Leaf-length (cm)"], bins=10, color='skyblue', edgecolor='black')
plt.title("Histogram of Leaf Length - All Plants")
plt.xlabel("Leaf Length (cm)")
plt.ylabel("Frequency")
plt.grid(False)

plt.tight_layout()
plt.savefig("histograms_all_plants.png")
plt.show()

# Create histograms for each individual plant type
plant_types = data["Plant Name"].unique()

for plant_type in plant_types:
    plt.figure(figsize=(12, 5))
    plant_data = data[data["Plant Name"] == plant_type]
    
    # Leaf width histogram for specific plant
    plt.subplot(1, 2, 1)
    plt.hist(plant_data["Leaf-width (cm)"], bins=8, color='lightgreen', edgecolor='black')
    plt.title(f"Histogram of Leaf Width - {plant_type}")
    plt.xlabel("Leaf Width (cm)")
    plt.ylabel("Frequency")
    plt.grid(False)
    
    # Leaf length histogram for specific plant
    plt.subplot(1, 2, 2)
    plt.hist(plant_data["Leaf-length (cm)"], bins=8, color='lightgreen', edgecolor='black')
    plt.title(f"Histogram of Leaf Length - {plant_type}")
    plt.xlabel("Leaf Length (cm)")
    plt.ylabel("Frequency")
    plt.grid(False)
    
    plt.tight_layout()
    plt.savefig(f"histograms_{plant_type}.png")
    plt.show()

# ------------------------------------------------------
# 2. BOXPLOTS
# ------------------------------------------------------

# Create boxplots for leaf width by plant type
plt.figure(figsize=(12, 6))

# First create a copy of the data with an "All" category for combined view
boxplot_data = data.copy()
boxplot_data_all = data.copy()
boxplot_data_all['Plant Name'] = 'All'
boxplot_data = pd.concat([boxplot_data, boxplot_data_all])

# Boxplot for leaf width
plt.subplot(1, 2, 1)
sns.boxplot(x="Plant Name", y="Leaf-width (cm)", data=boxplot_data)
plt.title("Boxplot of Leaf Width by Plant Type")
plt.xlabel("Plant Type")
plt.ylabel("Leaf Width (cm)")

# Boxplot for leaf length
plt.subplot(1, 2, 2)
sns.boxplot(x="Plant Name", y="Leaf-length (cm)", data=boxplot_data)
plt.title("Boxplot of Leaf Length by Plant Type")
plt.xlabel("Plant Type")
plt.ylabel("Leaf Length (cm)")

plt.tight_layout()
plt.savefig("boxplots.png")
plt.show()

# ------------------------------------------------------
# 3. SCATTER PLOT
# ------------------------------------------------------

# Plot scatter plot of leaf length vs leaf width with plant name as hue
plt.figure(figsize=(10, 8))
sns.scatterplot(x="Leaf-length (cm)", y="Leaf-width (cm)", hue="Plant Name", data=data, palette="viridis")
plt.title("Scatter Plot of Leaf Dimensions")
plt.xlabel("Leaf Length (cm)")
plt.ylabel("Leaf Width (cm)")
plt.legend(title="Plant Name")
plt.savefig("scatter_plot.png")
plt.show()

# ------------------------------------------------------
# 4. CALCULATE SUMMARY STATISTICS FOR EACH PLANT TYPE
# ------------------------------------------------------

# Include variance in addition to mean, median, and std
summary = data.groupby("Plant Name").agg(
    mean_width=("Leaf-width (cm)", "mean"),
    median_width=("Leaf-width (cm)", "median"),
    std_width=("Leaf-width (cm)", "std"),
    var_width=("Leaf-width (cm)", "var"),  # Added variance
    mean_length=("Leaf-length (cm)", "mean"),
    median_length=("Leaf-length (cm)", "median"),
    std_length=("Leaf-length (cm)", "std"),
    var_length=("Leaf-length (cm)", "var")  # Added variance
)

# Calculate statistics for all plants combined
all_stats = {
    'mean_width': data['Leaf-width (cm)'].mean(),
    'median_width': data['Leaf-width (cm)'].median(),
    'std_width': data['Leaf-width (cm)'].std(),
    'var_width': data['Leaf-width (cm)'].var(),
    'mean_length': data['Leaf-length (cm)'].mean(),
    'median_length': data['Leaf-length (cm)'].median(),
    'std_length': data['Leaf-length (cm)'].std(),
    'var_length': data['Leaf-length (cm)'].var()
}

# Add the "All" category to the summary table
summary.loc['All'] = pd.Series(all_stats)

# Print the summary statistics to the console
print("\nSummary Statistics:")
print(summary)

# Save the summary statistics to a CSV file
summary.to_csv("data/summary_statistics.csv")

# ------------------------------------------------------
# 5. EXPLANATION OF STATISTICS
# ------------------------------------------------------

# Print explanations of the statistical measures
print("\nStatistical Measures Explanation:")
print("Mean: The average value of the measurements")
print("Median: The middle value when measurements are arranged in order")
print("Standard Deviation: Measures how spread out the measurements are from the mean")
print("Variance: The square of the standard deviation, indicating the dispersion of data")

# ------------------------------------------------------
# 6. INFERENCES FROM DATA
# ------------------------------------------------------

print("\nInferences from Data Analysis:")

# Compare means across plant types
max_width_plant = summary['mean_width'].idxmax()
min_width_plant = summary['mean_width'].idxmin()
max_length_plant = summary['mean_length'].idxmax()
min_length_plant = summary['mean_length'].idxmin()

print(f"1. {max_width_plant} has the widest leaves on average ({summary.loc[max_width_plant, 'mean_width']:.2f} cm).")
print(f"2. {min_width_plant} has the narrowest leaves on average ({summary.loc[min_width_plant, 'mean_width']:.2f} cm).")
print(f"3. {max_length_plant} has the longest leaves on average ({summary.loc[max_length_plant, 'mean_length']:.2f} cm).")
print(f"4. {min_length_plant} has the shortest leaves on average ({summary.loc[min_length_plant, 'mean_length']:.2f} cm).")

# Identify most variable plant type
max_var_width_plant = summary['var_width'].idxmax()
max_var_length_plant = summary['var_length'].idxmax()

print(f"5. {max_var_width_plant} shows the most variation in leaf width (variance: {summary.loc[max_var_width_plant, 'var_width']:.2f}).")
print(f"6. {max_var_length_plant} shows the most variation in leaf length (variance: {summary.loc[max_var_length_plant, 'var_length']:.2f}).")

# Check for potential relationships between leaf length and width
correlation = data['Leaf-length (cm)'].corr(data['Leaf-width (cm)'])
print(f"7. The correlation between leaf length and width is {correlation:.2f}.")

if correlation > 0.7:
    print("   This indicates a strong positive relationship between leaf length and width.")
elif correlation > 0.3:
    print("   This indicates a moderate positive relationship between leaf length and width.")
else:
    print("   This indicates a weak relationship between leaf length and width.")

print("\n8. Looking at the scatter plot, we can observe if the plant types form distinct clusters,")
print("   which would suggest that leaf dimensions could be used to identify plant types.")