import pandas as pd
import os
def run_eda():
    print("Phishing Website Detection Project")

    #Load dataset
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(BASE_DIR,"data","PhishingData.csv")
    data = pd.read_csv(file_path)
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


    # Clean Column Names
    data.columns = data.columns.str.strip()

    # Remove Useless Index Column
    if "index" in data.columns:
        data = data.drop("index", axis=1)
    print("\n Columns After Cleaning:")
    print(data.columns)

    #Split Features and Label
    X = data.drop("Result", axis = 1)
    y = data["Result"]
    print("\nFeature Shape:" , X.shape)
    print("Label Shape:", y.shape)
    return X, y


