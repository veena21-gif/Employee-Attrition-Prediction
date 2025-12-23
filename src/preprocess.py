import pandas as pd
import numpy as np

def load_data(path):
    df = pd.read_csv(path)
    return df

def basic_cleaning(df):
    # drop duplicates
    df = df.drop_duplicates()
    # strip whitespace in column names
    df.columns = df.columns.str.strip()
    return df

def encode_and_feature_engineer(df):
    # Common example transformations for IBM Attrition dataset
    df = df.copy()
    # Map Attrition target
    if 'Attrition' in df.columns:
        df['Attrition'] = df['Attrition'].map({'Yes':1, 'No':0})

    # Convert categorical to dummies for a selected subset (to keep model simple)
    cat_cols = ['BusinessTravel','Department','EducationField','Gender','JobRole','MaritalStatus','OverTime']
    existing = [c for c in cat_cols if c in df.columns]
    df = pd.get_dummies(df, columns=existing, drop_first=True)

    # Fill NaNs with median
    df = df.fillna(df.median(numeric_only=True))

    return df

def preprocess_pipeline(path):
    df = load_data(path)
    df = basic_cleaning(df)
    df = encode_and_feature_engineer(df)
    return df

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_path', required=True)
    parser.add_argument('--out_path', default='data/cleaned_employee_attrition.csv')
    args = parser.parse_args()
    df = preprocess_pipeline(args.data_path)
    df.to_csv(args.out_path, index=False)
    print('Saved cleaned data to', args.out_path)
