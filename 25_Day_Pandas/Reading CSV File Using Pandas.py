import pandas as pd

pd.set_option("display.max_rows", None, "display.max_columns", None)

df = pd.read_csv('weight-height.csv')

# print(df.head(5))
# print(df.shape)
# print(df.columns)
# print(df.tail(5))

heights = df['Height']
weights = df['Weight']
# print(heights)
# print(len(heights) == len(weights))

# print(weights.describe())
# print(df.describe())

