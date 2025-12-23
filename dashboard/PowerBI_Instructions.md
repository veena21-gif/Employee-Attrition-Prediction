Power BI Dashboard Instructions (Employee Attrition)

Recommended visuals:
1. KPI cards: Overall Attrition Rate, Avg Tenure, Avg Monthly Income, % Overtime
2. Bar chart: Attrition % by Department (use measure: attrition_count / total_count)
3. Heatmap / matrix: JobRole vs Attrition Rate
4. Line chart: Attrition trend over months (if you have hire/leave dates)
5. Scatter: MonthlyIncome vs YearsAtCompany colored by Attrition
6. Slicer filters: Age, Gender, Department, JobRole, OverTime

Steps:
- Load `data/employee_attrition.csv` into Power BI Desktop.
- Create calculated columns/measures: AttritionRate, AvgTenure, etc.
- Use bookmarks to create a "What-if" scenario (e.g., reduce OverTime by 20%).
- Export screenshots for README if required.
