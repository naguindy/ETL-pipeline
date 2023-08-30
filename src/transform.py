# definition to drop duplicates
# ASK SARAH WHY IT WORKED WITHOUT IMPORTING PANDAS HERE
def drop_duplicates(df):
    if df.duplicated().sum() > 0:
        print(f"number of duplicates = {df.duplicated().sum()}")
        df_cleaned = df.drop_duplicates(keep='first')

    else:
        print("no duplicates in dataframe")
        df_cleaned = df
    return df_cleaned
