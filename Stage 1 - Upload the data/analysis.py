# Importing necessary libraries
import pandas as pd

# Set display options
pd.set_option('display.max_columns', 8)

# Define file paths
general_path = 'test/general.csv'
prenatal_path = 'test/prenatal.csv'
sports_path = 'test/sports.csv'

# Read CSV files into DataFrames
general_df = pd.read_csv(general_path)
prenatal_df = pd.read_csv(prenatal_path)
sports_df = pd.read_csv(sports_path)

# Display first 20 rows of each DataFrame
print("General Dataset:")
print(general_df.head(20))
print("\nPrenatal Dataset:")
print(prenatal_df.head(20))
print("\nSports Dataset:")
print(sports_df.head(20))
