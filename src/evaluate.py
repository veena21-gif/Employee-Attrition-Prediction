import joblib
import pandas as pd
from sklearn.metrics import confusion_matrix, classification_report, roc_auc_score
from src.preprocess import preprocess_pipeline

def evaluate_model(model_path, data_path):
    model = joblib.load(model_path)
    df = preprocess_pipeline(data_path)
    X = df.drop('Attrition', axis=1)
    y = df['Attrition']
    preds = model.predict(X)
    proba = model.predict_proba(X)[:,1] if hasattr(model, 'predict_proba') else None
    print('Classification Report:')
    print(classification_report(y, preds))
    if proba is not None:
        print('ROC AUC:', roc_auc_score(y, proba))

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', required=True)
    parser.add_argument('--data', required=True)
    args = parser.parse_args()
    evaluate_model(args.model, args.data)
