import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#### Task 1. Read CSV file and transfer it into DataFrame


df = pd.read_csv("/Users/pradnya/python-projects/python-tasks/Week-3/Cars93_missing.csv", encoding="utf-8")

print(df.head())
print(df.info())
print("Shape:", df.shape)

#### Task 2. Transfer object Series into index column of the dataframe

df_task2 = df.set_index("Manufacturer", drop=False)

print(df_task2.head())
print("Index name:", df_task2.index.name)

#### Task 3. Change the data in the column of DataFrame according to some condition

df_task3 = df.copy()
df_task3["Price"] = pd.to_numeric(df_task3["Price"], errors="coerce")

df_task3.loc[df_task3["Price"] > 30, "Price"] = 30

print(df_task3[["Price"]].head(10))

#### Task 4. Get names of the DataFrame columns and sum of losted values DF

print(df.columns.tolist())
print(df.isna().sum())

#### Task 5. Ex-change 2 columns, use function for it. Sort coulumn by name

df_task5 = df.copy()
columns = df_task5.columns.tolist()

i = columns.index("Price")
j = columns.index("MPG.city")
columns[i], columns[j] = columns[j], columns[i]

df_task5 = df_task5[columns]
df_task5 = df_task5.sort_index(axis=1)

#### Task 6. Delete upper and lower 5% in object DataFrame

df_task6 = df.copy()
df_task6["Price"] = pd.to_numeric(
    df_task6["Price"], errors="coerce"
)

lower = df_task6["Price"].quantile(0.05)
upper = df_task6["Price"].quantile(0.95)

df_task6 = df_task6[df_task6["Price"].between(lower, upper)].copy()

#### Task 7. Replay ( Apply) missed values in the Column with average values.

df_task7 = df.copy()
df_task7["Price"] = pd.to_numeric(
    df_task7["Price"], errors="coerce"
)
df_task7["Price"] = df_task7["Price"].fillna(
    df_task7["Price"].mean()
)

#### Task 8. Create two data frames using the two Dicts, Merge two
# data frames, and append the second data frame as a new
# column to the first data frame.


dict1 = {
    "ID": [1, 2, 3],
    "Name": ["Asha", "Ravi", "Maya"]
}
dict2 = {
    "ID": [1, 2, 3],
    "Score": [85, 90, 78]
}

df1 = pd.DataFrame(dict1)
df2 = pd.DataFrame(dict2)

merged_df = pd.merge(df1, df2, on="ID", how="inner")
appended_df = pd.concat(
    [df1, df2[["Score"]]], axis=1
)

#### Task 9. For any column create histogram

plt.hist(df_task7["Price"].dropna(), bins=10)
plt.title("Distribution of Car Prices")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("price_histogram.png")
plt.show()

#### Task 10. Create Correlation Matrix for any column

numeric_df = df.select_dtypes(include="number")
correlation_matrix = numeric_df.corr(method="pearson")
print(correlation_matrix)