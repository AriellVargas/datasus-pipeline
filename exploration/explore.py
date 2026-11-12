import pandas as pd

caminho = "/home/ariel/pysus/downloads/ducklake/sih/RDRS2501.parquet"
df = pd.read_parquet(caminho)

print(df.shape)
print(df.dtypes)
