import pandas as pd

print("working...")
df = pd.read_csv("input.csv")
df2 = pd.read_csv("ONSPD_MAY_2023_UK.csv", usecols = ["pcds", "oseast1m", "osnrth1m", "osgrdind"])


df_result = df.merge(df2,how="left",left_on="inputpostcode",right_on="pcds")


df_result.to_csv("output.csv", index=False)


print(df_result)
