# Customer Shopping Behaviour Analysis

> An end-to-end data analytics project exploring customer shopping behaviour using Python, SQL, and Power BI.

## Table of Contents

- [Project Overview](#project-overview)
- [Business Objectives](#business-objectives)
- [Dataset](#dataset)
- [Tools and Technologies](#tools-and-technologies)
- [Project Workflow](#project-workflow)
- [Data Cleaning and Feature Engineering](#data-cleaning-and-feature-engineering)
- [SQL Analysis](#sql-analysis)
- [Power BI Dashboard](#power-bi-dashboard)
- [Key Insights](#key-insights)
- [Project Structure](#project-structure)
- [How to Run the Project](#how-to-run-the-project)
- [Results and Deliverables](#results-and-deliverables)
- [Future Improvements](#future-improvements)
- [Author](#author)

## Project Overview

The **Customer Shopping Behaviour Analysis** project examines customer purchasing patterns, shopping frequency, review ratings, and purchase amounts. Python is used to clean and prepare the dataset, SQL is used to answer analytical questions, and Power BI is used to present results through an interactive dashboard.

The goal is to turn customer transaction and behaviour data into clear findings that can help a business understand its customers and make better decisions.

## Business Objectives

- Understand customer shopping and purchase patterns.
- Analyze purchase amounts and review ratings.
- Compare shopping behaviour across age groups.
- Standardize purchase-frequency values for analysis.
- Use SQL to answer business-focused questions.
- Present key performance indicators and findings in Power BI.

## Dataset

**Dataset file:** `customer_shopping_behavior.csv`

The project uses a customer shopping behaviour dataset. Based on the current Python workflow, the analysis includes fields such as `Age`, `Review Rating`, `Purchase Amount (USD)`, and `Frequency of Purchases`. The exact number of rows, full column list, and source should be confirmed from the CSV file.

| Dataset detail | Description |
|---|---|
| File | `customer_shopping_behavior.csv` |
| Format | CSV |
| Subject | Customer shopping behaviour |
| Data preparation | Python with Pandas and NumPy |
| Analysis | SQL |
| Visualization | Power BI |

> **Dataset source:** Add the original source or download page here. Before publishing the dataset, check its license and whether redistribution is permitted.

## Tools and Technologies

| Tool / Technology | Purpose |
|---|---|
| Python | Data preparation and analysis |
| Pandas | Loading, cleaning, and transforming tabular data |
| NumPy | Creating age-group categories and other data transformations |
| SQL | Querying and analyzing the prepared data |
| SQLAlchemy | Connecting Python to a SQL database |
| PostgreSQL / MySQL / SQL Server | Database engine, depending on the configured environment |
| Power BI Desktop | Dashboard and data visualization |
| Git and GitHub | Version control and project portfolio |

Only list the database engine you actually used in the final project.

## Project Workflow

### 1. Load the Dataset

The CSV file is loaded into a Pandas DataFrame.

```python
import pandas as pd
import numpy as np

df = pd.read_csv("customer_shopping_behavior.csv")

print(df.head())
print(df.shape)
print(df.info())
```

### 2. Explore the Data

Initial exploration checks the dataset's dimensions, column names, data types, missing values, duplicate rows, and descriptive statistics.

Useful checks include:

```python
print(df.shape)
print(df.info())
print(df.isnull().sum())
print(df.duplicated().sum())
print(df.describe(include="all"))
```

### 3. Clean and Prepare the Data

The current Python script performs these transformations:

- Fills missing values in `Review Rating` with the column median.
- Converts column names to lowercase.
- Replaces spaces in column names with underscores.
- Renames `purchase_amount_(usd)` to `purchase_amount`.
- Creates an `age_group` feature from `age`.
- Maps `frequency_of_purchases` to an estimated number of days between purchases.
- Drops the `promo_code_used` column.

**Important:** Dropping `promo_code_used` removes that field from later analysis. Keep it if you want to investigate promotional-code usage. Also verify that the frequency labels and their mapped day values match the meaning of the source dataset.

### 4. Create Age Groups

The script groups customers by age:

| Condition | Group |
|---|---|
| Age below 25 | Young Adult |
| Age 25 to below 40 | Adult |
| Age 40 to below 60 | Middle-aged |
| Age 60 or above | Senior |

The grouping is implemented with `numpy.select()`.

### 5. Standardize Purchase Frequency

The script converts purchase-frequency categories into approximate day intervals to make the field easier to analyze numerically.

| Frequency category | Mapped days in the current script |
|---|---:|
| Fortnightly | 14 |
| Weekly | 7 |
| Quarterly | 90 |
| Bi-Weekly | 14 |
| Annually | 365 |
| Every 3 Months | 90 |

These values are estimates, not measured time intervals. Review the category definitions before using them in calculations. In particular, “Quarterly” and “Every 3 Months” represent the same approximate interval, while “Fortnightly” and “Bi-Weekly” are also commonly equivalent.

### 6. Load the Prepared Data into SQL

The Python project imports SQLAlchemy and URL-encoding utilities, suggesting a database connection is configured in the script. The prepared DataFrame can be loaded into the selected SQL database and queried for business insights.

Typical analysis questions include:

- What is the average purchase amount?
- Which age groups have the highest purchase amounts?
- How do review ratings vary across customer groups?
- Which shopping-frequency categories are most common?
- What customer segments should the business investigate further?

The final questions and findings should match the SQL queries in `Customer_data_behavior SQL.sql`.

## SQL Analysis

The SQL script in this project is:

`Customer_data_behavior SQL.sql`

Use it to perform aggregations, comparisons, sorting, and other analysis against the prepared data. Depending on the database and the actual schema, queries may use `GROUP BY`, aggregate functions such as `AVG()` and `COUNT()`, filtering with `WHERE`, and sorting with `ORDER BY`.

Example query pattern (adjust the table and column names to match your database):

```sql
SELECT
    age_group,
    COUNT(*) AS customer_count,
    ROUND(AVG(purchase_amount), 2) AS average_purchase_amount
FROM customer_shopping_behavior
GROUP BY age_group
ORDER BY average_purchase_amount DESC;
```

Make sure the database table contains the cleaned columns used in the query. SQL syntax can vary slightly between PostgreSQL, MySQL, and SQL Server.

## Power BI Dashboard

The Power BI report file is:

`Customer_behavior_Dashboard.pbix`

The dashboard is intended to communicate customer behaviour and purchase patterns visually. Depending on the visuals currently included, it may present:

- Purchase amount KPIs.
- Customer comparisons by age group.
- Review-rating summaries.
- Purchase-frequency analysis.
- Category-level comparisons and filters.

### Add a Dashboard Screenshot

Save a screenshot of the finished dashboard as `images/dashboard.png`, then display it here:

```markdown
![Customer Shopping Behaviour Power BI Dashboard](images/dashboard.png)
```

Remove or update the image reference if your screenshot uses a different filename.

## Key Insights

Add verified findings from your SQL queries and Power BI dashboard here. Do not treat the following prompts as results until you have calculated them from the dataset.

- **Purchase behaviour:** `[Summarize the main purchase-amount pattern.]`
- **Age-group comparison:** `[Describe differences between age groups.]`
- **Customer feedback:** `[Summarize the review-rating results.]`
- **Shopping frequency:** `[Identify the most common purchase-frequency group.]`
- **Business recommendation:** `[Suggest an action supported by your analysis.]`

## Project Structure

```text
Customer_Shopping_Behaviour/
├── customer_shopping_behavior.csv
├── main.py
├── Customer_data_behavior SQL.sql
├── Customer_behavior_Dashboard.pbix
├── images/
│   └── dashboard.png
└── README.md
```

This structure reflects the files visible in the project workspace, with `images/dashboard.png` as an optional folder to create for the dashboard screenshot.

## How to Run the Project

### Prerequisites

- Python installed
- VS Code or another Python editor
- Required Python packages
- A configured SQL database if you want to run the database-loading and SQL-analysis steps
- Power BI Desktop to open the dashboard

### 1. Open the project folder

Open `Customer_Shopping_Behaviour` in VS Code.

### 2. Install dependencies

The script uses Pandas, NumPy, SQLAlchemy, and Python's URL parsing utilities. Install the required packages:

```bash
python -m pip install pandas numpy sqlalchemy
```

Install the database-specific SQLAlchemy driver for your selected database if it is required. For example, PostgreSQL commonly uses `psycopg` or `psycopg2`, while MySQL commonly uses `PyMySQL`.

### 3. Check the dataset path

Keep `customer_shopping_behavior.csv` in the project directory, or update the path in `main.py`:

```python
df = pd.read_csv("customer_shopping_behavior.csv")
```

### 4. Configure the database connection

Check the database connection code in `main.py`. Update the database URL, database name, username, and other settings for your local environment.

**Security:** Do not commit passwords, access tokens, or other secrets to GitHub. Use environment variables or a local configuration file excluded through `.gitignore`.

### 5. Run the Python script

From the project directory, run:

```bash
python main.py
```

Review any printed output and confirm that the transformations complete successfully. If `main.py` writes data to a database, make sure the database service is running and its connection settings are correct.

### 6. Run the SQL queries

Open `Customer_data_behavior SQL.sql` in your SQL editor, select the correct database, and execute the queries. Verify that the table and column names match the cleaned dataset.

### 7. Open the Power BI dashboard

Open `Customer_behavior_Dashboard.pbix` in Power BI Desktop. Configure the data source if prompted, then refresh the report to load the latest data.

## Results and Deliverables

- [x] Dataset file included in the project workspace
- [x] Python data-preparation script
- [x] SQL analysis file
- [x] Power BI dashboard file
- [ ] Dashboard screenshot added to the README
- [ ] Actual insights and recommendations documented
- [ ] Dataset source and final schema documented

## Future Improvements

- Add automated data-quality checks for missing values, duplicates, and unexpected categories.
- Keep a documented record of all cleaning and transformation decisions.
- Compare purchase behaviour across additional customer segments.
- Add validated KPIs and clearer dashboard tooltips.
- Automate the data refresh process.
- Add reproducible setup instructions and a `requirements.txt` file.

## Conclusion

This project combines Python, SQL, and Power BI to analyze customer shopping behaviour. Python prepares the data, SQL supports structured analysis, and Power BI communicates findings through a dashboard. Once the verified insights and recommendations are added, the repository can serve as a portfolio example of an end-to-end data analytics workflow.

## Author

**Name:** `[Your Name]`  
**GitHub:** `[Your GitHub profile or repository link]`  
**Project:** Customer Shopping Behaviour Analysis
