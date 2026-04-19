import pandas as pd

FILE = "data/expenses.csv"

def load_data():
    try:
        df = pd.read_csv(FILE)
    except:
        df = pd.DataFrame(columns=["Date", "Category", "Amount"])
    return df

def save_data(df):
    df.to_csv(FILE, index=False)
