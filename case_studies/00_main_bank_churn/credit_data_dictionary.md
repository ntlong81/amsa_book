# Data Dictionary: Credit Scoring Dataset (credit_scoring_imbalanced.csv)

This dataset contains 1,000 credit records of loan applicants. It is designed to illustrate Logistic Regression, Discriminant Analysis (LDA), and imbalanced class evaluation.

| Column | Type | Description |
|---|---|---|
| CustomerID | Integer | Unique identifier for each customer |
| Age | Integer | Age of the customer in years |
| Income | Float | Annual income in millions VND |
| CreditScore | Integer | Credit bureau score (300 to 850) |
| DebtRatio | Float | Debt-to-income ratio (total monthly debt payments divided by monthly income) |
| NumOfDependents | Integer | Number of dependents in the household |
| SeriousDlqin2yrs | Integer | Binary target variable: 1 if customer defaulted on payments (delinquent), 0 otherwise |
