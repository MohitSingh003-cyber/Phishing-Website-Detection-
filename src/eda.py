import pandas as pd

def run_eda():
    print("Phishing Website Detection Project")

    #Load dataset
    data = pd.read_csv("data/PhishingData.csv")
    print("\n Dataset Loaded Successfully")

    #we performing EDA(Exploratory Data Analysis)

    #Show first rows
    print("\n first 5 rows:")
    print(data.head())

    #Show first columns
    print("\n first 5 columns:")
    print(data.columns)

    #Show Dataset size
    print("\n Shape: ")
    print(data.shape)

    # Missing values Check
    print("\n Missing Values:")
    print(data.isnull().sum())
    # dataset is already cleaned no missing value's are here.

    return data


