import pandas as pd


class Analysis:

    def main(self):
        frames = self.load_data()
        df = pd.concat(frames, ignore_index=True)
        df.drop(df.columns[0], axis=1, inplace=True)
        df = self.preprocess(df)

        # Question 1: Which hospital has the highest number of patients?
        hospital_counts = df['hospital'].value_counts()
        print(f'The answer to the 1st question is {hospital_counts.index[0]}')

        # Question 2: What share of the patients in the general hospital suffers from stomach-related issues?
        general_hospital = df[df['hospital'] == 'general']
        stomach_issues = general_hospital[general_hospital['diagnosis'] == 'stomach'].shape[0]
        share = stomach_issues / general_hospital.shape[0]
        print(f'The answer to the 2nd question is {share:.3f}')

        # Question 3: What share of the patients in the sports hospital suffers from dislocation-related issues?
        sports_hospital = df[df['hospital'] == 'sports']
        dislocation_issues = sports_hospital[sports_hospital['diagnosis'] == 'dislocation'].shape[0]
        share = dislocation_issues / sports_hospital.shape[0]
        print(f'The answer to the 3rd question is {share:.3f}')

        # Question 4: What is the difference in the median ages of the patients in the general and sports hospitals?
        general_median_age = general_hospital['age'].median()
        sports_median_age = sports_hospital['age'].median()
        age_diff = general_median_age - sports_median_age
        print(f'The answer to the 4th question is {age_diff}')

        # Question 5: In which hospital the blood test was taken the most often?
        blood_test_counts = df[df['blood_test'] == 't']['hospital'].value_counts()
        max_blood_tests = blood_test_counts.index[0]
        num_blood_tests = blood_test_counts.max()
        print(f'The answer to the 5th question is {max_blood_tests}, {num_blood_tests} blood tests')

    @staticmethod
    def load_data() -> list[pd.DataFrame]:
        FILES = ['general', 'prenatal', 'sports']
        frames = [pd.read_csv(f'test/{file}.csv') for file in FILES]
        keys = frames[0].keys()
        for frame in frames[1:]:
            frame.columns = keys
        return frames

    @staticmethod
    def preprocess(df: pd.DataFrame) -> pd.DataFrame:
        df.dropna(how='all', inplace=True)
        df.fillna({'gender': 'f'}, inplace=True)
        df.replace({'gender': {'female': 'f', 'male': 'm', 'woman': 'f', 'man': 'm'}}, inplace=True)
        for col in ['bmi', 'diagnosis', 'blood_test', 'ecg', 'ultrasound', 'mri', 'xray', 'children', 'months']:
            df.fillna({col: 0}, inplace=True)
        return df


if __name__ == '__main__':
    Analysis().main()
