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

# Delete empty rows
merged_df = merged_df.dropna(how='all')

# Correct gender column values
gender_mapping = {
    'female': 'f',
    'male': 'm',
    'man': 'm',
    'woman': 'f'
}
merged_df['gender'] = merged_df['gender'].str.lower().map(gender_mapping)
merged_df.loc[merged_df['hospital'] == 'prenatal', 'gender'] = merged_df.loc[merged_df['hospital'] == 'prenatal', 'gender'].fillna('f')

# Replace NaN values with zeros
columns_to_fill_zero = ['bmi', 'diagnosis', 'blood_test', 'ecg', 'ultrasound', 'mri', 'xray', 'children', 'months']
merged_df[columns_to_fill_zero] = merged_df[columns_to_fill_zero].fillna(0)

# Print shape of the resulting DataFrame
print(f"Data shape: {merged_df.shape}")

# Print random 20 rows of the resulting DataFrame
print(merged_df.sample(n=20, random_state=30))
