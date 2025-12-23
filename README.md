# Employee Attrition Prediction & HR Analytics System

End-to-end ML project to predict employee attrition and provide HR analytics. Suitable to present as internship-level work.

## Project Structure
```
Employee-Attrition-Prediction/
├── data/
│   └── employee_attrition_sample.csv   # place dataset here (not included)
├── models/
├── notebooks/
│   └── EDA.ipynb
├── src/
│   ├── preprocess.py
│   ├── model.py
│   ├── evaluate.py
│   └── utils.py
├── api/
│   └── app.py
├── dashboard/
│   └── PowerBI_Instructions.md
├── requirements.txt
└── README.md
```

## Quickstart
1. Put your dataset (e.g., IBM HR Attrition CSV) into `data/employee_attrition.csv`
2. Create venv and install:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Preprocess & train:
   ```bash
   python src/model.py --data_path data/employee_attrition.csv --train
   ```
4. Run API:
   ```bash
   python api/app.py
   ```
5. Open Power BI and follow `dashboard/PowerBI_Instructions.md` to create the dashboard.
