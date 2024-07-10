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

# Change column names to match the general DataFrame
prenatal_df = prenatal_df.rename(columns={'HOSPITAL': 'hospital', 'Sex': 'gender'})
sports_df = sports_df.rename(columns={'Hospital': 'hospital', 'Male/female': 'gender'})

# Merge DataFrames into one
merged_df = pd.concat([general_df, prenatal_df, sports_df], ignore_index=True)

# Remove the 'Unnamed: 0' column
merged_df = merged_df.drop(columns=['Unnamed: 0'])

# Print random 20 rows from the merged DataFrame
print(merged_df.sample(n=20, random_state=30))
