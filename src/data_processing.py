import pandas as pd

data = pd.read_csv('data/Loan.csv')

def explore_data():
    print(data.head()) 
    print(data.describe())  
    print(data.info()) 
    print(data.isnull().sum()) 

if __name__ == "__main__":
    explore_data()