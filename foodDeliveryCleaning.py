import pandas as pd
import numpy as np

print("=" * 60)
print("FOOD DELIVERY DATA CLEANING")
print("=" * 60)


df = pd.read_csv("f440d17c-2e62-4c74-b0eb-bce6707b8c23.csv")

print("\nSTEP 2: DATASET LOADED")
print("Dataset loaded successfully!")


print("\nSTEP 3: FIRST 5 ROWS")
print(df.head())




print("\nSTEP 4: DATASET SIZE")

print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])




print("\nSTEP 5: COLUMN NAMES")

print(df.columns.tolist())


print("\nSTEP 6: DATA INFORMATION")

df.info()




print("\nSTEP 7: MISSING VALUES")

missing_values = df.isnull().sum()

print(missing_values)


# Display only columns having missing values

print("\nColumns with missing values:")

print(missing_values[missing_values > 0])



print("\nSTEP 8: MISSING VALUE PERCENTAGE")

missing_percentage = (df.isnull().sum() / len(df)) * 100

print(
    missing_percentage[missing_percentage > 0]
)



print("\nSTEP 9: DUPLICATE ROWS")

duplicate_count = df.duplicated().sum()

print("Number of duplicate rows:", duplicate_count)



if duplicate_count > 0:

    df = df.drop_duplicates()

    print("Duplicate rows removed.")

else:

    print("No duplicate rows found.")




print("\nSTEP 11: DUPLICATE ORDER IDs")

duplicate_order_ids = df['order_id'].duplicated().sum()

print("Duplicate order IDs:", duplicate_order_ids)



print("\nSTEP 12: CLEANING COLUMN NAMES")

df.columns = df.columns.str.strip()

df.columns = df.columns.str.lower()

df.columns = df.columns.str.replace(" ", "_")

print("Column names cleaned successfully.")

print(df.columns.tolist())



print("\nSTEP 13: CLEANING TEXT COLUMNS")

text_columns = df.select_dtypes(include="object").columns

for column in text_columns:

    df[column] = df[column].str.strip()

print("Text columns cleaned successfully.")



print("\nSTEP 14: CONVERTING DATE COLUMNS")

df["order_timestamp"] = pd.to_datetime(
    df["order_timestamp"],
    errors="coerce"
)

df["order_date"] = pd.to_datetime(
    df["order_date"],
    errors="coerce"
)

print("Date columns converted successfully.")



print("\nSTEP 15: DATE COLUMN DATA TYPES")

print(df[["order_timestamp", "order_date"]].dtypes)



print("\nSTEP 16: HANDLING MISSING TIP VALUES")

print(
    "Missing tip values before cleaning:",
    df["tip_amount"].isnull().sum()
)

# Missing tip means no tip was recorded,
# so we replace it with 0.

df["tip_amount"] = df["tip_amount"].fillna(0)

print(
    "Missing tip values after cleaning:",
    df["tip_amount"].isnull().sum()
)



print("\nSTEP 17: CUSTOMER TYPES")

print(df["customer_type"].value_counts())


print("\nPAYMENT METHODS")

print(df["payment_method"].value_counts())


print("\nORDER STATUS")

print(df["order_status"].value_counts())


print("\nWEATHER")

print(df["weather"].value_counts())


print("\nTRAFFIC LEVEL")

print(df["traffic_level"].value_counts())


print("\nSTEP 18: CHECKING RESTAURANT RATINGS")

invalid_restaurant_ratings = df[
    (df["restaurant_rating"] < 1) |
    (df["restaurant_rating"] > 5)
]

print(
    "Invalid restaurant ratings:",
    len(invalid_restaurant_ratings)
)


print("\nSTEP 19: CHECKING DELIVERY PARTNER RATINGS")

invalid_partner_ratings = df[
    (df["delivery_partner_rating"] < 1) |
    (df["delivery_partner_rating"] > 5)
]

print(
    "Invalid delivery partner ratings:",
    len(invalid_partner_ratings)
)


print("\nSTEP 20: CHECKING CUSTOMER RATINGS")

invalid_customer_ratings = df[
    (df["customer_rating"] < 1) |
    (df["customer_rating"] > 5)
]

print(
    "Invalid customer ratings:",
    len(invalid_customer_ratings)
)


print("\nSTEP 21: CHECKING CUSTOMER AGE")

invalid_age = df[
    (df["customer_age"] < 18) |
    (df["customer_age"] > 100)
]

print(
    "Invalid age records:",
    len(invalid_age)
)



print("\nSTEP 22: CHECKING DISCOUNT PERCENTAGE")

invalid_discount = df[
    (df["discount_percent"] < 0) |
    (df["discount_percent"] > 100)
]

print(
    "Invalid discount records:",
    len(invalid_discount)
)




print("\nSTEP 23: CHECKING DELIVERY DISTANCE")

invalid_distance = df[
    df["distance_km"] <= 0
]

print(
    "Invalid distance records:",
    len(invalid_distance)
)




print("\nSTEP 24: CHECKING ESTIMATED DELIVERY TIME")

invalid_estimated_time = df[
    df["estimated_delivery_time_minutes"] <= 0
]

print(
    "Invalid estimated delivery time records:",
    len(invalid_estimated_time)
)




print("\nSTEP 25: CHECKING ACTUAL DELIVERY TIME")

invalid_actual_time = df[
    df["actual_delivery_time_minutes"] < 0
]

print(
    "Invalid actual delivery time records:",
    len(invalid_actual_time)
)



print("\nSTEP 26: CHECKING LATE DELIVERY LOGIC")

# Only completed orders are considered because
# cancelled orders do not have an actual delivery time.

completed_orders = df[
    df["order_status"] == "Completed"
].copy()

completed_orders["calculated_late"] = (
    completed_orders["actual_delivery_time_minutes"]
    >
    completed_orders["estimated_delivery_time_minutes"]
).astype(int)

print(
    pd.crosstab(
        completed_orders["late_delivery"],
        completed_orders["calculated_late"]
    )
)




print("\nSTEP 27: CHECKING ORDER TOTAL")

calculated_total = (
    df["subtotal"]
    * (1 - df["discount_percent"] / 100)
    + df["tax_amount"]
    + df["service_fee"]
    + df["delivery_fee"]
)

total_difference = (
    df["order_total"] - calculated_total
).abs()

print(
    "Maximum difference in order total:",
    total_difference.max()
)




print("\nSTEP 28: FINAL MISSING VALUE CHECK")

print(df.isnull().sum())




print("\nSTEP 29: FINAL DUPLICATE CHECK")

print(
    "Duplicate rows:",
    df.duplicated().sum()
)



print("\nSTEP 30: FINAL DATASET INFORMATION")

print("Rows:", df.shape[0])
print("Columns:", df.shape[1])




output_file = "food_delivery_cleaned.csv"

df.to_csv(
    output_file,
    index=False
)

print("\nSTEP 31: DATASET SAVED")

print(
    "Cleaned dataset saved as:",
    output_file
)




print("\nSTEP 32: VERIFYING CLEANED DATASET")

cleaned_data = pd.read_csv(output_file)

print("Cleaned dataset shape:", cleaned_data.shape)

print("\nFirst 5 rows of cleaned dataset:")

print(cleaned_data.head())




print("\n" + "=" * 60)

print("DATA CLEANING COMPLETED SUCCESSFULLY!")

print("=" * 60)