import pandas as pd
import numpy as np
df=pd.read_csv("customer_shopping_behavior.csv")

df["Review Rating"] = df["Review Rating"].fillna(df["Review Rating"].median())

df.columns=df.columns.str.lower()
df.columns=df.columns.str.replace(' ','_')

df=df.rename(columns={'purchase_amount_(usd)':'purchase_amount'})

df["age_group"] = np.select(
    [
        df["age"] < 25,
        df["age"] < 40,
        df["age"] < 60
    ],
    [
        "Young Adult",
        "Adult",
        "Middle-aged"
    ],
    default="Senior"
)

frequency_mapping={
    'Fortnightly':14,
    'Weekly':7,
    'Quarterly':90,
    'Bi-Weekly':14,
    'Annually':365,
    'Every 3 Months':90
}
df["purchase_frequency_days"]=df["frequency_of_purchases"].map(frequency_mapping)
df=df.drop("promo_code_used",axis=1)

# Data loading code
from sqlalchemy import create_engine
from urllib.parse import quote_plus

password = quote_plus("Parvesh@2003")

engine = create_engine(
    f"mysql+pymysql://root:{password}@localhost:3306/customer_analysis"
)

df.to_sql(
    "customer_data",
    engine,
    if_exists="replace",
    index=False
)
print("Data loaded successfully!")