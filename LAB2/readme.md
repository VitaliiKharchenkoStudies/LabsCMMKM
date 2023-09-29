# Data Analysis and Feature Engineering

This repository contains Python scripts for data analysis, data cleaning, exploratory data analysis (EDA), and feature engineering on a dataset. The dataset is loaded from a CSV file, and various operations are performed to prepare the data for further analysis and modeling.

## Functions

### 1. `process_csv()`

This function processes the input CSV file by converting numeric columns to float types and handling missing data. Numeric columns with missing values represented as "Not Available" are converted to NaN.

### 2. `remove_missing_data_and_outliers(input_file, output_file)`

This function removes columns with more than 50% missing values and outliers based on the interquartile range (IQR) criterion. It loads the input CSV file, performs data cleaning, and saves the cleaned data to the output CSV file.

### 3. `conduct_eda(input_file)`

This function conducts exploratory data analysis (EDA) on the cleaned dataset. It includes the following steps:

- Converts the "ENERGY STAR Score" column to a numeric type.
- Creates density plots of "ENERGY STAR Score" by building type using Seaborn's FacetGrid.

The function returns the FacetGrid object for further customization and analysis.

### 4. `feature_engineering_and_selection(input_file, output_file)`

This function performs feature engineering and selection on the cleaned dataset. It includes the following steps:

- One-hot encodes categorical features ("Borough" and "Primary Property Type - Self Selected").
- Takes the natural logarithm of numerical data.
- Removes collinear features based on a correlation coefficient threshold of 0.6.

The modified dataset is saved to the output CSV file.

as result you will see that plot. 


<img src="https://media.discordapp.net/attachments/917547349864230912/1157392875819126914/image.png?ex=6518719c&is=6517201c&hm=fe706d1d65ca0f42fb5ad0e02d2dc691e76df22b41d636078962114c9cc2201a&=&width=252&height=671">