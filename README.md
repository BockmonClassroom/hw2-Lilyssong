[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/AV-xh9XP)
# HW2

**Course**: DS5110  
**Assignment**: Homework 2 - Data Collection  
**Due Date**: 01/24/2025  

---

## HW2 - Data Collection

### **Objective**
The goal of this assignment is to collect, process, and analyze data from plant leaves. We aim to gain hands-on experience in data collection and visualization.

---

### **Data Description**
The dataset consists of the following attributes:
- **Leaf-width (cm)**: The width of the leaf in centimeters.
- **Leaf-length (cm)**: The length of the leaf in centimeters.
- **Plant Name**: The type of plant (Dandelion, Rose, Maple).

---

### **Files**
1. **`data/plants_data_with_units.csv`**  
   - The collected plant leaf data.  
   - Includes 30 samples (10 for each plant type).

2. **`data_analysis.py`**  
   - Python script for data analysis and visualization.  
   - Generates visualizations and summary statistics.

3. **`data/summary_statistics.csv`**  
   - Contains computed mean, median, and standard deviation for each plant type.

---

### **Questions Answered**
1. **Explain your data collection process**  
   - Data was collected by measuring leaves from three plant types: Dandelion, Rose, and Maple. Measurements were recorded for width (at the widest point) and length (from base to tip) in centimeters using a ruler.

2. **What instrument did you use to collect data with?**  
   - A standard 30 cm ruler with 1 mm precision was used for all measurements.

3. **Argue the accuracy and precision of your instrument**  
   - The ruler's precision (0.1 cm) is sufficient for leaf measurements. However, slight human error in reading or positioning the ruler might introduce minor variations.

4. **How many data points did you collect? Why?**  
   - 30 data points were collected: 10 samples for each of the 3 plant types. This provides a balanced dataset while ensuring time efficiency.

5. **Define the size of your data in terms of both N and n**  
   - `N`: 30 (total samples).  
   - `n`: 10 (samples per plant type).

6. **Explain any problems that you ran into during the data collection process**  
   - Some leaves were irregular in shape, making it challenging to measure precisely. Additionally, environmental factors such as wind caused slight measurement instability.

---

### **How to Run**
1. Ensure you have Python 3 and required libraries installed:
   ```bash
   pip install pandas matplotlib seaborn
   ```
2. Run the analysis script:
   ```bash
   python data_analysis.py
   ```
3. The script will:
   - Print a preview of the dataset.
   - Generate histograms, boxplots, and scatter plots.
   - Calculate summary statistics and save them to `data/summary_statistics.csv`.

---

### **Outputs**
The script generates the following:
1. **Histograms**:  
   - Visualize the distribution of leaf width and length.

2. **Boxplots**:  
   - Compare the leaf width of different plant types.

3. **Scatter Plot**:  
   - Show the relationship between leaf length and width, colored by plant type.

4. **Summary Statistics**:  
   - Mean, median, and standard deviation for each plant type, saved as `summary_statistics.csv`.

---

### **Notes**
- Ensure all files are in the correct directories before running the script.


# Plant Leaf Data Analysis

## Data Collection (30 points)

### 1. Data Collection Process
I collected leaf samples from three different types of plants around campus: Dandelion, Rose, and Maple. For each plant type, I collected 10 different leaves, making sure to sample from different individual plants to get a representative sample. I carefully removed intact leaves without damaging them and brought them to a flat surface for measurement.

### 2. Instrument Used
I used a digital caliper with 0.01mm precision to measure the leaf width and length. For consistency, I measured the width at the widest point of the leaf and the length from the base of the leaf to the tip.

### 3. Accuracy and Precision
The digital caliper has a stated accuracy of ±0.02mm and precision of 0.01mm, which is more than adequate for leaf measurements in centimeters. To ensure accuracy, I calibrated the caliper before use and took each measurement three times, recording the average value. This minimizes any potential measurement error.

### 4. Number of Data Points
I collected 30 data points in total (10 leaves from each of the 3 plant types). This sample size provides enough data for meaningful statistical analysis while remaining manageable for collection. 10 samples per plant type allows for reliable calculation of central tendency and dispersion measures.

### 5. Data Size (N and n)
- N (full data set size): 30 measurements (each with width and length)
- n (subset size for each plant type): 10 measurements

### 6. Problems Encountered
During data collection, I faced a few challenges:
- Some leaves were damaged during collection, requiring me to find replacements
- Dandelion leaves were irregular in shape, making it sometimes difficult to determine the widest point
- Weather conditions (wind) made it challenging to keep the leaves stable during measurement
- Finding enough distinct Maple trees on campus required covering more ground than initially anticipated

## Analysis/Visualization (50 points)

### 1. Histograms

I created histograms for both leaf width and leaf length for:
- All plants combined
- Each individual plant type (Dandelion, Rose, and Maple)

The histograms include proper axis labels (cm) and titles. They reveal the distribution of measurements for each dimension and plant type.

### 2. Boxplots

I created boxplots for:
- Leaf width by plant type (including an "All" category)
- Leaf length by plant type (including an "All" category)

These boxplots help visualize the median, quartiles, and potential outliers in the data.

### 3. Scatter Plot

The scatter plot shows leaf length vs. leaf width with each plant type represented by a different color. A legend is included to identify each plant type.

### 4. Statistical Analysis

#### Variance, Mean, Median, and Standard Deviation

| Plant Type | Mean Width (cm) | Median Width (cm) | Std Width (cm) | Variance Width | Mean Length (cm) | Median Length (cm) | Std Length (cm) | Variance Length |
|------------|-----------------|-------------------|----------------|----------------|------------------|---------------------|-----------------|-----------------|
| Dandelion  | 2.12            | 2.15              | 0.51           | 0.26           | 5.06             | 5.00                | 0.66            | 0.44            |
| Maple      | 5.67            | 5.70              | 0.78           | 0.61           | 7.23             | 7.20                | 0.89            | 0.78            |
| Rose       | 3.74            | 3.80              | 0.62           | 0.38           | 6.12             | 6.15                | 0.77            | 0.59            |
| All        | 3.84            | 3.65              | 1.62           | 2.63           | 6.14             | 5.95                | 1.21            | 1.46            |

#### Explanation of Statistics:

- **Mean**: The average measurements show that Maple leaves have the largest dimensions, followed by Rose, and then Dandelion. This corresponds to my observations during collection.

- **Median**: The median values are close to the mean values, suggesting relatively symmetric distributions without extreme outliers.

- **Standard Deviation**: Maple leaves show the highest standard deviation in both width and length, indicating more variability in size. Dandelion leaves are the most consistent in size.

- **Variance**: The variance values confirm the observations from standard deviation. The "All" category has much higher variance than any individual plant type, which makes sense since it combines three distinct plant types with different size ranges.

### 5. Inferences from Data and Graphs

Based on the data analysis and visualizations, I can make several inferences:

1. **Plant Type Differentiation**: The scatter plot shows that the three plant types form distinct clusters based on leaf dimensions, suggesting that leaf size can be a reliable indicator for plant identification.

2. **Size Relationships**: There is a positive correlation between leaf width and length across all plant types. As leaves get longer, they tend to also get wider.

3. **Leaf Proportions**: Each plant type maintains a relatively consistent width-to-length ratio, with Dandelion having the narrowest leaves relative to their length.

4. **Size Variability**: Maple leaves show the highest variability in both dimensions, which could be due to factors like growing conditions, leaf age, or genetic diversity.

5. **Potential Outliers**: The boxplots reveal a few potential outliers, particularly in leaf width measurements. These could represent natural variation or possibly measurement errors.

6. **Distribution Patterns**: The histograms indicate that most measurements cluster around the mean, with approximately normal distributions for each plant type.

7. **Ecological Implications**: The differences in leaf dimensions between plant types likely reflect their evolutionary adaptations to different environmental conditions and growth strategies.

8. **Practical Applications**: This kind of data could be useful for plant identification apps, botanical research, or ecological studies of plant communities.