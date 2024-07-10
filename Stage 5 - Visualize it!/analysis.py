import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class Analysis:

    def main(self):
        frames = self.load_data()
        df = pd.concat(frames, ignore_index=True)
        df.drop(df.columns[0], axis=1, inplace=True)
        df = self.preprocess(df)

        # Question 1: What is the most common age of a patient among all hospitals?
        bins = [0, 15, 35, 55, 70, 80]
        age_counts, _ = np.histogram(df['age'], bins=bins)
        most_common_age = bins[np.argmax(age_counts)]
        if most_common_age == 0:
            most_common_age = '0-15'
        elif most_common_age == 15:
            most_common_age = '15-35'
        elif most_common_age == 35:
            most_common_age = '35-55'
        elif most_common_age == 55:
            most_common_age = '55-70'
        else:
            most_common_age = '70-80'
        print(f'The answer to the 1st question: {most_common_age}')

        plt.hist(df['age'], bins=bins, edgecolor='black')
        plt.xlabel('Age')
        plt.ylabel('Count')
        plt.title('Age Distribution')
        plt.show()

        # Question 2: What is the most common diagnosis among patients in all hospitals?
        diagnosis_counts = df['diagnosis'].value_counts()
        most_common_diagnosis = diagnosis_counts.index[0]
        print(f'The answer to the 2nd question: {most_common_diagnosis}')

        plt.pie(diagnosis_counts, labels=diagnosis_counts.index, autopct='%1.1f%%')
        plt.title('Diagnosis Distribution')
        plt.show()

        # Question 3: Build a violin plot of height distribution by hospitals.
        sns.violinplot(x='hospital', y='height', data=df)
        plt.title('Height Distribution by Hospital')
        plt.show()

        # Answer to the third question
        print(
            "The answer to the 3rd question: It's because the sports hospital has a higher proportion of athletes, "
            "who tend to be taller, and the prenatal hospital has a higher proportion of pregnant women, who tend to "
            "be shorter.")

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
    import numpy as np

    Analysis().main()
