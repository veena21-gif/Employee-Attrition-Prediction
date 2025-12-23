import argparse, os, joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from src.preprocess import preprocess_pipeline

def train_model(data_path, model_out='models/attrition_model.pkl'):
    df = preprocess_pipeline(data_path)
    if 'Attrition' not in df.columns:
        raise ValueError('Target column Attrition not found in preprocessed data.')

    X = df.drop('Attrition', axis=1)
    y = df['Attrition']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    model = RandomForestClassifier(n_estimators=200, max_depth=10, random_state=42)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    print('Test Accuracy:', accuracy_score(y_test, preds))
    print(classification_report(y_test, preds))

    os.makedirs(os.path.dirname(model_out), exist_ok=True)
    joblib.dump(model, model_out)
    print('Saved model to', model_out)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_path', required=True, help='Path to raw CSV')
    parser.add_argument('--train', action='store_true')
    parser.add_argument('--model_out', default='models/attrition_model.pkl')
    args = parser.parse_args()
    if args.train:
        train_model(args.data_path, args.model_out)
