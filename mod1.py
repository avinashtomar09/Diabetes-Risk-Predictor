import pandas as pd

def load_database():
    # Reads the dataset and returns the required data. 
    data = pd.read_csv('dataset.csv')
    return data