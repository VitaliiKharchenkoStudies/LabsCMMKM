import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('dataset.csv')


def process_csv():
    # Loop through columns
    for column in df.columns:
        # Convert numeric columns to float (if not already float)
        if df[column].dtype == 'int64' or df[column].dtype == 'float64':
            df[column] = df[column].apply(lambda x: float(x) if x != 'Not Available' else float('NaN'))

    # Save the modified DataFrame to a new CSV file
    df.to_csv("output.csv", index=False)


process_csv()


def remove_missing_data_and_outliers(input_file, output_file):
    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv(input_file)

    # Step a: Remove columns with more than 50% missing values
    missing_threshold = 0.5 * len(df)
    df = df.dropna(thresh=missing_threshold, axis=1)

    # Step b: Remove outliers based on the interquartile range (IQR) criterion
    # Define a function to detect and remove outliers in each numeric column
    def remove_outliers(column):
        Q1 = np.percentile(column, 25)
        Q3 = np.percentile(column, 75)
        IQR = Q3 - Q1
        lower_fence = Q1 - 3 * IQR
        upper_fence = Q3 + 3 * IQR
        return column[(column >= lower_fence) & (column <= upper_fence)]

    # Apply the remove_outliers function to all numeric columns
    numeric_columns = df.select_dtypes(include=[np.number])
    df[numeric_columns.columns] = numeric_columns.apply(remove_outliers, axis=0)

    # Save the cleaned DataFrame to a new CSV file
    df.to_csv(output_file, index=False)


# Example usage:
input_file_path = 'output.csv'
output_file_path = 'cleaned_output.csv'
remove_missing_data_and_outliers(input_file_path, output_file_path)


def conduct_eda(input_file):
    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv(input_file)

    # Convert "ENERGY STAR Score" to a numeric type
    df["ENERGY STAR Score"] = pd.to_numeric(df["ENERGY STAR Score"], errors='coerce')

    # Check if the conversion was successful
    if df["ENERGY STAR Score"].isna().any():
        print("Warning: Some values in 'ENERGY STAR Score' could not be converted to numeric.")

    # Increase the figure size
    plt.figure(figsize=(16, 6))

    # Create a FacetGrid for the density plots
    g = sns.FacetGrid(df, col="Primary Property Type - Self Selected", hue="Primary Property Type - Self Selected",
                      col_wrap=4)

    # Use kdeplot within FacetGrid
    g.map(sns.kdeplot, "ENERGY STAR Score", fill=True, warn_singular=False)

    # Set titles for subplots
    g.set_titles("Building Type: {col_name}")

    # Add a legend
    g.add_legend(title="Primary Property Type")

    # Adjust subplot spacing
    plt.subplots_adjust(top=0.9, bottom=0.1, left=0.1, right=0.9, hspace=0.4, wspace=0.2)

    # Return the FacetGrid object
    return g


# Example usage:
input_file_path = 'cleaned_output.csv'
facet_grid = conduct_eda(input_file_path)

# To display the first density plot, you can access it using facet_grid.axes[0]
first_plot = facet_grid.axes[0]
first_plot.set_title("First Density Plot")
plt.show()

def feature_engineering_and_selection(input_file, output_file):
    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv(input_file)

    # a) One-hot encoding of categorical features (district and building type)
    df = pd.get_dummies(df, columns=["Borough", "Primary Property Type - Self Selected"])

    # b) Taking the natural logarithm of numerical data
    numeric_columns = df.select_dtypes(include=[np.number])
    df[numeric_columns.columns] = np.log1p(numeric_columns)

    # c) Selection: Remove collinear features
    # Calculate the correlation matrix
    corr_matrix = df.corr().abs()

    # Create a mask for collinear features
    upper_tri = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))

    # Find and drop features with correlation greater than 0.6
    to_drop = [column for column in upper_tri.columns if any(upper_tri[column] > 0.6)]
    df = df.drop(columns=to_drop)

    # Save the modified DataFrame to a new CSV file
    df.to_csv(output_file, index=False)


# Example usage:
input_file_path = 'cleaned_output.csv'
output_file_path = 'feature_engineered_output.csv'
feature_engineering_and_selection(input_file_path, output_file_path)
