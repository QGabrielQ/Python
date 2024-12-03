import pandas as pd
df = pd.read_csv("/home/gabriel/Programming/Python/Lab10/miasta.csv")
print(df.to_string())
data = {
    'Rok': [2010],
    'Gdansk': [460],
    'Poznan': [555],
    'Szczecin': [405]
}
dg = pd.DataFrame(data)
dg.to_csv('/home/gabriel/Programming/Python/Lab10/miasta.csv', mode='a', index=False, header=False)
df = pd.read_csv("/home/gabriel/Programming/Python/Lab10/miasta.csv")
print(df.to_string())