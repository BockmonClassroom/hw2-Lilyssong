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

4. **`answers.pdf` (if applicable)**  
   - Written responses to the data collection questions.

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
